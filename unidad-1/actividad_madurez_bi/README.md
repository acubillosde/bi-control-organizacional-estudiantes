# Actividad · Diagnóstico de madurez de BI con evidencia

**Unidad:** U1 (con debrief en la U2, Sábado 2) · **RA:** RA1 (refuerza RA2) · **Trabajo:** individual · **Es la Profundización A (2% de la nota final)** · **Horas estimadas:** 2 h 45 min · **Se publica:** al cierre del S1 · **Fecha límite:** cierre de la semana 2, 23:59 (sábado de la semana 2)
**Plantilla:** [plantilla_diagnostico.md](plantilla_diagnostico.md) · **Rúbrica:** [R6](../../evaluacion/rubricas.md#r6-diagnóstico-de-madurez-de-bi-con-evidencia)

> **Antes de esta actividad, en el S1:** cada equipo hizo un [diagnóstico rápido de COAGUA y un plan de transformación](plan_transformacion.md) (L1). Esta actividad es el diagnóstico individual, completo y con evidencia; en el S2 se contrasta con el del equipo.

## Propósito
Diagnosticar la madurez de BI de una organización **con evidencia verificable y no con percepción**, e identificar el eslabón más débil y el riesgo de control que genera.

Esta actividad entrena una competencia que el auditor usa todos los días: sostener un juicio con evidencia, declarar qué tan seguro está y reconocer lo que no puede verificar.

**Qué no es:** no es una auditoría ni una calificación de la entidad. Mide la capacidad de BI **dentro del alcance que usted declara**.

## Dos rutas, un mismo instrumento

| | Ruta A · Organización propia | Ruta B · Caso general (COAGUA) |
|---|---|---|
| Para quién | Quien tiene acceso razonable a la información de su organización | Quien no tiene acceso, o prefiere no usar su organización |
| Alcance | Una unidad, gerencia o proceso que usted declara | COAGUA completa |
| Fuente de evidencia | Documentos, sistemas y procesos de su organización, **descritos y no adjuntos** | Solo materiales del repositorio del curso ([catálogo de fuentes](../../caso-integrador/madurez/coagua_fuentes.md)) |
| Particularidad | Confidencialidad y anonimización | «No verificable» y preguntas pendientes para el cliente |
| Rúbrica | La misma | La misma, con la adaptación del criterio 4 |

**Elegir la Ruta B no tiene ninguna penalización.** Se califica la calidad de la evidencia y del juicio, no el nivel obtenido.

## Reglas de evidencia
Cada pregunta se califica de **1 a 5**. Los valores 2 y 4 se permiten solo si usted justifica por qué la situación queda entre dos anclas.

| Tipo | Significa |
|---|---|
| **D** | **Documento:** política, manual, glosario, diagrama, acta, reporte |
| **S** | **Sistema:** usted vio funcionar el sistema, el modelo o el tablero, o tiene acceso a él |
| **O** | **Observación directa** de un proceso en operación |
| **T** | **Testimonio:** alguien se lo dijo |

1. **Una calificación mayor a 3 exige evidencia tipo D o S.** Con solo O o T, el máximo es 3.
2. **«NV» (no verificable)** es una respuesta válida y **no se promedia**. Registre qué evidencia haría falta.
3. **Confianza** por pregunta: **A** (alta: evidencia D o S vigente) · **M** (media) · **B** (baja: solo T).
4. La nota no premia un nivel alto. Premia la calidad de la evidencia y la coherencia del juicio.

*Ejemplo:* su jefe le dice que «todo está automatizado». Eso es un testimonio (T): la calificación máxima es 3 y la confianza es B. Si además usted ve el calendario de cargas y la bitácora de ejecución (D), puede calificar más alto, con confianza A.

## Escala general de niveles
| Nivel | Cómo se ve |
|---|---|
| 1. Informes aislados | Cada área tiene sus hojas de cálculo; las cifras no cuadran |
| 2. Consolidación | Se centralizan algunas fuentes; informes periódicos estándar |
| 3. Integración | Almacén o data marts; definiciones comunes; tableros por área |
| 4. Gestión con datos | Indicadores con metas y responsables; decisiones basadas en el tablero |
| 5. Analítica avanzada | Predicción y prescripción incorporadas a los procesos |

La escala es didáctica. El objetivo **no** es llegar al nivel 5: el nivel adecuado depende del riesgo y del costo-beneficio. Además, la madurez mide **capacidad, no valor**: un nivel 4 sin decisiones que cambien es un tablero decorativo.

## Instrumento: 4 dimensiones, 12 preguntas
Las columnas «Nivel 1», «Nivel 3» y «Nivel 5» son las anclas. Califique con la que mejor describa lo que usted **verificó**.

### Dimensión 1 · Datos y gobierno

| Cód. | Pregunta verificable | Nivel 1 | Nivel 3 | Nivel 5 | Evidencia aceptable |
|---|---|---|---|---|---|
| D1.1 | ¿Los indicadores clave tienen definición única y dueño? | Cada área calcula las cifras a su manera | Hay glosario para algunos indicadores, sin dueño ni actualización | Catálogo vigente, versionado, con dueño por indicador | Glosario, diccionario de datos, ficha de indicador |
| D1.2 | ¿Se mide la calidad de los datos críticos? | No se mide; se corrige a mano | Reglas de validación en algunas fuentes, sin seguimiento | Indicadores de calidad periódicos con responsable y plan de corrección | Reporte de calidad, reglas de validación, tablero de calidad |
| D1.3 | ¿Están definidos dueño y custodio del dato y la protección de datos personales? | No hay roles definidos | TI custodia; los dueños son informales; la política de datos personales no se aplica al análisis | Roles formalizados, acceso por rol y trazabilidad, cumplimiento de la Ley 1581 | Política de gobierno, acta de roles, manual de tratamiento, matriz de accesos |

### Dimensión 2 · Arquitectura y tecnología

| Cód. | Pregunta verificable | Nivel 1 | Nivel 3 | Nivel 5 | Evidencia aceptable |
|---|---|---|---|---|---|
| D2.1 | ¿Cómo se integran las fuentes? | Archivos enviados por correo; consolidación manual | Repositorio central con cargas para parte de las fuentes | Almacén o lago integrado, con cargas automáticas y monitoreadas | Diagrama de arquitectura, calendario de cargas, bitácora de ejecución |
| D2.2 | ¿El procedimiento que produce el dato lo puede repetir otra persona? | Depende de una persona; sin documentar | Documentado en parte; ejecución semiautomática | Automatizado, versionado y repetible | Manual, scripts versionados, registros de ejecución |
| D2.3 | ¿Existe un modelo compartido y seguridad por rol? | Cada informe consulta la fuente directa | Modelos por área, sin certificación | Modelo corporativo certificado, con seguridad por rol o por fila | Catálogo de modelos, configuración de seguridad, política de publicación |

### Dimensión 3 · Procesos y entrega

| Cód. | Pregunta verificable | Nivel 1 | Nivel 3 | Nivel 5 | Evidencia aceptable |
|---|---|---|---|---|---|
| D3.1 | ¿Cuánto tarda en estar disponible la información de un proceso crítico? | Semanas o más | Mensual o semanal | Diaria o casi en línea | Calendario de publicación, sello de actualización del informe |
| D3.2 | ¿Cómo se gestionan los requerimientos de información? | Por correo, sin prioridad | Canal definido, sin tiempos de respuesta | Proceso con priorización, tiempos medidos y ciclo de vida de los tableros | Formato o mesa de solicitudes, tiempos de entrega, inventario de reportes |
| D3.3 | ¿Los indicadores tienen fórmula, meta, umbral y responsable? | Sin metas | Metas parciales, sin umbral o sin responsable | KPI, KRI y KCI completos, con excepciones escaladas | Fichas de indicadores, tablero, actas de seguimiento |

### Dimensión 4 · Cultura y uso

| Cód. | Pregunta verificable | Nivel 1 | Nivel 3 | Nivel 5 | Evidencia aceptable |
|---|---|---|---|---|---|
| D4.1 | ¿Se documentan decisiones apoyadas en los informes? | Los informes no aparecen en las decisiones | Se citan en comités, sin trazabilidad | Decisiones y acciones trazables al tablero | Actas, planes de acción vinculados a indicadores |
| D4.2 | ¿Los usuarios usan y entienden los datos? | Poco uso; dudas sobre las cifras | Formación puntual; uso desigual | Formación continua y uso medido | Estadísticas de uso, plan de formación, encuesta |
| D4.3 | ¿Hay patrocinio con presupuesto? | Ninguno | Apoyo declarado sin presupuesto | Sponsor ejecutivo, presupuesto y metas en el plan estratégico | Plan estratégico, presupuesto, comité de datos |

### Banderas de riesgo de control (sí / no / no sé)
Se responden aparte y **no entran al promedio**. Conectan con los riesgos del BI de autoservicio que vimos en el S1.

| Cód. | Bandera | Riesgo de control |
|---|---|---|
| B1 | ¿Hay informes críticos en hojas de cálculo que solo una persona sabe actualizar? | Dependencia de una persona; falta de continuidad |
| B2 | ¿Circulan por correo archivos con datos personales o sensibles? | Datos fuera del perímetro; incumplimiento de la Ley 1581 |
| B3 | ¿Un mismo indicador tiene cifras distintas entre áreas? | Múltiples versiones de la verdad |
| B4 | ¿Los cambios a fórmulas o consultas críticas quedan sin rastro? | Pérdida de evidencia y de trazabilidad |

## Cálculo del perfil
- **Puntaje de dimensión** = promedio de sus preguntas verificables. Las NV se excluyen del promedio y se informa cuántas hubo.
- **No se calcula un nivel global promedio.** Un promedio oculta el eslabón débil.
- **Dimensión limitante** = la de menor puntaje. Es la que define la confiabilidad del tablero.
- Si una dimensión tiene **2 o 3 preguntas NV**, se declara **«perfil incompleto»** en esa dimensión.

Descargue la [plantilla de Excel](plantilla_diagnostico.xlsx): hace el cálculo automáticamente (puntajes, NV, perfil incompleto, dimensión limitante y radar) y revisa las reglas de evidencia. La [plantilla en texto](plantilla_diagnostico.md) trae las mismas fórmulas, por si prefiere armarlo usted.

## Entregable (máximo 3 páginas, PDF)
1. **Ficha de alcance** (media página): organización (o «Entidad A» si anonimiza), unidad evaluada, sector, tamaño por rangos y su rol.
2. **Matriz de diagnóstico** (12 filas): puntaje, tipo de evidencia, descripción de la evidencia y confianza. Más las 4 banderas.
3. **Perfil por dimensiones:** tabla o gráfico de radar.
4. **Análisis** (máximo 200 palabras): la dimensión limitante, el riesgo de control que genera (con referencia al **principio 13 de COSO 2013**: información relevante y de calidad) y **una acción realizable en 90 días**.
5. **Declaración de confidencialidad** (Ruta A): una frase.

Nombre del archivo: `Madurez_<Apellido>_<Ruta>.pdf`, por ejemplo `Madurez_Gomez_A.pdf`.

## Ruta A · Organización propia

**Pasos**
1. **Declare el alcance.** Un alcance estrecho y honesto vale más que uno amplio y vago.
2. Recorra las 12 preguntas y busque evidencia para cada una.
3. Responda las 4 banderas.
4. Calcule el perfil y redacte el análisis.
5. Anonimice y entregue.

**Reglas de confidencialidad**
- Puede anonimizar el nombre de la organización y de las personas.
- **No adjunte documentos, cifras ni datos personales de la organización.** Describa la evidencia: tipo, nombre genérico, fecha y quién la mantiene.
- Si la evidencia es confidencial, declare que existe y cuáles son sus características, sin reproducirla.
- El docente no solicita ni conserva documentos internos.

*Ejemplo de descripción de evidencia:* «D · Glosario de indicadores de la gerencia financiera (hoja de cálculo), versión de enero, mantenido por el área de planeación». Es suficiente. No se pega el glosario.

## Ruta B · Caso general (COAGUA)

Los pasos son los mismos, con estas diferencias:
- **La única fuente permitida es el repositorio del curso.** El [catálogo de fuentes](../../caso-integrador/madurez/coagua_fuentes.md) dice qué hay disponible y a qué preguntas podría aportar.
- **Lo que no se puede verificar con ese material se registra como NV.** Por cada NV escriba **la pregunta que haría al gerente de COAGUA y qué evidencia pediría**.
- **Su ETL, sus tableros y sus resultados del curso no son evidencia de COAGUA.** Son lo que usted construye; no la capacidad de la cooperativa.
- El diagnóstico **no debe afirmar ni sugerir si hay irregularidades en los datos**, ni cuántas ni de qué tipo. Esta actividad mide la capacidad de BI, no el contenido de los datos: ese análisis es del caso integrador.
- Los datos son sintéticos: no atribuya hallazgos a entidades reales.

*Ejemplo de NV bien formulada (para otra pregunta, solo como modelo):* «**D1.1 · NV.** Pregunta al gerente: ¿existe un documento que defina cada indicador clave y su responsable? Evidencia que pediría: el glosario o catálogo de indicadores, con fecha de última actualización y dueño por indicador».

## Rúbrica
Resumen (la rúbrica completa, con niveles de desempeño, está en [R6](../../evaluacion/rubricas.md#r6-diagnóstico-de-madurez-de-bi-con-evidencia)):

| Criterio | Peso |
|---|---:|
| 1. Calidad de la evidencia | 35% |
| 2. Coherencia del juicio y confianza | 25% |
| 3. Dimensión limitante y riesgo de control | 25% |
| 4. Comunicación y cumplimiento | 15% |

## Calendario y carga
| Momento | Qué pasa |
|---|---|
| Cierre del S1 (16:40–17:00) | Se publica y se anuncia la actividad |
| Semana 2 | Trabajo independiente: **2 h 45 min** (45 min instrumento · 75 min evidencia · 45 min redacción) |
| Cierre de la semana 2 | Entrega del PDF y del formulario anónimo con los puntajes por dimensión (Ruta A) |
| Semana 3 | El docente consolida el agregado anónimo de la cohorte. El Avance 1 del caso integrador vence el miércoles de esa semana: la actividad ya está entregada |
| Sábado 2 | **Debrief de 15 minutos** dentro del caso del centro comercial: [guía del caso](../../casos/caso_centro_comercial.md#debrief) |

## Conexión con el resto del curso
- **U1, S1:** la diapositiva de madurez y la actividad «la arquitectura de su organización» son el antecedente: la capa más débil de la arquitectura apunta a la dimensión más débil.
- **U2, S2:** el caso del centro comercial presenta un modelo formal de madurez. Allí se contrasta con este instrumento.
- **Caso integrador:** las dimensiones del instrumento (gobierno, calidad, indicadores) son los mismos temas que usted aplicará a los datos de COAGUA.
