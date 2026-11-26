"""Contraste en Python de las verificaciones del caso Tiendas Aurora (V01 a V17).

Power BI y Python son dos herramientas independientes: si las dos dan el mismo valor, la cifra es confiable;
si no coinciden, una de las dos tiene un error de filtro, de relación o de tipo de dato, y hay que encontrarlo.

Uso, desde la carpeta del repositorio:
    python casos/verificacion_aurora.py          # todas las verificaciones
    python casos/verificacion_aurora.py V07 V13  # solo las que indique
Requiere pandas (pip install pandas). Lee datos/demo_aurora/. No modifica nada.
Este archivo lo genera scripts/verificaciones_aurora.py en el repositorio del docente.
"""
import math
import sys
from pathlib import Path

import pandas as pd

D = Path(__file__).resolve().parents[1] / "datos" / "demo_aurora"
pagos = pd.read_csv(D / "pagos.csv", parse_dates=["fecha_factura", "fecha_registro", "fecha_aprobacion", "fecha_pago"])
ventas = pd.read_csv(D / "ventas_diarias.csv", parse_dates=["fecha"])
prov = pd.read_csv(D / "proveedores.csv", dtype=str)
emp = pd.read_csv(D / "empleados.csv", dtype=str)
tiendas = pd.read_csv(D / "tiendas.csv")
limites = pd.read_csv(D / "limites_aprobacion.csv")
tablas = {"tiendas": tiendas, "empleados": emp, "limites_aprobacion": limites, "proveedores": prov, "pagos": pagos, "ventas_diarias": ventas}

# Columnas de control (las mismas de V03 y V07 en Power Query y en DAX)
pagos["factura_normalizada"] = pagos.numero_factura.str.replace(r"\D", "", regex=True).str.lstrip("0")
pagos["clave"] = pagos.id_proveedor + "|" + pagos.factura_normalizada + "|" + pagos.valor.astype(str)
pagos["es_duplicado"] = (pagos.id_pago > pagos.groupby("clave").id_pago.transform("min")).astype(int)


def n0(x):
    return f"{x:,.0f}".replace(",", ".")


def n1(x):
    return f"{x:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".")


def n2(x):
    return f"{x:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def v01():
    """Cargue las seis tablas y cuente las filas"""
    for nombre, df in tablas.items():
        print(f"{nombre}: {len(df)} filas")


def v02():
    """Limpie el maestro sin destruir el original"""
    limpia = prov.ciudad.str.lower().str.replace("medellin", "medellín").str.replace("itagui", "itagüí").str.title()
    nit_digitos = prov.nit.str.replace(r"\D", "", regex=True)
    print("Filas de proveedores:", len(prov))
    print("Ciudades distintas antes:", prov.ciudad.nunique())
    print("Ciudades distintas después:", limpia.nunique())
    print("NIT distintos (solo dígitos):", nit_digitos.nunique())


def v03():
    """Construya tres columnas de control sobre pagos"""
    mismo_usuario = (pagos.usuario_registra == pagos.usuario_aprueba).astype(int)
    dia_no_habil = (pagos.fecha_aprobacion.dt.dayofweek >= 5).astype(int)   # lunes = 0, sábado = 5
    factura_norm = pagos.numero_factura.str.replace(r"\D", "", regex=True).str.lstrip("0")
    print("Suma de mismo_usuario:", mismo_usuario.sum())
    print("Suma de aprobacion_dia_no_habil:", dia_no_habil.sum())
    print("factura_normalizada de FV-2269:", factura_norm[pagos.numero_factura == "FV-2269"].iloc[0])


def v04():
    """Cree el calendario y encuentre los días sin ventas"""
    junio = pd.date_range("2025-06-01", "2025-06-30")
    vendio = set(ventas[(ventas.id_tienda == "T07") & (ventas.fecha.dt.month == 6)].fecha)
    sin_ventas = [d for d in junio if d not in vendio]
    print("Días sin ventas de T07 en junio:", len(sin_ventas))
    print("Filas esperadas (12 tiendas x 365 días):", 12 * 365, "· filas reales:", len(ventas))


def v05():
    """Arme la estrella de ventas y pida «ventas por cliente»"""
    por_tienda = ventas.groupby("id_tienda").ventas.sum().sort_values(ascending=False)
    nombre = tiendas.set_index("id_tienda").nombre_tienda[por_tienda.index[0]]
    print("Ventas totales 2025: $" + n0(ventas.ventas.sum()), "=", n1(ventas.ventas.sum() / 1e6), "millones")
    print("Tienda con más ventas:", por_tienda.index[0], nombre, n1(por_tienda.iloc[0] / 1e6), "millones")
    print("Filas de ventas:", len(ventas))


def v06():
    """Calcule un KPI, un KRI y un KCI"""
    print("KPI · días de factura a pago:", n1((pagos.fecha_pago - pagos.fecha_factura).dt.days.mean()))
    print("KRI · devoluciones sobre ventas:", n2(ventas.devoluciones.sum() / ventas.ventas.sum() * 100) + "%")
    print("KCI · pagos con el mismo usuario:", n2((pagos.usuario_registra == pagos.usuario_aprueba).mean() * 100) + "%")


def v07():
    """Reproduzca los tres números de marzo"""
    marzo_aprobacion = pagos[pagos.fecha_aprobacion.dt.to_period("M") == "2025-03"]
    marzo_pago = pagos[pagos.fecha_pago.dt.to_period("M") == "2025-03"]
    sin_duplicados = marzo_aprobacion[marzo_aprobacion.es_duplicado == 0]
    print("Por fecha de aprobación:", n1(marzo_aprobacion.valor.sum() / 1e6), "millones")
    print("Por fecha de pago:", n1(marzo_pago.valor.sum() / 1e6), "millones")
    print("Aprobación sin duplicados:", n1(sin_duplicados.valor.sum() / 1e6), "millones")
    print("Duplicados en marzo:", len(marzo_aprobacion) - len(sin_duplicados))


def v08():
    """Mida la calidad del maestro con reglas en DAX"""
    lista = ["Medellín", "Envigado", "Itagüí", "Bello", "Sabaneta"]
    nit_digitos = prov.nit.str.replace(r"\D", "", regex=True)
    print("Ciudades fuera de lista:", (~prov.ciudad.isin(lista)).sum(), "de", len(prov))   # isin distingue mayúsculas y tildes
    print("NIT repetidos:", len(prov) - nit_digitos.nunique())
    print("Proveedores con el NIT repetido:", list(prov[nit_digitos.duplicated(keep=False)].id_proveedor))


def v09():
    """Ponga los umbrales de la matriz en un semáforo"""
    dias = (pagos.fecha_pago - pagos.fecha_factura).dt.days.mean()
    dev = ventas.devoluciones.sum() / ventas.ventas.sum()
    sep = ventas[(ventas.id_tienda == "T03") & (ventas.fecha.dt.month == 9)]
    dev_t03 = sep.devoluciones.sum() / sep.ventas.sum()
    mismo = (pagos.usuario_registra == pagos.usuario_aprueba).mean()
    duplicados = pagos.es_duplicado.sum()
    semaforo = lambda rojo: "Rojo" if rojo else "Verde"
    print("Días de factura a pago:", n1(dias), "→", "Rojo" if dias > 20 else "Amarillo" if dias > 15 else "Verde")
    print("Devoluciones (todas las tiendas):", n2(dev * 100) + "%", "→", semaforo(dev > 0.02))
    print("Devoluciones de T03 en septiembre:", n2(dev_t03 * 100) + "%", "→", semaforo(dev_t03 > 0.02))
    print("Pagos con el mismo usuario:", n2(mismo * 100) + "%", "→", semaforo(mismo > 0))
    print("Pagos duplicados:", duplicados, "→", semaforo(duplicados > 0))


def v10():
    """Haga la torta y compárela con barras"""
    por_tienda = ventas.groupby("id_tienda").ventas.sum().sort_values(ascending=False)
    parte = por_tienda / por_tienda.sum() * 100
    print("Tienda con más ventas:", por_tienda.index[0])
    print("Participación de las dos primeras:", n1(parte.iloc[0]) + "% y " + n1(parte.iloc[1]) + "%")
    print("Diferencia entre las dos primeras:", n1((por_tienda.iloc[0] - por_tienda.iloc[1]) / 1e6), "millones")


def v11():
    """Resalte las devoluciones de T03 frente al resto"""
    ventas["mes"] = ventas.fecha.dt.month
    def pct(df):
        return df.groupby("mes")[["devoluciones", "ventas"]].sum().pipe(lambda g: g.devoluciones / g.ventas * 100)
    t03, resto = pct(ventas[ventas.id_tienda == "T03"]), pct(ventas[ventas.id_tienda != "T03"])
    print(pd.DataFrame({"T03 %": t03.round(2), "Resto %": resto.round(2)}))
    print("Mes del pico de T03:", t03.idxmax(), "·", n2(t03.max()) + "%", "· resto ese mes:", n2(resto[t03.idxmax()]) + "%")


def v12():
    """Haga un titular dinámico y póngalo a prueba"""
    ventas["mes"] = ventas.fecha.dt.month
    def pct(df, mes):
        g = df[df.mes == mes]
        return g.devoluciones.sum() / g.ventas.sum() * 100
    for mes, nombre in [(9, "septiembre"), (1, "enero")]:
        t03, resto = pct(ventas[ventas.id_tienda == "T03"], mes), pct(ventas[ventas.id_tienda != "T03"], mes)
        print(f"Titular en {nombre}: T03 devolvió {n1(t03)}% de sus ventas; el resto de tiendas, {n1(resto)}%")
        if t03 > 2:
            print(f"Titular mejorado en {nombre}: Alerta: T03 devolvió {n1(t03)}% de sus ventas, {round(t03 / resto)} veces el resto")


def v13():
    """Pruebe Benford sobre el valor de los pagos"""
    primer = pagos.valor.astype(str).str[0].astype(int)
    uno = lambda mascara: (primer[mascara] == 1).mean() * 100   # % de pagos del grupo cuyo valor empieza por 1
    print("Esperado para el dígito 1:", n1(math.log10(2) * 100) + "%")
    print("Todos los pagos:", n1((primer == 1).mean() * 100) + "%")
    print("Resto de usuarios:", n1(uno(pagos.usuario_registra != "aur006")) + "%")
    print("aur006:", n1(uno(pagos.usuario_registra == "aur006")) + "%", "·", (pagos.usuario_registra == "aur006").sum(), "pagos")


def v14():
    """Cuente duplicados exactos y aproximados"""
    exactos = pagos.duplicated(["id_proveedor", "numero_factura", "valor"]).sum()
    normalizados = pagos.es_duplicado.sum()
    print("Duplicados exactos:", exactos)
    print("Duplicados con la factura normalizada:", normalizados)
    print("Duplicados aproximados:", normalizados - exactos)


def v15():
    """Busque pagos pegados al límite de aprobación"""
    cerca = pagos[(pagos.valor >= 0.95 * 8_000_000) & (pagos.valor < 8_000_000)]
    print("Pagos entre 95% y 100% del límite (año):", len(cerca))
    print(cerca.id_proveedor.value_counts().head(3))
    ago = cerca[(cerca.id_proveedor == "P017") & (cerca.fecha_aprobacion.dt.month == 8)]
    print("P017 en agosto:", len(ago), "pagos entre", n2(ago.valor.min() / 1e6), "y", n2(ago.valor.max() / 1e6), "millones")


def v16():
    """Mida el valor y la concentración de las dos señales"""
    mismo = pagos[pagos.usuario_registra == pagos.usuario_aprueba]
    finde = pagos[pagos.fecha_aprobacion.dt.dayofweek >= 5]
    print("Pagos del mismo usuario:", len(mismo), "·", n1(mismo.valor.sum() / 1e6), "millones · usuarios:", list(mismo.usuario_registra.unique()))
    print("Pagos en día no hábil:", len(finde), "· sábados:", (finde.fecha_aprobacion.dt.dayofweek == 5).sum(), "· domingos:", (finde.fecha_aprobacion.dt.dayofweek == 6).sum())
    print("Valor de los pagos de fin de semana:", n1(finde.valor.sum() / 1e6), "millones")


def v17():
    """Cruce cuentas bancarias de proveedores y de nómina"""
    coinciden = prov[prov.cuenta_bancaria.isin(emp.cuenta_nomina)]
    print("Proveedores con cuenta de nómina:", len(coinciden), list(coinciden.id_proveedor))
    pr = pagos[pagos.id_proveedor.isin(coinciden.id_proveedor)]
    print("Pagos a ese proveedor:", len(pr), "·", n1(pr.valor.sum() / 1e6), "millones")
    print("Proveedor creado:", coinciden.fecha_creacion.iloc[0], "· primer pago aprobado:", pr.fecha_aprobacion.min().date(), "· último:", pr.fecha_aprobacion.max().date())
    print("Quién registró los pagos:", list(pr.usuario_registra.unique()), "· valor máximo:", n1(pr.valor.max() / 1e6), "millones")


VERIFICACIONES = {"V01": v01, "V02": v02, "V03": v03, "V04": v04, "V05": v05, "V06": v06, "V07": v07, "V08": v08, "V09": v09, "V10": v10, "V11": v11, "V12": v12, "V13": v13, "V14": v14, "V15": v15, "V16": v16, "V17": v17}


if __name__ == "__main__":
    pedidas = [a.upper() for a in sys.argv[1:]] or list(VERIFICACIONES)
    for clave in pedidas:
        if clave not in VERIFICACIONES:
            print(f"{clave}: no existe (use V01 a V17)")
            continue
        print(f"\n=== {clave} · {VERIFICACIONES[clave].__doc__} ===")
        VERIFICACIONES[clave]()
