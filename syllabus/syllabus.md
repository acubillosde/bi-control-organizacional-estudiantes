# Syllabus — Seminario de Interacción 7: Inteligencia de Negocios
### Inteligencia de Negocios para el Control Organizacional

> Fuente de verdad: `fuentes/syllabus_original.md` (transcripción del syllabus institucional). Este documento conserva sus competencias, resultados de aprendizaje, temáticas y sistema de evaluación, y agrega la Unidad 4 y el diseño operativo del curso. Las diferencias frente al original están en [`CHANGELOG.md`](../CHANGELOG.md).

## 1. Información general

| Campo | Valor | Fuente |
|---|---|---|
| Programa | Maestría en Control Organizacional | PDF oficial |
| Asignatura | Seminario de Interacción 7 – Inteligencia de Negocios | PDF oficial |
| Código de asignatura | No indicado en el syllabus oficial (pendiente de confirmar con la coordinación) | — |
| Prerrequisitos formales | No indicados. Requisitos de entrada: manejo de Excel (tablas dinámicas) y PowerPoint; computador portátil | PDF oficial |
| Créditos | 2 (48 h por crédito = 96 h) | PDF oficial |
| Horas presenciales | 24 (3 sábados de 8 h) | PDF oficial |
| Horas de trabajo autónomo | 72 | PDF oficial |
| Modalidad | Seminario-taller | PDF oficial |
| Docente | [Nombre y correo del docente a cargo] | Por definir |
| Herramienta de visualización | Power BI Desktop (gratuito). No se usa ninguna otra herramienta de visualización | Decisión de diseño |
| Canal de dudas | Issues del repositorio de estudiantes (ver [plan de seguimiento](../cronograma/plan_seguimiento.md)) | Decisión de diseño |

**Parámetros de carga:** `CREDITOS=2`, `HORAS_POR_CREDITO=48`, `HORAS_PRESENCIALES=24`, `HORAS_INDEPENDIENTES=72`.

## 2. Presentación

Las organizaciones toman hoy decisiones de control con más datos, más rápido y con mayores exigencias de supervisión. La inteligencia de negocios (BI) ya no es solo un sistema de reportes: es la infraestructura que permite a la administración, a la auditoría interna, a la revisoría fiscal y a los órganos de control **monitorear riesgos, detectar anomalías y verificar el cumplimiento** de manera continua.

El seminario recorre ese camino completo con Power BI. Parte de la extracción y la calidad de los datos, sigue con el modelo, los indicadores y el tablero de control, y termina con la detección de anomalías y la comunicación de hallazgos a un comité de auditoría. El hilo conductor es un caso integrador sobre una organización ficticia del sector agrofinanciero colombiano, con datos sintéticos en los que se han inyectado irregularidades documentadas.

## 3. Competencias (syllabus oficial)

| ID | Tipo | Descripción |
|---|---|---|
| C1 | Cognitiva | Reconocer y aplicar métodos que contribuyen al análisis de datos y a la toma de decisiones. |
| C2 | Comunicativa | Proponer y presentar estrategias argumentadas con base en métodos de analítica de datos. |
| C3 | Investigativa | Aplicar métodos de analítica que permitan visualizar escenarios de manera integrada para apoyar a las organizaciones en su toma de decisiones. |

## 4. Resultados de aprendizaje (syllabus oficial)

| ID | Resultado de aprendizaje | Competencias | Unidades |
|---|---|---|---|
| RA1 | Diseñar y aplicar modelos de inteligencia de negocios orientados al control organizacional, integrando procesos de extracción, transformación y visualización de datos para fortalecer la toma de decisiones estratégicas. | C1, C3 | U1, U2, U3 |
| RA2 | Implementar dashboards e indicadores clave de control interno que permitan monitorear riesgos, detectar anomalías y evaluar el cumplimiento normativo en tiempo real dentro de las organizaciones. | C1, C3 | U2, U3, U4 |
| RA3 | Analizar y comunicar hallazgos mediante técnicas de analítica descriptiva, predictiva y prescriptiva, vinculando la información generada con recomendaciones prácticas para auditoría, aseguramiento y gestión de riesgos. | C2, C3 | U3, U4 |

> **Alcance de "tiempo real" (RA2).** Con Power BI Desktop y archivos CSV, el curso trabaja con monitoreo **periódico y automatizable** (actualización programable). El monitoreo en tiempo real estricto (streaming) se explica conceptualmente en U4, pero no se implementa porque requiere licencias y servicios en la nube. Ver la matriz de alineación.

## 5. Unidades y contenidos

Las unidades U1 a U3 corresponden a los tres temas del syllabus oficial. La U4 se agrega porque las temáticas originales no cubren de forma explícita la detección de anomalías ni la analítica predictiva y prescriptiva que exigen RA2 y RA3.

| Unidad | Tema oficial | Contenidos |
|---|---|---|
| **U1. BI y Business Analytics** | T1. Inteligencia de negocios y su ejecución mediante indicadores | Definición y objetivos de BI; componentes y procesos (ETL, almacenamiento de datos, data warehouse, informes y dashboards); BI frente a Business Analytics: conceptos, objetivos, alcance, procesos, herramientas y técnicas; ciclo de vida analítico; CRISP-DM. Práctica: ETL con Power Query. |
| **U2. BI en el control organizacional** | T2. La inteligencia de negocios en el control organizacional | Rol estratégico de BI en el control organizacional (datificación y control); gobierno y calidad de datos; KPIs y KRIs de control interno; dashboards de monitoreo; cuadro de mando integral. Práctica: modelo estrella y medidas DAX. |
| **U3. Visualización y comunicación** | T3. Visualización e interpretación para el BI en cuadros de mando integral y su comunicación a la gerencia | Principios de visualización efectiva; storytelling con datos; comunicación de hallazgos a la alta dirección y a los órganos de control; buenas prácticas de presentación. Práctica: tablero de control y narrativa ejecutiva. |
| **U4. Analítica para el aseguramiento** *(nueva)* | Cubre RA2 (detección de anomalías, cumplimiento) y RA3 | Control interno y gestión de riesgos (COSO 2013, ISO 31000); auditoría y monitoreo continuos; analítica forense: Ley de Benford, duplicados, pruebas de razonabilidad, muestreo; analítica descriptiva, predictiva y prescriptiva; Isolation Forest y regresión logística; marco normativo colombiano aplicable. Práctica: alertas en Power BI y modelo de ML consumido desde Power BI. |

## 6. Metodología

Seminario-taller, como lo establece el syllabus oficial. Cada sábado combina exposición breve del docente, discusión de casos, laboratorios guiados en Power BI y trabajo en equipo sobre el caso integrador. El trabajo autónomo prepara cada sesión (lecturas, quices, talleres) y la extiende (avances del caso integrador, profundización).

- **Antes de la sesión 1:** informe de lectura en el formato institucional "FrmFichaRevisiónDocumental" sobre uno de los artículos de la sección *Reportes y artículos* (ver [lecturas](../lecturas/lecturas.md)), quiz diagnóstico e instalación de Power BI.
- **Desde la sesión 2:** exposiciones de equipo asignadas en la sesión 1 (casos y lecturas), con un equipo expositor y un equipo de réplica.
- **Equipos:** de 4 a 5 integrantes, conformados en la sesión 1 y estables durante todo el curso.
- **Software:** Power BI Desktop (gratuito, Windows) y Excel. Python (o Google Colab, sin instalación) se usa desde el Taller T0 y en la profundización C. Alternativas para Mac en [`recursos/instalacion.md`](../recursos/instalacion.md). La Universidad dispone de salas con el software, sujetas a programación.

## 7. Distribución de la carga de trabajo (96 h)

### 7.1 Por momento

| Momento | Presencial | Independiente | Total |
|---|---:|---:|---:|
| Antes del sábado 1 (semana 1) | 0 | 8 | 8 |
| Sábado 1 | 8 | 0 | 8 |
| Entre S1 y S2 (semanas 2–3) | 0 | 24 | 24 |
| Sábado 2 | 8 | 0 | 8 |
| Entre S2 y S3 (semanas 4–5) | 0 | 24 | 24 |
| Sábado 3 | 8 | 0 | 8 |
| Después del S3 (semanas 6–7) | 0 | 16 | 16 |
| **Total** | **24** | **72** | **96** |

### 7.2 Por unidad y momento

| Unidad | S1 | S2 | S3 | Pre-S1 | S1→S2 | S2→S3 | Post-S3 | **Presencial** | **Independiente** | **Total** |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| U1. BI y Business Analytics | 6 | 0 | 0 | 8 | 6 | 0 | 0 | 6 | 14 | 20 |
| U2. BI en el control organizacional | 2 | 4 | 0 | 0 | 14.5 | 0.5 | 0 | 6 | 15 | 21 |
| U3. Visualización y comunicación | 0 | 4 | 0 | 0 | 0 | 5.5 | 0 | 4 | 5.5 | 9.5 |
| U4. Analítica para el aseguramiento | 0 | 0 | 5 | 0 | 0 | 10 | 6.5 | 5 | 16.5 | 21.5 |
| Caso integrador (U1–U4) | 0 | 0 | 3 | 0 | 3.5 | 8 | 9.5 | 3 | 21 | 24 |
| **Total** | **8** | **8** | **8** | **8** | **24** | **24** | **16** | **24** | **72** | **96** |

> U3 tiene pocas horas propias porque su aplicación principal ocurre dentro del caso integrador: el Avance 2 (6 h) es el tablero con KPIs y storytelling. El detalle actividad por actividad está en [`cronograma/trabajo_independiente.md`](../cronograma/trabajo_independiente.md).

## 8. Cronograma resumido

Fechas de ejemplo. Las reales las fija la programación académica; el cronograma requiere al menos dos semanas entre sábados.

| Semana | Fechas de ejemplo | Momento | Hito |
|---|---|---|---|
| 1 | 14–19 feb 2027 | Pre-S1 (8 h) | Quiz diagnóstico, ficha de lectura, Taller T0 |
| — | **Sáb 20 feb 2027** | **Sábado 1** | U1 completa + inicio U2 (calidad de datos en Power Query) |
| 2–3 | 21 feb – 5 mar | S1→S2 (24 h) | Quiz U1, T1, T2, profundización A, **Avance 1** |
| — | **Sáb 6 mar 2027** | **Sábado 2** | U2 (modelo, DAX, KPIs, cuadro de mando integral) + U3 |
| 4–5 | 7–19 mar | S2→S3 (24 h) | Quices U2 y U3, T3, T4, profundización B, **Avance 2** |
| — | **Sáb 20 mar 2027** | **Sábado 3** | U4 + clínica + **sustentación ante el comité** |
| 6–7 | 21 mar – 3 abr | Post-S3 (16 h) | Quiz U4, profundización C, **entrega final**, coevaluación |

Agendas hora a hora: [Sábado 1](../cronograma/sabado_1.md) · [Sábado 2](../cronograma/sabado_2.md) · [Sábado 3](../cronograma/sabado_3.md).

## 9. Evaluación

**Prevalece el sistema de evaluación oficial del syllabus institucional.** La ponderación que se había propuesto para el rediseño no se aplica; la diferencia se explica en `CHANGELOG.md`. Cada componente oficial se desagrega así:

| Bloque oficial | Componente oficial | Peso | Desagregación en este curso | Modalidad |
|---|---|---:|---|---|
| 70% | Quices | 15% | Quices de cierre U1, U2, U3 y U4 (3.75% c/u). El quiz diagnóstico es formativo (0%) | Individual |
| 70% | Informe de lectura previa | 10% | Ficha de revisión documental previa al S1 | Individual |
| 70% | Talleres y trabajos en clase | 20% | Laboratorios en clase L1–L3 (2% c/u = 6%) · Talleres autónomos T0 (1%), T1–T4 (2% c/u) = 9% · Profundización A (2%), B (1.5%), C (1.5%) = 5% | Grupal* |
| 70% | Exposiciones | 25% | Exposición o réplica de caso (10%) · Sustentación ante el comité de auditoría (15%) | Grupal |
| 30% | Caso de estudio con minería, analítica, visualización y estrategias de mejora | 30% | Avance 1 (7.5%) · Avance 2 (7.5%) · Entrega final: tablero con detección de anomalías e informe ejecutivo (15%) | En equipo |
| | **Total** | **100%** | | |

\* Los talleres autónomos T0–T4 y las actividades de profundización se entregan en equipo, con evidencias individuales de participación. La **coevaluación** final ajusta la nota individual de los componentes grupales con un factor entre 0.8 y 1.0 (ver [`evaluacion/criterios_calificacion.md`](../evaluacion/criterios_calificacion.md)).

Rúbricas: [`evaluacion/rubricas.md`](../evaluacion/rubricas.md) y [`caso-integrador/`](../caso-integrador/).

## 10. Bibliografía

La bibliografía está organizada por unidad en [`lecturas/lecturas.md`](../lecturas/lecturas.md), con tres categorías:
- **Obligatoria:** del syllabus oficial y asignada en la ruta semanal.
- **Complementaria:** del syllabus oficial, opcional.
- **Propuesta:** fuentes abiertas agregadas para cubrir control interno, riesgos, auditoría continua, analítica forense y normativa colombiana. Se distinguen claramente de las del syllabus oficial.

Las herramientas de visualización distintas de Power BI fueron excluidas del material de apoyo. Ver [`recursos/enlaces_verificados.md`](../recursos/enlaces_verificados.md).

## 11. Integridad académica y uso de datos

- Todos los datos del curso son **sintéticos** y fueron generados por script. No contienen información real de ninguna entidad ni persona.
- Los artículos y casos con derechos de autor se consultan en la Biblioteca de la Universidad. Este repositorio no reproduce sus textos.
- El uso de asistentes de IA generativa es permitido como apoyo, pero debe declararse en cada entrega con una nota que indique en qué parte se usó y cómo se verificó el resultado.
