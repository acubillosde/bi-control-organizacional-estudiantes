# CHANGELOG

## 2026-11-25 · Verificación en Power BI de los hechos de Aurora

- Nueva guía [`casos/verificacion_aurora.md`](casos/verificacion_aurora.md): 17 verificaciones (V01 a V17) para que el estudiante compruebe en su Power BI cada hecho de Aurora, con ciclo prediga → construya → compare → concluya. Trae pasos, Power Query (M), medidas DAX, una pista si no coincide y, al final, los valores esperados. Los valores salen de los datos.
- `caso_aurora.md` enlaza la guía.


## 2026-11-25 · Tiendas Aurora pasa a su propia presentación


## 2026-11-25 · L1: el diagnóstico y el plan se demuestran antes de hacerlos


## 2026-11-25 · Caso de demostración: Tiendas Aurora

<!-- REPO:ESTUDIANTES -->
Nuevo caso ficticio de demostración, [Tiendas Aurora](casos/caso_tiendas_aurora.md) (cadena de 12 tiendas de barrio), con sus datos en `datos/demo_aurora/`. El docente lo usa para mostrar cada concepto aplicado; el caso integrador sigue siendo COAGUA, que cada equipo trabaja por su cuenta.
<!-- /REPO:ESTUDIANTES -->


## 2026-11-25 · Se elimina el caso SYSCO

<!-- REPO:ESTUDIANTES -->
La sesión de casos del S1 usa la Distribuidora Andina (ficticio) y la DIARI. Se retira la guía del caso SYSCO y sus referencias.
<!-- /REPO:ESTUDIANTES -->


## [Sin publicar] · Actividad «Diagnóstico de madurez de BI con evidencia»

- Nueva actividad individual de la U1 con dos rutas (organización propia o COAGUA), un instrumento de 4 dimensiones y 12 preguntas, reglas de evidencia y rúbrica R6: [`unidad-1/actividad_madurez_bi/`](unidad-1/actividad_madurez_bi/README.md).
- Catálogo de fuentes para la Ruta B: [`caso-integrador/madurez/coagua_fuentes.md`](caso-integrador/madurez/coagua_fuentes.md).
- **Nuevo L1 del Sábado 1: del diagnóstico al plan de transformación (sin Power BI).** En equipo y sobre COAGUA: pregunta y anomalía (15'), inventario de fuentes (15'), diagnóstico rápido de madurez con una pregunta por dimensión y cuatro banderas (35') y plan de transformación en tres horizontes (35' + 10' de galería). La clínica de calidad se mantiene en la tarde. Entregable: plan de datos + diagnóstico rápido + plan; se califica con la nueva rúbrica **R7** (la R2 queda para L2 y L3). La demostración de Power Query y el `.pbix` exploratorio salen del S1; sus diapositivas quedan como ampliación de apoyo para el T1. Guía: [`plan_transformacion.md`](unidad-1/actividad_madurez_bi/plan_transformacion.md). El guion pasa a 67 diapositivas. La PA individual se mantiene; el debrief del S2 incluye la revisión del plan.
- **Quiz diagnóstico: la pregunta 1 pasa de tablas dinámicas de Excel a *pandas*** (agrupar y sumar), en coherencia con el T0 en Python. El área del resumen pasa a «Python y análisis de datos (pandas)». Hay que regenerar el formulario de Google Forms si ya se creó.
- **Capa mínima de IA generativa, centrada en el control (sin horas nuevas):** una diapositiva en el guion de la U2 («IA generativa sobre los datos: primero el gobierno») y otra en la U3 («Titulares y narrativas generados por IA: ¿quién verifica?»); verificación del apoyo de IA, con declaración, dentro del T2 (opcional) y del T3; una línea en la guía del plan de transformación del L1; pregunta 11 en el Quiz U2 (22 minutos). Sin tutoriales de herramientas ni afirmaciones sobre productos concretos.
- **Lecturas propuestas sobre riesgos de IA y control interno (sin horas asignadas):** COSO (2026) *Achieving Effective Internal Control Over Generative AI*, IIA (2024) *AI Auditing Framework*, NIST (2024) AI 600-1 y CONPES 4144 de 2025, con una guía de lectura de cinco preguntas en [`unidad-2/lecturas.md`](unidad-2/lecturas.md). Se verificaron título, editor y acceso en las páginas oficiales; la fecha exacta y la gratuidad del documento de COSO, el contenido detallado del PDF del IIA, la lista de riesgos de NIST y el texto del CONPES quedan **pendientes de verificación**.
- **Plantilla de Excel descargable para el diagnóstico de madurez** ([`plantilla_diagnostico.xlsx`](unidad-1/actividad_madurez_bi/plantilla_diagnostico.xlsx)): listas desplegables para puntaje, confianza y banderas; revisión automática de las reglas de evidencia (más de 3 exige D o S, solo testimonio implica confianza B, NV con evidencia faltante); perfil por dimensión con NV, «perfil incompleto» y dimensión limitante; radar y contador de palabras del análisis. Se genera con `scripts/generar_plantilla_madurez.py`, leyendo las preguntas del README de la actividad. La plantilla en texto se conserva.
- **Plantilla de Excel del L1** ([`plantilla_diagnostico_rapido.xlsx`](unidad-1/actividad_madurez_bi/plantilla_diagnostico_rapido.xlsx)): diagnóstico rápido de cuatro preguntas con revisión automática de las reglas de evidencia y hoja del plan de transformación con una revisión automática (brecha de evidencia en 90 días, dueño, producto e indicador por iniciativa, iniciativas de capacidad, tres horizontes, decisión al comité). También se genera con `scripts/generar_plantilla_madurez.py`.
- **Matriz de diagnóstico realineada con la literatura de modelos de madurez de BI:** las 12 preguntas ahora tienen los **cinco niveles anclados** (se redactaron los niveles 2 y 4; los niveles 1, 3 y 5 se conservan), con regla de cumplimiento acumulativa (se asigna el nivel más alto cuya descripción se cumple por completo). Se elimina la regla de justificar los valores 2 y 4. Nueva [nota metodológica](unidad-1/actividad_madurez_bi/fundamento_metodologico.md) con la correspondencia con los modelos de Lahrmann et al. (2011), Raber, Winter y Wortmann (2012) y TDWI (2020), qué se verificó, límites y referencias. Las plantillas de Excel se regeneran con las cinco anclas. **Pendiente de verificación:** el artículo de Raber et al. (2012) y la guía de TDWI (2020); la correspondencia es conceptual y la hizo el curso.
- **Expediente de COAGUA para la Ruta B** ([`expediente_coagua.md`](caso-integrador/madurez/expediente_coagua.md)): ocho documentos internos ficticios (glosario de un área, mapa de sistemas, bitácora del cierre mensual, fichas de indicadores, acta del comité, registro de solicitudes, política de datos personales, correo de la gerencia) que permiten diagnosticar casi todas las preguntas en la semana 2. Diseño: perfil **desigual** (patrocinio presente, gobierno de datos débil) y tres trampas (testimonio frente a documento, un glosario que parece vigente y no lo es, un frente tentador que no es el crítico). Catálogo y mapa de evidencia actualizados; el diagnóstico rápido del S1 se hace sin el expediente. El expediente no dice nada sobre los datos ni sobre las piezas ocultas de la entrevista.
- Quiz U1: tres preguntas nuevas (11 a 13); el tiempo pasa de 20 a 25 minutos.
- Debrief de 15 minutos en la guía del caso del centro comercial (S2).
- **El ETL guiado pasa a la semana 2 (T1) y el S1 trabaja sobre el caso.** El laboratorio L1 del Sábado 1 es ahora un taller de caso («de la pregunta al dato») con un plan de datos como entregable (sigue valiendo 2%); la práctica 01 completa se hace en el T1, que sube de 3.0 a 5.5 h. El Avance 1 baja de 6.0 a 3.5 h y EX pasa de la semana 2 a la 3 para equilibrar la carga (12.75 y 11.25 h). Las 24 h presenciales y las 72 independientes no cambian; sí cambian las horas por unidad (U1 +2.5 y caso integrador −2.5) en la tabla 7.2 del syllabus.
- **Taller T0, Parte B, en Python:** la exploración de `pagos.csv` pasa de tablas dinámicas de Excel a *pandas*, con un cuaderno de partida ([`unidad-1/t0_exploracion_pagos.ipynb`](unidad-1/t0_exploracion_pagos.ipynb)) que corre en Google Colab sin instalar nada. Las horas del T0 no cambian (3.5 h).
- Caso ficticio alternativo a SYSCO, cuando no se dispone del original: [`casos/caso_distribuidora_andina.md`](casos/caso_distribuidora_andina.md) (texto completo y guía de discusión con las mismas siete preguntas). La pregunta 8 del quiz U1 deja de nombrar solo a SYSCO.
- **La Profundización A pasa a ser este diagnóstico** (individual, 2.75 h, 2%, rúbrica R6). El perfilado del maestro de clientes anterior se conserva como extensión opcional sin nota en `unidad-2/actividades.md`.
- Índices de la U1 y la U2 actualizados.
- Lecturas propuestas nuevas, sin horas asignadas: DAMA-DMBOK (U2), CRISP-ML(Q) (U4) y la guía del IIA sobre tecnologías de análisis de datos como contexto histórico (U4).


## [1.0.0] · 2026-10-27 · Primera versión del curso rediseñado

### Fuente
- Se transcribió el syllabus institucional (PDF de 7 páginas con capa de texto; no requirió OCR) a `fuentes/syllabus_original.md`, que es la fuente de verdad. Se eliminaron el código de formato institucional de cada página y los saltos de línea que partían palabras y URL, y se reconstruyeron las tablas.
- `fuentes/` está excluida de ambos repositorios (`.gitignore`) porque contiene el PDF institucional.
- **No existía `fuentes/contexto_chat.md`**, por lo que no fue posible contrastar la extracción con ese archivo.

### Diferencias con el syllabus oficial y con el encargo de diseño

| # | Tema | Encargo de diseño | Syllabus oficial | Decisión |
|---|---|---|---|---|
| 1 | **Sistema de evaluación** | Talleres 20% · Avances 20% · Tablero final 25% · Sustentación 25% · Quices y participación 10% | Quices 15% · Informe de lectura previa 10% · Talleres y trabajos en clase 20% · Exposiciones 25% · Caso de estudio 30% | **Prevalece el oficial.** Se desagregó así: los avances y el tablero final van dentro de "Caso de estudio"; la sustentación va dentro de "Exposiciones" (15%) junto con la exposición de caso (10%); los talleres autónomos y la profundización van dentro de "Talleres" (20%). La "participación" no tiene peso propio porque el sistema oficial no la contempla |
| 2 | Nombre del curso | "Inteligencia de Negocios para el Control Organizacional" | "Seminario de Interacción 7 – Inteligencia de Negocios" | Se usa el nombre oficial como título y el propuesto como subtítulo |
| 3 | Programa | "Posgrado en analítica aplicada a contabilidad, auditoría y aseguramiento" | "Maestría en Control Organizacional" | Se usa el oficial |
| 4 | Código, prerrequisitos | Extraer del PDF | No figuran | Se registran como "no indicados". Requisitos de entrada: Excel (tablas dinámicas), PowerPoint y portátil |
| 5 | Horario de los sábados | 09:00–17:00 con 1 h de almuerzo = 7 h efectivas (3 × 7 = 21 ≠ 24) | 24 h presenciales | **08:00–17:00** con almuerzo de 12:00 a 13:00 = 8 h efectivas. Las pausas activas de 10' van dentro de los bloques de 2 h. *Debe validarse con la coordinación* |
| 6 | Unidad 4 | Agregar | No existe | Agregada, con la justificación de cubrir RA2 (anomalías) y RA3 (descriptiva, predictiva y prescriptiva) |
| 7 | Herramienta de visualización | Solo Power BI | El material de apoyo incluye el enlace de otra herramienta de visualización | Ese enlace y cualquier mención a esa herramienta fueron **excluidos** de todo el material |
| 8 | Lectura previa Gimenez (2024) | — | Aparece en Metodología, no en la bibliografía | Complementaria, *pendiente de verificación* (sin registro bibliográfico confirmable) |
| 9 | Davenport y Patil | — | Año 2013 | Se corrige a **2012** (HBR, octubre, 90(10), 70–76), verificado |
| 10 | Lluís (2007), páginas | — | "Capítulo 1 pp. 20 a 4…" (truncado en el PDF) | Según el índice del libro, el cap. 1 ocupa las pp. 19–56. Se asignan las pp. 20–45 (estimado) para respetar el tope de lectura previo al S1 |
| 11 | Material de apoyo comercial y antiguo | Marcar | — | Marcado como *contexto histórico* o *complementaria opcional (comercial)* (ver `lecturas/lecturas.md`) |
| 12 | "El lado oscuro de la analítica" | Marcar como "por verificar" | Davenport y Harris (2007) | Marcado **por verificar**. Se halló un posible registro de catálogo, que no se confirma |

### Decisiones de diseño (para validar)
1. **Ventana de 7 semanas**, con S1, S2 y S3 separados por 14 días. Fechas de ejemplo: 20 feb, 6 mar y 20 mar de 2027; entrega final el 3 abr de 2027.
2. **Distribución presencial:** U1 6 h · U2 6 h (2 en el S1 y 4 en el S2) · U3 4 h · U4 5 h · Integrador 3 h.
3. **T4 en aula invertida:** la mecánica de Benford y duplicados se practica antes del S3 para que el sábado se dedique a interpretar y sustentar.
4. **Sustentación en el S3 e informe final después:** el comité retroalimenta en vivo y la versión final incorpora esa retroalimentación (2 semanas después).
5. **Equipos de 4–5 integrantes**, 6 equipos de referencia. Cada caso se trabaja con un equipo expositor y uno de réplica.
6. **Coevaluación** con un factor individual entre 0.8 y 1.0 sobre los componentes grupales.
7. **Organización ficticia:** Cooperativa Agrofinanciera Los Guaduales (COAGUA). Segunda industria (profundización B): retail ("Almacenes Mirador", también ficticia).
8. **Caso colombiano actual** que complementa a SYSCO: la DIARI de la Contraloría General de la República, documentada por la OCDE (2021).
9. **Políticas del caso ficticias:** límites de aprobación, calificación A–E por mora, topes por línea y límite de 300 M por cliente. No se atribuyen a normas reales.
10. **Separación de repositorios:** al de estudiantes no van las guías del docente, las presentaciones, las respuestas, las soluciones, la clave de anomalías, las notas de facilitación, el generador de datos (porque revela la lógica de inyección) ni el script de control de calidad. Los resultados precalculados (`datos/resultados/`) **sí** se publican, para quienes no tienen Python.
11. **Quices** en `evaluacion/quizzes/` (y no dentro de cada unidad) para tener un solo banco. Cada unidad enlaza al suyo.
12. **Docente:** no se incluyó el nombre ni el correo del profesor que registra el PDF. Queda un campo por completar.
13. **Tiempo real (RA2):** cubierto parcialmente, con actualización programada y diseño de monitoreo continuo. El streaming queda fuera de alcance porque requiere licencias.

### Pendientes de verificación
Ver la lista consolidada en [`recursos/enlaces_verificados.md`](recursos/enlaces_verificados.md) (secciones B y C) y en [`lecturas/lecturas.md`](lecturas/lecturas.md). Resumen:
- Número de caso y autoría en el catálogo de HBP: SYSCO, Watson, Ritz-Carlton (autores, año y páginas).
- Autoría de la guía CRISP-DM de IBM atribuida a "Jensen (2016)".
- Gimenez (2024); los dos artículos "buscar en Biblioteca UEC"; editorial de Moreno y Gómez (2021); año, edición y editorial de Hair (2018).
- Davenport y Harris (2007): **por verificar**.
- Páginas estimadas (est.): Ritz-Carlton, Watson, COSO (resumen ejecutivo), Royal Society (resumen ejecutivo), Auditool, CILIP (caps. 4–5), Lluís (rango asignado).
- Umbrales MAD de Benford (Nigrini, 2012): las fuentes secundarias difieren entre 0.004 y 0.006 para "conformidad cercana".
- Algoritmo del dígito de verificación del NIT: se usa la versión de uso común; contrastar con una fuente de la DIAN.
- Normativa: enlace y numeración vigente del anexo de normas de aseguramiento (Decreto 2420 de 2015), Decreto 1499 de 2017 (MIPG), circular SARLAFT aplicable (Supersolidaria o SFC), Acto Legislativo 04 de 2019, Decreto Ley 403 de 2020, Decreto 2037 de 2019 y alcance del art. 34-7 de la Ley 1474 de 2011 (adicionado por la Ley 2195 de 2022).
- Power BI en Mac: soporte oficial en Windows para ARM y en máquinas virtuales; capacidades de Power BI Service según la licencia institucional; *gateway* para scripts de Python y R.
- Estructura y denominación vigentes de la DIARI en el sitio de la Contraloría.

### Control de calidad
`python scripts/control_calidad.py --estudiantes` verifica:
- horas: 24 + 72 = 96, por tramo y por unidad frente a la ruta semanal;
- tope de lectura del 30% por tramo;
- producto y criterio en cada actividad;
- matriz de alineación (evidencia presencial e independiente por RA);
- pesos = 100%;
- cero menciones de la herramienta excluida;
- enlaces relativos;
- ejecución y reproducibilidad de los scripts;
- ausencia de material docente en el repositorio de estudiantes.
