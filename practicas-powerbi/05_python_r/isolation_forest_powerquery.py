# Script para el paso "Ejecutar script de Python" de Power Query (Transformar > Ejecutar script de Python).
# Power BI entrega la tabla actual en la variable `dataset` (pandas DataFrame).
# Partir de la consulta fPagos (ver 01_power_query/consultas.m). Requiere pandas y scikit-learn.
# Power BI devuelve como tablas todos los DataFrame definidos; seleccione `resultado`.
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest

df = dataset.copy()
for c in ["fecha_registro", "fecha_aprobacion", "fecha_pago"]:
    df[c] = pd.to_datetime(df[c])

mediana_proveedor = df.groupby("id_proveedor")["valor"].transform("median")
X = pd.DataFrame({
    "log_valor": np.log10(df["valor"].astype(float)),
    "ratio_vs_mediana_proveedor": df["valor"] / mediana_proveedor,
    "dias_registro_a_pago": (df["fecha_pago"] - df["fecha_registro"]).dt.days,
    "dias_aprobacion_a_pago": (df["fecha_pago"] - df["fecha_aprobacion"]).dt.days,
    "dia_semana": df["fecha_pago"].dt.weekday,
    "mismo_usuario": (df["usuario_registra"] == df["usuario_aprueba"]).astype(int),
})

modelo = IsolationForest(n_estimators=300, contamination=0.02, random_state=42).fit(X)
resultado = pd.DataFrame({
    "id_pago": df["id_pago"],
    "if_puntaje": -modelo.score_samples(X),
    "if_anomalo": (modelo.predict(X) == -1).astype(int),
})
