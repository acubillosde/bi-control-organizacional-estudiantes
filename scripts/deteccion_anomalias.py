"""Pruebas de analítica forense sobre los pagos de COAGUA (entidad ficticia).

Pruebas incluidas:
    1. Ley de Benford (primer dígito): chi-cuadrado y MAD.
    2. Duplicados exactos y aproximados (número de factura normalizado).
    3. Reglas de control: fin de semana/festivo, segregación de funciones, pago antes de aprobación,
       aprobación sobre el límite, fraccionamiento, proveedor-empleado, proveedor nuevo, montos redondos.
    4. Valores atípicos por proveedor (z-score robusto con la mediana y la MAD).
    5. Isolation Forest (aprendizaje no supervisado) sobre variables del pago.

Uso:
    python scripts/deteccion_anomalias.py                 # datos de datos/integrador
    python scripts/deteccion_anomalias.py --evaluar       # compara contra la clave (solo repo docente)

Salidas (carpeta datos/resultados/):
    alertas_pagos.csv     una fila por pago y prueba que lo alerta (para cargar en Power BI)
    benford_resumen.csv   frecuencias observadas vs. esperadas por dígito
    puntaje_pagos.csv     puntaje de riesgo e Isolation Forest por pago
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.ensemble import IsolationForest

RAIZ = Path(__file__).resolve().parents[1]
DATOS = RAIZ / "datos" / "integrador"
SALIDA = RAIZ / "datos" / "resultados"


def cargar():
    fechas = ["fecha_factura", "fecha_registro", "fecha_aprobacion", "fecha_pago"]
    pagos = pd.read_csv(DATOS / "pagos.csv", parse_dates=fechas)
    prov = pd.read_csv(DATOS / "proveedores.csv", parse_dates=["fecha_creacion"], dtype={"cuenta_bancaria": str})
    emp = pd.read_csv(DATOS / "empleados.csv", dtype={"cuenta_bancaria": str})
    limites = pd.read_csv(DATOS / "limites_aprobacion.csv")
    festivos = pd.read_csv(DATOS / "festivos.csv", parse_dates=["fecha"])
    return pagos, prov, emp, limites, festivos


# ----------------------------------------------------------------------------- Benford
def benford(valores: pd.Series) -> tuple[pd.DataFrame, float, float]:
    """Devuelve la tabla por dígito, el estadístico chi-cuadrado (p-valor) y la MAD."""
    v = valores[valores >= 10].astype(str).str.lstrip("0").str[0].astype(int)
    obs = v.value_counts().reindex(range(1, 10), fill_value=0)
    esperado = np.log10(1 + 1 / np.arange(1, 10))
    tabla = pd.DataFrame({"digito": range(1, 10), "observado": obs.values,
                          "prop_observada": obs.values / obs.sum(), "prop_esperada": esperado})
    tabla["diferencia"] = tabla["prop_observada"] - tabla["prop_esperada"]
    chi2, p = stats.chisquare(obs.values, esperado * obs.sum())
    mad = float(np.mean(np.abs(tabla["diferencia"])))
    return tabla, p, mad


def interpretar_mad(mad: float) -> str:
    # Umbrales empíricos para el primer dígito atribuidos a Nigrini (2012); ver lecturas U4.
    if mad <= 0.006:
        return "conformidad cercana"
    if mad <= 0.012:
        return "conformidad aceptable"
    if mad <= 0.015:
        return "conformidad marginal"
    return "no conformidad"


# ----------------------------------------------------------------------------- pruebas
def normalizar_factura(s: pd.Series) -> pd.Series:
    return s.str.upper().str.replace(r"[^0-9]", "", regex=True).str.lstrip("0")


def pruebas(pagos, prov, emp, limites, festivos) -> pd.DataFrame:
    alertas = []

    def agregar(mask, prueba, detalle):
        sub = pagos.loc[mask, ["id_pago"]].copy()
        sub["prueba"], sub["detalle"] = prueba, detalle
        alertas.append(sub)

    # Duplicados exactos: mismo proveedor, factura y valor (se alertan todos los miembros del grupo)
    agregar(pagos.duplicated(["id_proveedor", "numero_factura", "valor"], keep=False),
            "Duplicado exacto", "Proveedor, factura y valor repetidos")
    # Duplicados aproximados: misma factura normalizada y valor, distinto texto
    pagos["_fact_norm"] = normalizar_factura(pagos["numero_factura"])
    aprox = pagos.duplicated(["id_proveedor", "_fact_norm", "valor"], keep=False) & \
        ~pagos.duplicated(["id_proveedor", "numero_factura", "valor"], keep=False)
    agregar(aprox, "Duplicado aproximado", "Factura con formato distinto y mismo valor")

    # Fin de semana o festivo
    fest = set(festivos["fecha"].dt.normalize())
    agregar((pagos["fecha_pago"].dt.weekday >= 5) | pagos["fecha_pago"].isin(fest),
            "Pago en día no hábil", "Sábado, domingo o festivo")
    # Segregación de funciones
    agregar(pagos["usuario_registra"] == pagos["usuario_aprueba"], "Segregación de funciones",
            "Mismo usuario registra y aprueba")
    # Pago antes de aprobación
    agregar(pagos["fecha_pago"] < pagos["fecha_aprobacion"], "Pago antes de aprobación",
            "Fecha de pago anterior a la aprobación")
    # Aprobación sobre el límite del cargo
    lim = emp.merge(limites, on="cargo")[["usuario_sistema", "limite_aprobacion"]]
    p = pagos.merge(lim, left_on="usuario_aprueba", right_on="usuario_sistema", how="left")
    agregar((p["valor"] > p["limite_aprobacion"]).values, "Aprobación sobre el límite",
            "Valor superior al límite de aprobación del cargo")
    # Fraccionamiento: >=3 pagos del mismo proveedor y aprobador en 7 días, cada uno entre 90% y 100% del límite
    p["cerca_limite"] = (p["valor"] >= 0.9 * p["limite_aprobacion"]) & (p["valor"] <= p["limite_aprobacion"])
    p["semana"] = p["fecha_aprobacion"].dt.to_period("W")
    grupos = p[p["cerca_limite"]].groupby(["id_proveedor", "usuario_aprueba", "semana"])["id_pago"].transform("count")
    frac_ids = p[p["cerca_limite"]].loc[grupos >= 3, "id_pago"]
    agregar(pagos["id_pago"].isin(frac_ids), "Posible fraccionamiento", "3 o más pagos cercanos al límite en una semana")
    # Proveedor con cuenta de empleado
    prov_emp = prov.merge(emp, on="cuenta_bancaria", suffixes=("", "_emp"))["id_proveedor"]
    agregar(pagos["id_proveedor"].isin(prov_emp), "Proveedor-empleado", "Cuenta bancaria compartida con un empleado")
    # Proveedor nuevo con pago alto
    p2 = pagos.merge(prov[["id_proveedor", "fecha_creacion"]], on="id_proveedor")
    nuevo = ((p2["fecha_pago"] - p2["fecha_creacion"]).dt.days < 30) & (p2["valor"] > 50_000_000)
    agregar(pagos["id_pago"].isin(p2.loc[nuevo, "id_pago"]), "Proveedor nuevo con pago alto",
            "Menos de 30 días desde la creación y valor > 50 M")
    # Montos redondos: proveedores con más del 50% de pagos múltiplos de 1 M
    redondo = pagos["valor"] % 1_000_000 == 0
    tasa = redondo.groupby(pagos["id_proveedor"]).mean()
    sospechosos = tasa[(tasa > 0.5) & (pagos.groupby("id_proveedor").size() >= 5)].index
    agregar(redondo & pagos["id_proveedor"].isin(sospechosos), "Montos redondos",
            "Proveedor con mayoría de pagos múltiplos de 1 M")
    # Atípicos por proveedor: z robusto > 3.5 sobre log10(valor) (los montos son asimétricos)
    logv = np.log10(pagos["valor"])
    med = logv.groupby(pagos["id_proveedor"]).transform("median")
    mad = logv.groupby(pagos["id_proveedor"]).transform(lambda x: np.median(np.abs(x - np.median(x))))
    z = 0.6745 * (logv - med) / mad.replace(0, np.nan)
    agregar((z > 3.5) & (pagos.groupby("id_proveedor")["valor"].transform("size") >= 8),
            "Valor atípico", "z robusto > 3.5 (escala log) frente al historial del proveedor")
    # Benford por usuario registrador. Con muestras de 100-300 registros la MAD tiene mucho ruido,
    # por eso se exige además significancia (p < 0.001) y solo se alertan los dígitos sobrerrepresentados.
    primer_digito = pagos["valor"].astype(str).str[0].astype(int)
    for usuario, grupo in pagos.groupby("usuario_registra"):
        if len(grupo) >= 100:
            tabla, p_valor, m = benford(grupo["valor"])
            if m > 0.015 and p_valor < 0.001:
                exceso = tabla.loc[tabla["diferencia"] > 0.02, "digito"]
                agregar((pagos["usuario_registra"] == usuario) & primer_digito.isin(exceso), "Benford por usuario",
                        f"Usuario {usuario}: MAD {m:.3f} ({interpretar_mad(m)}), p={p_valor:.1e}")
    pagos.drop(columns="_fact_norm", inplace=True)
    return pd.concat(alertas, ignore_index=True)


def isolation_forest(pagos, prov, contaminacion=0.02) -> pd.DataFrame:
    df = pagos.merge(prov[["id_proveedor", "fecha_creacion"]], on="id_proveedor")
    med = df.groupby("id_proveedor")["valor"].transform("median")
    X = pd.DataFrame({
        "log_valor": np.log10(df["valor"]),
        "ratio_vs_mediana_proveedor": df["valor"] / med,
        "dias_registro_a_pago": (df["fecha_pago"] - df["fecha_registro"]).dt.days,
        "dias_aprobacion_a_pago": (df["fecha_pago"] - df["fecha_aprobacion"]).dt.days,
        "dia_semana": df["fecha_pago"].dt.weekday,
        "antiguedad_proveedor_dias": (df["fecha_pago"] - df["fecha_creacion"]).dt.days,
        "mismo_usuario": (df["usuario_registra"] == df["usuario_aprueba"]).astype(int),
    })
    modelo = IsolationForest(n_estimators=300, contamination=contaminacion, random_state=42)
    modelo.fit(X)
    return pd.DataFrame({"id_pago": df["id_pago"], "if_puntaje": -modelo.score_samples(X),
                         "if_anomalo": (modelo.predict(X) == -1).astype(int)})


def evaluar(alertas: pd.DataFrame, puntajes: pd.DataFrame) -> None:
    clave_path = RAIZ / "soluciones" / "clave_anomalias_pagos.csv"
    if not clave_path.exists():
        print("No se encontró la clave de anomalías (solo disponible en el repositorio docente).")
        return
    clave = pd.read_csv(clave_path)
    verdaderos = set(clave["id_pago"])
    reglas = set(alertas["id_pago"])
    iforest = set(puntajes.loc[puntajes["if_anomalo"] == 1, "id_pago"])
    for nombre, pred in [("Reglas + Benford", reglas), ("Isolation Forest", iforest), ("Unión", reglas | iforest)]:
        tp = len(pred & verdaderos)
        print(f"{nombre:18s} alertas={len(pred):5d}  precisión={tp / max(len(pred), 1):.2f}  "
              f"exhaustividad={tp / len(verdaderos):.2f}")
    cobertura = clave.assign(detectado=clave["id_pago"].isin(reglas | iforest)).groupby("codigo")["detectado"].mean()
    print("\nExhaustividad por tipo de anomalía inyectada:\n", cobertura.round(2).to_string())


def main(evaluar_clave: bool) -> None:
    SALIDA.mkdir(parents=True, exist_ok=True)
    pagos, prov, emp, limites, festivos = cargar()
    tabla, p, mad = benford(pagos["valor"])
    print(f"Benford (todos los pagos): chi2 p-valor={p:.4f}  MAD={mad:.4f} -> {interpretar_mad(mad)}")
    tabla.to_csv(SALIDA / "benford_resumen.csv", index=False)

    alertas = pruebas(pagos, prov, emp, limites, festivos)
    alertas.to_csv(SALIDA / "alertas_pagos.csv", index=False)
    print("\nAlertas por prueba:\n", alertas["prueba"].value_counts().to_string())

    puntajes = isolation_forest(pagos, prov)
    n_reglas = alertas.groupby("id_pago").size().rename("n_alertas_reglas")
    puntajes = puntajes.merge(n_reglas, on="id_pago", how="left").fillna({"n_alertas_reglas": 0})
    puntajes["n_alertas_reglas"] = puntajes["n_alertas_reglas"].astype(int)
    puntajes.to_csv(SALIDA / "puntaje_pagos.csv", index=False)
    print(f"\nIsolation Forest: {puntajes['if_anomalo'].sum()} pagos marcados como anómalos")
    if evaluar_clave:
        print()
        evaluar(alertas, puntajes)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--evaluar", action="store_true", help="compara contra la clave de anomalías (docente)")
    main(ap.parse_args().evaluar)
