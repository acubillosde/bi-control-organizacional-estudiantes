# Unidad 4 · Analítica para el aseguramiento *(unidad agregada)*

**Justificación:** las temáticas oficiales (T1–T3) no cubren de forma explícita la detección de anomalías (RA2) ni la analítica descriptiva, predictiva y prescriptiva aplicada a la auditoría y a la gestión de riesgos (RA3). Esta unidad cierra esa brecha.
**Resultados de aprendizaje:** RA2, RA3 · **Competencias:** C1, C2, C3
**Carga:** 5 h presenciales (S3) + 16.5 h independientes = 21.5 h

## Objetivos
1. Relaciona los componentes del control interno (COSO 2013) y del proceso de gestión del riesgo (ISO 31000) con las pruebas analíticas que los soportan.
2. Aplica pruebas de analítica forense: Ley de Benford, duplicados, pruebas de razonabilidad, fraccionamiento, segregación de funciones y muestreo dirigido.
3. Aplica y evalúa un modelo no supervisado (Isolation Forest) y uno supervisado (regresión logística), y explica sus límites.
4. Traduce probabilidades y alertas en acciones priorizadas (analítica prescriptiva basada en reglas).
5. Identifica el marco normativo colombiano que motiva cada control.

## Contenidos
1. Control interno y gestión de riesgos: COSO 2013, ISO 31000, modelo de las tres líneas.
2. Auditoría continua y monitoreo continuo: arquitectura, frecuencia, umbrales y escalamiento (guía del IIA, 3.ª ed., 2025).
3. Analítica forense: Benford (chi-cuadrado y MAD), duplicados exactos y aproximados, pruebas de razonabilidad, muestreo (NIA 530).
4. Analítica descriptiva, predictiva y prescriptiva: Isolation Forest, regresión logística y reglas de decisión. Ciclo de vida de un modelo en producción: aseguramiento de calidad y monitoreo (CRISP-ML(Q)).
5. Mapa normativo colombiano aplicable.
6. Caso: Watson (capacidades y límites de la IA).

## Materiales
| Material | Enlace |
|---|---|
| Lecturas y mapa normativo | [lecturas.md](lecturas.md) |
| Actividades (L3, T4, PB, PC) | [actividades.md](actividades.md) |
| Caso | [Watson](../casos/caso_watson.md) |
| Prácticas | [03 DAX (Benford, alertas)](../practicas-powerbi/03_dax/README.md) · [05 Python/R](../practicas-powerbi/05_python_r/README.md) |
| Scripts | [`deteccion_anomalias.py`](../scripts/deteccion_anomalias.py) · [`modelo_credito.py`](../scripts/modelo_credito.py) |
| Quiz de cierre | [Quiz U4](../evaluacion/quizzes/quiz_u4.md) |
