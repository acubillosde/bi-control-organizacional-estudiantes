# Ruta semanal de trabajo independiente (72 h)

## Supuestos

| Supuesto | Valor |
|---|---|
| Ventana del curso | 7 semanas. Las semanas van de domingo a sábado |
| Sábados presenciales | S1 al final de la semana 1, S2 al final de la semana 3, S3 al final de la semana 5 (14 días entre sábados) |
| Fechas de ejemplo | S1 = 20 feb 2027 · S2 = 6 mar 2027 · S3 = 20 mar 2027 · Entrega final = 3 abr 2027. **El docente debe reemplazarlas por las fechas reales** |
| Carga semanal | 8 h (sem. 1) · 12.75 y 11.25 h (sem. 2 y 3) · 12 h (sem. 4–5) · 8 h (sem. 6–7) |
| Hora de cierre de entregas | 23:59 (hora de Colombia), en el aula virtual o en el canal que indique el docente |
| Festivos en la ventana de ejemplo | 22 mar 2027 (San José), 25 y 26 mar 2027 (Jueves y Viernes Santo), en la semana 6, que tiene carga reducida |

## Criterio para estimar las horas de lectura

Las horas de lectura se calculan como `páginas ÷ velocidad`, redondeando a la media hora más cercana. La velocidad incluye la toma de notas.

| Complejidad | Ejemplos | Velocidad |
|---|---|---:|
| Alta | Artículo académico en inglés con marco teórico denso | 8 p/h |
| Media-alta | Artículo académico aplicado o caso de enseñanza en inglés | 10 p/h |
| Media | Capítulo de libro o informe técnico en español | 12 p/h |
| Baja | Artículo de divulgación (HBR), blog técnico o resumen ejecutivo | 15 p/h |

**Restricción:** las lecturas obligatorias no superan el 30% de las horas independientes de cada tramo.

| Tramo | Horas | Tope de lectura (30%) | Lectura asignada | % |
|---|---:|---:|---:|---:|
| Pre-S1 | 8 | 2.4 | 2.0 | 25.0% |
| S1→S2 | 24 | 7.2 | 7.0 | 29.2% |
| S2→S3 | 24 | 7.2 | 6.5 | 27.1% |
| Post-S3 | 16 | 4.8 | 2.0 | 12.5% |

> Cuando una fuente no tiene número de páginas verificado, la estimación se marca **(est.)** y queda en la lista de pendientes de verificación del [CHANGELOG](../CHANGELOG.md).

## Ruta

Leyenda: **RA** = resultado de aprendizaje · **Peso** = porcentaje de la nota final (ver [criterios](../evaluacion/criterios_calificacion.md)).

### Semana 1 · Antes del Sábado 1 (8 h) · 14–19 feb

| ID | Actividad | Horas | RA | Producto | Fecha límite | Criterio de evaluación | Peso |
|---|---|---:|---|---|---|---|---:|
| P1 | [Quiz diagnóstico](../evaluacion/quizzes/quiz_diagnostico.md) | 0.5 | RA1–RA3 | Quiz respondido | Jue 18 feb | Completitud. Es formativo: orienta el énfasis del S1 | 0% |
| P2 | Lectura para la ficha: **un** artículo a elección de la lista pre-S1 de [lecturas](../lecturas/lecturas.md#pre-s1) | 2.0 | RA1 | Notas de lectura | Vie 19 feb | Se evalúa en P3 | — |
| P3 | Ficha de revisión documental (formato institucional "FrmFichaRevisiónDocumental") | 2.0 | RA1 | Ficha (máx. 3 páginas) | Vie 19 feb | [Rúbrica de ficha de lectura](../evaluacion/rubricas.md#r1-ficha-de-revisión-documental) | 10% |
| T0 | [Taller T0](../unidad-1/actividades.md#t0): instalación de Power BI y exploración de `pagos.csv` en Python (pandas) | 3.5 | RA1 | Lista de verificación del entorno + 5 respuestas con evidencia | Vie 19 feb | [Rúbrica de taller autónomo](../evaluacion/rubricas.md#r3-taller-autónomo) | 1% |
| | **Subtotal** | **8.0** | | | | | |

### Semana 2 · Después del Sábado 1 (12.75 h) · 21–27 feb

| ID | Actividad | Horas | RA | Producto | Fecha límite | Criterio de evaluación | Peso |
|---|---|---:|---|---|---|---|---:|
| Q1 | [Quiz U1](../evaluacion/quizzes/quiz_u1.md) | 0.5 | RA1 | Quiz | Mié 24 feb | Respuestas correctas | 3.75% |
| L1 | Lectura: Schafheitle et al. (2020), 33 p, complejidad alta | 4.0 | RA2 | Mapa del marco de datificación aplicado a una organización conocida (1 p) | Sáb 27 feb | Preguntas 1–3 del Quiz U2 y discusión del S2 | (Q2) |
| T1 | [Taller T1](../unidad-1/actividades.md#t1): ETL completo y documentado en Power Query (práctica 01), con las reglas de calidad del L1 y controles propios | 5.5 | RA1 | Archivo `.pbix` + documento de pasos aplicados | Sáb 27 feb | [Rúbrica de taller autónomo](../evaluacion/rubricas.md#r3-taller-autónomo) | 2% |
| PA | [Profundización A](../unidad-2/actividades.md#pa): [diagnóstico de madurez de BI con evidencia](../unidad-1/actividad_madurez_bi/README.md) (individual) | 2.75 | RA1, RA2 | Diagnóstico (PDF, máx. 3 p) + formulario anónimo | Sáb 27 feb | [Rúbrica R6](../evaluacion/rubricas.md#r6-diagnóstico-de-madurez-de-bi-con-evidencia) | 2% |
| | **Subtotal** | **12.75** | | | | | |

### Semana 3 · Antes del Sábado 2 (11.25 h) · 28 feb – 5 mar

| ID | Actividad | Horas | RA | Producto | Fecha límite | Criterio de evaluación | Peso |
|---|---|---:|---|---|---|---|---:|
| L2 | Lectura: Pauwels et al. (2009), 15 p, media-alta | 1.5 | RA2 | Notas: cinco etapas del desarrollo de un dashboard | Vie 5 mar | Preguntas 4–5 del Quiz U2 | (Q2) |
| L3 | Lectura: caso Ramírez-Angulo y Chaparro-Guevara (2020), 16 p, media-alta | 1.5 | RA2 | Respuestas a la [guía del caso](../casos/caso_centro_comercial.md) | Vie 5 mar | Discusión del S2 y exposición de caso | (EX) |
| T2 | [Taller T2](../unidad-2/actividades.md#t2): modelo estrella y 10 medidas DAX de control | 3.0 | RA1, RA2 | `.pbix` + diccionario de medidas | Vie 5 mar | [Rúbrica de taller autónomo](../evaluacion/rubricas.md#r3-taller-autónomo) | 2% |
| EX | Preparación de la exposición o réplica asignada en el S1 | 1.75 | RA3 | Presentación (máx. 6 diapositivas) | Día de la exposición (S2 o S3) | [Rúbrica de exposición](../evaluacion/rubricas.md#r5-exposición-o-réplica-de-caso) | 10% |
| AV1 | [Avance 1 del caso integrador](../caso-integrador/avance_1.md): extracción, limpieza y modelo de datos | 3.5 | RA1 | `.pbix` + memoria técnica (3–5 p) | **Mié 3 mar** | [Rúbrica Avance 1](../caso-integrador/avance_1.md#rúbrica) | 7.5% |
| | **Subtotal** | **11.25** | | | | | |

> EX pasó a la semana 3 (siempre antes del S2) para equilibrar la carga después de mover el ETL al T1. Los equipos que exponen el caso Watson (S3) pueden trasladar las 1.75 h de EX a la semana 5 sin cambiar el total.

### Semana 4 · Después del Sábado 2 (12 h) · 7–13 mar

| ID | Actividad | Horas | RA | Producto | Fecha límite | Criterio de evaluación | Peso |
|---|---|---:|---|---|---|---|---:|
| Q2 | [Quiz U2](../evaluacion/quizzes/quiz_u2.md) | 0.5 | RA1, RA2 | Quiz | Mié 10 mar | Respuestas correctas | 3.75% |
| Q3 | [Quiz U3](../evaluacion/quizzes/quiz_u3.md) | 0.5 | RA3 | Quiz | Mié 10 mar | Respuestas correctas | 3.75% |
| L4 | Lectura: Davenport y Patil (2012), 7 p, baja | 0.5 | RA3 | Notas | Mié 10 mar | Preguntas del Quiz U3 | (Q3) |
| L5 | Lectura: caso Ritz-Carlton (Sasser y Jones, 1999), ≈15 p (est.), media-alta | 1.5 | RA3 | Notas | Mié 10 mar | Preguntas del Quiz U3 | (Q3) |
| T3 | [Taller T3](../unidad-3/actividades.md#t3): rediseño de un tablero y guion de storytelling | 3.0 | RA2, RA3 | `.pbix` + guion (1 p) | Vie 12 mar | [Rúbrica de taller autónomo](../evaluacion/rubricas.md#r3-taller-autónomo) | 2% |
| AV2 | [Avance 2 del caso integrador](../caso-integrador/avance_2.md): dashboard de control con KPIs y storytelling | 6.0 | RA2, RA3 | `.pbix` + nota ejecutiva (2 p) | **Sáb 13 mar** | [Rúbrica Avance 2](../caso-integrador/avance_2.md#rúbrica) | 7.5% |
| | **Subtotal** | **12.0** | | | | | |

### Semana 5 · Antes del Sábado 3 (12 h) · 14–19 mar

| ID | Actividad | Horas | RA | Producto | Fecha límite | Criterio de evaluación | Peso |
|---|---|---:|---|---|---|---|---:|
| L6 | Lectura propuesta: COSO (2013), *Internal Control – Integrated Framework, Executive Summary*, ≈10 p (est.), media | 1.0 | RA2 | Tabla: 5 componentes y su evidencia en datos | Jue 18 mar | Preguntas del Quiz U4 | (Q4) |
| L7 | Lectura: Auditool, *Métodos analíticos en la detección del fraude* (blog), ≈6 p (est.), baja | 0.5 | RA2 | Notas | Jue 18 mar | Preguntas del Quiz U4 | (Q4) |
| L8 | Lectura: The Royal Society (2017), resumen ejecutivo, ≈12 p (est.), media | 1.0 | RA3 | Notas | Jue 18 mar | Preguntas del Quiz U4 | (Q4) |
| L9 | Lectura: caso Watson (Shih, 2012), ≈20 p (est.), media-alta | 2.0 | RA3 | Respuestas a la [guía del caso](../casos/caso_watson.md) | Sáb 20 mar | Discusión del S3 y exposición de caso | (EX) |
| T4 | [Taller T4](../unidad-4/actividades.md#t4): Benford, duplicados y reglas de control en Power BI | 3.0 | RA2 | `.pbix` + tabla de alertas | Jue 18 mar | [Rúbrica de taller autónomo](../evaluacion/rubricas.md#r3-taller-autónomo) | 2% |
| PB | [Profundización B](../unidad-4/actividades.md#pb): segundo dataset de otra industria (gastos de viaje en retail) | 2.5 | RA2, RA3 | Hallazgos (1 p) + 1 página de Power BI | Jue 18 mar | [Rúbrica de profundización](../evaluacion/rubricas.md#r4-profundización-a-b-c) | 1.5% |
| SU | Preparación de la sustentación ante el comité de auditoría | 2.0 | RA3 | Presentación ejecutiva (máx. 8 diapositivas) | Sáb 20 mar (S3) | [Rúbrica de sustentación](../caso-integrador/entrega_final.md#rúbrica-de-sustentación) | 15% |
| | **Subtotal** | **12.0** | | | | | |

### Semana 6 · Después del Sábado 3 (8 h) · 21–27 mar

| ID | Actividad | Horas | RA | Producto | Fecha límite | Criterio de evaluación | Peso |
|---|---|---:|---|---|---|---|---:|
| Q4 | [Quiz U4](../evaluacion/quizzes/quiz_u4.md) | 0.5 | RA2, RA3 | Quiz | Mié 24 mar | Respuestas correctas | 3.75% |
| L10 | Lectura de cierre, a elegir: Lemus-Delgado y Pérez Navarro (2020), 22 p, media; o CILIP (2021), caps. 4–5 (est.) | 2.0 | RA3 | Párrafo citado en la sección "hoja de ruta" del informe final | Sáb 3 abr | Criterio "Hoja de ruta" de la rúbrica final | (EF) |
| PC | [Profundización C](../unidad-4/actividades.md#pc): modelo de ML (Python o R) consumido desde Power BI | 4.0 | RA3 | `.pbix` o capturas + nota metodológica (1 p) | Sáb 27 mar | [Rúbrica de profundización](../evaluacion/rubricas.md#r4-profundización-a-b-c) | 1.5% |
| EF-a | Entrega final, parte 1: incorporar la retroalimentación del comité al tablero | 1.5 | RA2 | Versión ajustada del `.pbix` | — | Se evalúa en EF | — |
| | **Subtotal** | **8.0** | | | | | |

### Semana 7 · Cierre (8 h) · 28 mar – 3 abr

| ID | Actividad | Horas | RA | Producto | Fecha límite | Criterio de evaluación | Peso |
|---|---|---:|---|---|---|---|---:|
| EF-b | [Entrega final](../caso-integrador/entrega_final.md): tablero con detección de anomalías + informe ejecutivo | 6.5 | RA1–RA3 | `.pbix` + informe ejecutivo (máx. 6 p) | **Sáb 3 abr** | [Rúbrica de entrega final](../caso-integrador/entrega_final.md#rúbrica-de-la-entrega-final) | 15% |
| CO | Coevaluación y autoevaluación del equipo | 1.5 | — | Formulario de coevaluación + reflexión individual (½ p) | Sáb 3 abr | Cumplimiento. Ajusta la nota individual de los componentes grupales | Factor |
| | **Subtotal** | **8.0** | | | | | |

## Resumen de control

| Tramo | Semanas | Horas | Verificación |
|---|---|---:|---|
| Pre-S1 | 1 | 8.0 | 0.5 + 2.0 + 2.0 + 3.5 |
| S1→S2 | 2–3 | 24.0 | 12.75 + 11.25 |
| S2→S3 | 4–5 | 24.0 | 12.0 + 12.0 |
| Post-S3 | 6–7 | 16.0 | 8.0 + 8.0 |
| **Total** | | **72.0** | |

Todas las actividades tienen un producto evaluable. Las lecturas se evalúan a través del quiz de la unidad, de la exposición de caso o de un criterio explícito de la entrega final, como se indica en cada fila. El script `scripts/control_calidad.py` recalcula estas sumas.
