# Actividades · Unidad 4

## Ejercicio de analítica forense (S3, B1, en equipo)
Con la tabla `benford_resumen.csv` y una muestra impresa de 30 pagos:
1. ¿Los pagos totales se ajustan a Benford? Interprete la MAD y el p-valor. ¿Por qué pueden contradecirse?
2. Identifique en la muestra: un duplicado aproximado, un pago en día no hábil y un caso de segregación de funciones.
3. Si solo puede revisar 25 pagos, ¿usaría muestreo estadístico o dirigido? Justifique con la NIA 530.

## L3 · Laboratorio en clase: alertas e Isolation Forest (S3, en equipo, 2%)
1. Ejecute (o use los ya generados) `scripts/deteccion_anomalias.py`.
2. Cargue `fAlertas` y `fPuntajePagos` y relaciónelos con `fPagos`.
3. Cree una página con la matriz prueba × centro de costo, la dispersión puntaje de Isolation Forest vs. valor, y una tabla de los **10 pagos de prioridad alta** (alertados por las reglas **y** por el modelo).
4. Para 3 de esos pagos, redacte en una línea qué haría el auditor (procedimiento, evidencia que solicitaría y responsable).

---

## <a id="t4"></a>T4 · Benford, duplicados y reglas de control en Power BI (semana 5, 3 h, en equipo, 2%)

**RA:** RA2 · **Fecha límite:** jueves de la semana 5

Este taller se hace **antes** del S3 (aula invertida): llega al sábado con la mecánica dominada y el S3 se dedica a interpretar.

1. Implemente en DAX (carpetas 3 y 4 de `medidas.dax`): Benford con MAD y conformidad, pagos en grupos duplicados, valor potencialmente duplicado, pagos sobre el límite y pagos en día no hábil.
2. Construya la gráfica Benford (observado vs. esperado) con un segmentador por `usuario_registra`. ¿Qué usuario se desvía? ¿Con cuántos registros? ¿Es concluyente?
3. Diseñe y documente **una regla propia** que no esté en la práctica, por ejemplo: pagos del mismo valor a proveedores distintos el mismo día, o proveedores cuyo único aprobador es siempre la misma persona.
4. Compare sus resultados con `alertas_pagos.csv`. ¿Coinciden? Explique las diferencias.

**Entregable:** `.pbix` + tabla de alertas (prueba, N° de pagos, valor, interpretación).

---

## <a id="pb"></a>PB · Profundización B: segundo dataset de otra industria (semana 5, 2.5 h, en equipo, 1.5%)

**RA:** RA2, RA3 · **Datos:** `datos/profundizacion/gastos_viaje_retail.csv`: gastos de viaje de "Almacenes Mirador", cadena de retail ficticia · **Fecha límite:** jueves de la semana 5

Esta actividad **no repite** el T4. Aplica la lógica de las pruebas a otra industria y a otro proceso.
1. Proponga 4 pruebas analíticas adecuadas para gastos de viaje (no copie las de pagos: piense en topes por categoría, recibos repetidos, fines de semana, valores justo bajo el tope).
2. Impleméntelas en una página de Power BI.
3. Escriba 1 página de hallazgos: ¿qué pruebas se transfieren entre industrias y cuáles no? ¿Qué norma o política motivaría cada control en una sociedad comercial (ver mapa normativo)?

---

## <a id="pc"></a>PC · Profundización C: modelo de ML consumido desde Power BI (semana 6, 4 h, en equipo, 1.5%)

**RA:** RA3 · **Fecha límite:** sábado de la semana 6

Esta actividad **no repite** el L3: allí se consumieron puntajes precalculados; aquí el equipo **entrena, evalúa y explica** un modelo.
1. **Elegir una opción.**
   - *Python:* Isolation Forest dentro de Power Query ([script](../practicas-powerbi/05_python_r/isolation_forest_powerquery.py)), probando 3 valores de `contamination` (0.01, 0.02, 0.05).
   - *R o Python:* regresión logística de incumplimiento ([script R](../practicas-powerbi/05_python_r/regresion_logistica_powerquery.R) o `scripts/modelo_credito.py`).
2. **Evaluar.** Para Isolation Forest, ¿cuántas alertas genera cada nivel de contaminación y cuántas coinciden con las reglas? Para la regresión logística, reporte el AUC y la tasa de incumplimiento por decil de probabilidad.
3. **Prescribir.** Proponga una regla de acción (qué hacer según el puntaje y la exposición) y estime cuántos casos tendría que revisar el equipo de auditoría cada mes.
4. **Límites.** Explique en 5 líneas un riesgo del modelo (sesgo, fuga de información, deriva, explicabilidad) y cómo lo mitigaría.

**Entregable:** `.pbix` (o capturas, si trabaja desde Mac con la opción A) + nota metodológica de 1 página.
