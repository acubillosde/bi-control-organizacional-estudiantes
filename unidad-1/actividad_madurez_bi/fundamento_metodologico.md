# Nota metodológica · Diagnóstico de madurez de BI

Esta nota dice **en qué se apoya el instrumento, qué se verificó y qué no**. Sirve para que el estudiante sepa qué puede y qué no puede afirmar con el diagnóstico.

## 1. Qué tipo de instrumento es

Es un **modelo de madurez por etapas, adaptado para el curso**. Combina cuatro elementos:

| Elemento | En qué consiste | Por qué se usa |
|---|---|---|
| **Niveles acumulativos** | Cinco niveles. Un nivel se alcanza solo si se cumple por completo su descripción; si se cumple en parte, se queda en el inferior | Es la lógica de los modelos de madurez por etapas: cada nivel parte del anterior |
| **Escala con anclas de conducta** | Cada pregunta describe cómo se ve la situación en los cinco niveles, con hechos observables | Reduce el juicio libre: se compara con una descripción, no con una opinión |
| **Regla de evidencia** | Tipos D, S, O y T; un puntaje mayor a 3 exige D o S; NV es una respuesta válida; la confianza se declara | Un diagnóstico vale lo que vale su evidencia. Es una práctica propia del trabajo de auditoría |
| **Eslabón más débil** | No hay nivel global promedio; se identifica la dimensión limitante | Un promedio oculta la dimensión que limita la confiabilidad del conjunto |

## 2. Correspondencia con modelos publicados

La correspondencia es **conceptual y la hizo el curso**. No significa que los autores de esos modelos avalen este instrumento, ni que cada pregunta salga de un ítem de sus modelos.

### Las cuatro dimensiones

| Dimensión del curso | Se parece a… | Fuente |
|---|---|---|
| **1. Datos y gobierno** | Gobierno y gestión de datos | TDWI, *Analytics Maturity Model*: «governance» y «data» (nombres exactos pendientes de verificar) |
| **2. Arquitectura y tecnología** | Infraestructura de datos y recursos | TDWI (misma fuente); capacidades técnicas de integración en Raber, Winter y Wortmann (2012) |
| **3. Procesos y entrega** | Procesos de BI y de analítica | TDWI, «analytics»; capacidades de proceso en Raber et al. (2012) |
| **4. Cultura y uso** | Organización, uso y efecto individual de la BI | TDWI, «organization»; Lahrmann et al. (2011): uso de la BI y efecto individual |

Lahrmann et al. (2011) observan que muchos modelos de madurez se centran en lo técnico y descuidan el **valor de negocio** de la BI, e integran en su modelo el despliegue, el uso, el efecto individual y el desempeño organizacional. El instrumento del curso hace lo mismo en parte: la dimensión 4 mira el uso, y el análisis pide vincular el hallazgo con un riesgo de control. **No mide el valor ni el desempeño de la organización**: la actividad lo dice expresamente (la madurez mide capacidad, no valor).

### Los cinco niveles

| Nivel del curso | Etiqueta en Raber, Winter y Wortmann (2012) | Etapa en el modelo de TDWI (2020) |
|---|---|---|
| 1. Informes aislados | *Initiate* | *Nascent* |
| 2. Consolidación | *Harmonize* | *Early* |
| 3. Integración | *Integrate* | *Established* |
| 4. Gestión con datos | *Optimize* | *Mature* |
| 5. Analítica avanzada | *Perpetuate* | *Advanced / Visionary* |

La alineación de los nombres es **aproximada**: los niveles del curso se describen con la práctica de BI para el control, y los de esos modelos con otro énfasis. Úsela como orientación para leer la literatura, no como equivalencia exacta.

## 3. Qué se verificó y qué no

| Afirmación | Estado |
|---|---|
| Lahrmann, Wortmann, Marx y Winter (2011), *Business Intelligence Maturity: Development and Evaluation of a Theoretical Model*, HICSS-44. Modelo orientado al impacto: despliegue, uso, efecto individual y desempeño organizacional | **Verificado** en el registro del repositorio de la Universidad de St. Gallen (título, autores, año, evento y resumen). No se leyó el texto completo |
| Hribar Rajterič (2010), *Overview of Business Intelligence Maturity Models*, *Management*, 15(1), 47–67. Compara seis modelos; concluye que la mayoría se centra en una parte de la BI | **Verificado** en el registro de la revista (Hrčak) |
| Raber, Winter y Wortmann (2012), modelo de madurez de capacidades de BI con cinco niveles (*initiate, harmonize, integrate, optimize, perpetuate*) | **Pendiente de verificación:** se confirmó por el resumen en un buscador; no se leyó el artículo ni se confirmaron el número de ítems ni la sede de publicación |
| TDWI (2020), *Analytics Maturity Model Assessment Guide*: cinco etapas y cinco dimensiones | **Pendiente de verificación:** el PDF oficial no se pudo abrir; los nombres de etapas y dimensiones salen de resúmenes de buscador |
| Que las anclas de cada pregunta (niveles 1, 3 y 5) correspondan a ítems de algún modelo publicado | **No se afirma.** Vienen del documento de diseño de la actividad. Las anclas de los niveles 2 y 4 las redactó el curso para completar la escala |

## 4. Límites del instrumento

- **Es didáctico, no un estándar.** No sustituye una evaluación de madurez profesional.
- **No se ha medido su confiabilidad.** No se sabe si dos personas distintas califican igual la misma evidencia. La primera cohorte permitiría revisarlo comparando el diagnóstico de equipo con los individuales.
- **Las anclas intermedias (niveles 2 y 4) son un borrador.** Conviene revisarlas con los resultados de la primera cohorte.
- **El diagnóstico rápido del L1 usa 4 de las 12 preguntas** (una por dimensión), elegidas por práctica y no por criterio estadístico. Es una primera lectura.
- **COAGUA no tiene evidencia para casi ninguna pregunta.** En la Ruta B, el resultado esperable es un perfil incompleto, y eso es un hallazgo.

## 5. Referencias

- Hribar Rajterič, I. (2010). Overview of business intelligence maturity models. *Management*, 15(1), 47–67. https://hrcak.srce.hr/53606
- Lahrmann, G., Wortmann, F., Marx, F. y Winter, R. (2011). Business intelligence maturity: Development and evaluation of a theoretical model. *Proceedings of the 44th Hawaii International Conference on System Sciences*. https://doi.org/10.1109/HICSS.2011.90
- Raber, D., Winter, R. y Wortmann, F. (2012). Using quantitative analyses to construct a capability maturity model for business intelligence. *Hawaii International Conference on System Sciences (HICSS-45)*. **Pendiente de verificación** (ver la sección 3).
- TDWI (2020). *Analytics Maturity Model Assessment Guide*. **Pendiente de verificación** (ver la sección 3).
- COSO (2013). *Internal Control – Integrated Framework*, principio 13: información relevante y de calidad.
