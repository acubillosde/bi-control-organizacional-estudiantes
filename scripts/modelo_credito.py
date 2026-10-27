"""Analítica predictiva y prescriptiva sobre la cartera agropecuaria de COAGUA (datos sintéticos).

1. Predictiva: regresión logística que estima la probabilidad de incumplimiento a 12 meses
   con variables disponibles al momento del desembolso (sin fuga de información: no usa dias_mora).
2. Prescriptiva: regla de decisión que asigna una acción de control según probabilidad y exposición.

Uso:
    python scripts/modelo_credito.py
Salida:
    datos/resultados/creditos_puntaje.csv  (para cargar en Power BI)
"""

from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

RAIZ = Path(__file__).resolve().parents[1]
NUMERICAS = ["monto_desembolsado", "tasa_ea", "plazo_meses", "score_buro", "antiguedad_cliente_anios"]
CATEGORICAS = ["linea", "garantia", "municipio", "id_asesor"]


def accion(prob: float, saldo: float) -> str:
    """Regla prescriptiva ilustrativa (umbrales definidos por el comité de riesgos ficticio)."""
    if prob >= 0.5 and saldo >= 50_000_000:
        return "Visita de campo y revisión de garantía"
    if prob >= 0.5:
        return "Gestión de cobro preventiva"
    if prob >= 0.25:
        return "Seguimiento mensual"
    return "Monitoreo estándar"


def main() -> None:
    cr = pd.read_csv(RAIZ / "datos" / "integrador" / "creditos.csv")
    X, y = cr[NUMERICAS + CATEGORICAS], cr["incumplimiento_12m"]
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    modelo = Pipeline([
        ("prep", ColumnTransformer([("num", StandardScaler(), NUMERICAS),
                                    ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAS)])),
        ("clf", LogisticRegression(max_iter=1000)),
    ])
    modelo.fit(X_tr, y_tr)
    auc = roc_auc_score(y_te, modelo.predict_proba(X_te)[:, 1])
    print(f"Tasa de incumplimiento: {y.mean():.1%}  |  AUC en prueba: {auc:.3f}")

    cr["prob_incumplimiento"] = modelo.predict_proba(X)[:, 1].round(4)
    cr["perdida_esperada_simple"] = (cr["prob_incumplimiento"] * cr["saldo_capital"]).round(0)
    cr["accion_recomendada"] = [accion(p, s) for p, s in zip(cr["prob_incumplimiento"], cr["saldo_capital"])]
    salida = RAIZ / "datos" / "resultados"
    salida.mkdir(parents=True, exist_ok=True)
    cr[["id_credito", "prob_incumplimiento", "perdida_esperada_simple", "accion_recomendada"]].to_csv(
        salida / "creditos_puntaje.csv", index=False)
    print(cr["accion_recomendada"].value_counts().to_string())
    tasa_asesor = cr.groupby("id_asesor")["incumplimiento_12m"].mean().sort_values(ascending=False)
    print("\nAsesores con mayor tasa de incumplimiento:\n", tasa_asesor.head(3).round(3).to_string())


if __name__ == "__main__":
    main()
