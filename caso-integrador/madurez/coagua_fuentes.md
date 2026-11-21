# Ruta B · COAGUA: contexto y catálogo de fuentes para el diagnóstico de madurez

**Se usa en:** [Actividad de diagnóstico de madurez de BI con evidencia](../../unidad-1/actividad_madurez_bi/README.md), Ruta B, y en el [diagnóstico rápido y plan de transformación del L1](../../unidad-1/actividad_madurez_bi/plan_transformacion.md) (S1).

Este archivo hace dos cosas: resume lo que el repositorio dice de COAGUA (ficha de contexto) y lista qué materiales **podrían** servir de evidencia para cada pregunta del instrumento. Además del enunciado y los datos, hay un **[expediente de COAGUA](expediente_coagua.md)** con ocho documentos internos ficticios (E1 a E8), que se usa en la semana 2. **No califica nada por usted.** Qué puntaje merece cada pregunta, con qué tipo de evidencia y con qué confianza es su juicio.

> **Todo es ficticio.** COAGUA y sus datos son sintéticos. No atribuya hallazgos a entidades reales.

## 1. Ficha de contexto de COAGUA

Tomada del [enunciado del caso integrador](../README.md) y de [`datos/README.md`](../../datos/README.md). No hay otra información sobre COAGUA en el repositorio.

| Aspecto | Lo que dicen los materiales |
|---|---|
| Qué es | Cooperativa de ahorro y crédito orientada a productores agropecuarios (la narrativa la llama *Cooperativa Agrofinanciera Los Guaduales*) |
| Sede y presencia | Bogotá D.C., con oficinas en Meta, Huila, Tolima, Córdoba, Casanare, Risaralda y Cauca |
| Tamaño | 60 empleados, alrededor de 180 proveedores, una cartera de 3.200 créditos |
| 2025 | Creció rápido: abrió oficinas, contrató proveedores nuevos de servicios profesionales y tecnología, y su sistema de pagos pasó de aprobaciones en papel a un flujo digital |
| Gobierno | Tiene un **comité de auditoría** del consejo de administración, una **revisoría fiscal** y una **gerencia de riesgos** |
| Origen del encargo | El comité de auditoría recibió dos comunicaciones (el texto está en el [enunciado del caso](../README.md)) y contrató a su equipo para diseñar un tablero de control interno en Power BI |
| Datos disponibles | Los conjuntos sintéticos de [`datos/`](../../datos/README.md) |
| Documentos internos | El [expediente de COAGUA](expediente_coagua.md) (E1 a E8), ficticio |

**Qué no dicen el enunciado ni los datos:** cómo se integran las fuentes, quién es el dueño de cada dato, si hay glosarios o catálogos de indicadores, cómo se atienden los requerimientos de información, quién usa los informes ni qué presupuesto tiene BI. **Eso lo responde el [expediente](expediente_coagua.md)**, sin decir nada sobre el contenido de los datos. En el **S1**, el diagnóstico rápido se hace *sin* el expediente (con el enunciado y este catálogo), así que allí casi todo será NV.

## 2. Qué no es evidencia de COAGUA

La Ruta B pide evidencia de **la capacidad de COAGUA**, no de la suya. No sirven como evidencia:

| Material | Por qué no sirve |
|---|---|
| Su ETL de Power Query (T1, Avance 1) | Es lo que **usted** construyó. No muestra cómo produce COAGUA sus datos |
| Su modelo estrella, sus medidas DAX y sus tableros (L2, T2, Avance 2) | Es su trabajo en el curso, no un modelo corporativo de COAGUA |
| Su perfilado de calidad y sus tablas de excepciones (L1 parte 2 y la extensión opcional de la profundización A) | Mide los datos con su método; no prueba que COAGUA mida su calidad |
| Los resultados de analizar `pagos.csv`, `creditos.csv` u otros | Son hallazgos del caso integrador. **Esta actividad no debe afirmar ni sugerir nada sobre irregularidades en los datos** (si existen, cuántas ni de qué tipo) |
| La guía del caso del centro comercial y los demás casos de discusión | Son otras organizaciones |
| Lo que le contó un compañero, o lo que usted supone | No es evidencia: es testimonio sin fuente (T, y de otra persona) |

## 3. Catálogo de fuentes del repositorio

Cada fuente se describe por lo que **contiene**, no por lo que usted debería concluir de ella.

| # | Fuente (ruta) | Qué contiene | Preguntas a las que podría aportar | Límite |
|---|---|---|---|---|
| F1 | [`caso-integrador/README.md`](../README.md) | Narrativa del caso: tamaño, crecimiento en 2025, tránsito de aprobaciones en papel a flujo digital, órganos de gobierno, origen del encargo | Contexto de **D4.3** (quién patrocina el proyecto de tablero); contexto de **D2.1** (existe un flujo digital de pagos) | Es una narración del caso. No menciona presupuesto, plan estratégico ni cómo se integran las fuentes |
| F2 | [`datos/README.md`](../../datos/README.md) | Descripción de los conjuntos de datos: tablas, campos y notas | Contexto de **D2.1** (qué entidades de datos existen por separado) | Documenta los conjuntos del curso. No es un diagrama de arquitectura ni un diccionario corporativo de COAGUA |
| F3 | [`datos/integrador/limites_aprobacion.csv`](../../datos/integrador/limites_aprobacion.csv) y [`politica_lineas_credito.csv`](../../datos/integrador/politica_lineas_credito.csv) | Políticas (ficticias) con topes: atribuciones de aprobación por cargo y topes y tasas por línea de crédito | Contexto de **D3.3** (la organización formaliza reglas con umbrales) | Son políticas de control, **no indicadores de BI**. No dicen quién los monitorea ni si hay tablero |
| F4 | [`datos/profundizacion/clientes_maestro.csv`](../../datos/profundizacion/clientes_maestro.csv) | Maestro de clientes con datos personales | Contexto de **D1.3** y de la bandera **B2** (existen datos personales que gobernar) | Muestra que hay datos personales. No muestra roles, política de tratamiento ni controles de acceso |
| F5 | [E1 · Glosario de indicadores de Finanzas](expediente_coagua.md#e1--glosario-de-indicadores-de-finanzas) | Glosario de una sola área, con fecha, versión y responsable | **D1.1**, banderas **B3** | Es de un área, no del conjunto de la cooperativa. Revise la vigencia y el responsable |
| F6 | [E2 · Mapa de sistemas](expediente_coagua.md#e2--mapa-de-sistemas-de-coagua) | Sistemas, quién los mantiene y cómo llega la información a los informes | **D2.1**, **D2.3**, **D1.3** | Es una vista de 2024; no describe cargas automáticas ni modelos |
| F7 | [E3 · Bitácora del cierre mensual](expediente_coagua.md#e3--bitácora-del-cierre-mensual-de-informes-últimos-tres-meses) | Fechas, pasos y responsable del cierre de tres meses, con notas del analista | **D2.2**, **D3.1**, **D1.2** (por ausencia), **B1** | Lo que no aparece (una validación) no prueba que no exista |
| F8 | [E4 · Fichas de indicadores](expediente_coagua.md#e4--fichas-de-indicadores) | Fórmula, meta, umbral y responsable de tres indicadores | **D3.3** | Son tres indicadores, no todos |
| F9 | [E5 · Acta del comité de auditoría](expediente_coagua.md#e5--extracto-del-acta-del-comité-de-auditoría) | Lo que el comité decidió y cómo hace seguimiento | **D4.1**, **D4.3** | Es un extracto de una sesión |
| F10 | [E6 · Registro de solicitudes](expediente_coagua.md#e6--registro-de-solicitudes-de-información-hoja-compartida) | Cuatro solicitudes con canal, fechas y quién atendió | **D3.2**, **D4.2** (solo como testimonio) | Es una muestra de un semestre. El mensaje del regional es un testimonio (T) |
| F11 | [E7 · Política de datos personales](expediente_coagua.md#e7--política-de-tratamiento-de-datos-personales-extracto) | Extracto de la política: custodia, finalidad y alcance | **D1.3** | No muestra su aplicación |
| F12 | [E8 · Correo de la Gerencia](expediente_coagua.md#e8--correo-de-la-gerencia-general-al-comité) | Una afirmación de la gerencia al comité | Ninguna como evidencia: es un **testimonio (T)** | Contrástelo con los documentos antes de usarlo |

**Cómo usar una fuente como evidencia:** descríbala en la matriz con su tipo (casi todo lo anterior es tipo **D**, documento), nombre genérico y fecha. Pregúntese siempre: ¿esto prueba **la capacidad que pregunta el instrumento**, o solo da contexto? Si solo da contexto, no alcanza para una calificación mayor a 3.

## 4. Mapa de preguntas

«**Sin fuente**» significa que ningún material del repositorio contiene la evidencia aceptable que pide el instrumento: la respuesta honesta es **NV** (con la evidencia que haría falta). «**Solo por ausencia o testimonio**» significa que lo único que hay no alcanza para una calificación alta: una ausencia no prueba nada y un testimonio (T) da, como máximo, un 3 con confianza baja. **El mapa dice dónde buscar; no dice qué puntaje merece cada pregunta.**

| Cód. | Pregunta | ¿Hay fuente? | Fuentes |
|---|---|---|---|
| D1.1 | ¿Los indicadores clave tienen definición única y dueño? | Sí, en el expediente | F5 |
| D1.2 | ¿Se mide la calidad de los datos críticos? | Solo por ausencia o testimonio | F7 |
| D1.3 | ¿Dueño y custodio del dato y protección de datos personales? | Sí, en el expediente | F11, F6 (contexto: F4) |
| D2.1 | ¿Cómo se integran las fuentes? | Sí, en el expediente | F6, F7 (contexto: F1, F2) |
| D2.2 | ¿El procedimiento que produce el dato lo puede repetir otra persona? | Sí, en el expediente | F7 |
| D2.3 | ¿Existe un modelo compartido y seguridad por rol? | Sí, en el expediente | F6 |
| D3.1 | ¿Cuánto tarda en estar disponible la información de un proceso crítico? | Sí, en el expediente | F7 |
| D3.2 | ¿Cómo se gestionan los requerimientos de información? | Sí, en el expediente | F10 |
| D3.3 | ¿Los indicadores tienen fórmula, meta, umbral y responsable? | Sí, en el expediente | F8 (contexto: F3) |
| D4.1 | ¿Se documentan decisiones apoyadas en los informes? | Sí, en el expediente | F9 |
| D4.2 | ¿Los usuarios usan y entienden los datos? | Solo por ausencia o testimonio | F10 |
| D4.3 | ¿Hay patrocinio con presupuesto? | Sí, en el expediente | F9 (contexto: F1) |
| B1 | Informes críticos que solo una persona sabe actualizar | Sí, en el expediente | F7 |
| B2 | Archivos con datos personales por correo | **Sin fuente** | — |
| B3 | Un indicador con cifras distintas entre áreas | Solo por ausencia o testimonio | F5 |
| B4 | Cambios a fórmulas o consultas sin rastro | **Sin fuente** | — |

**El expediente se usa en la semana 2.** En el S1, el diagnóstico rápido se hace con el enunciado y este catálogo, **sin** el expediente, así que casi todo será NV. Con el expediente, la mayoría de las preguntas tiene evidencia, y hay que **leerla con cuidado**: fíjese en la vigencia, en quién firma y en la diferencia entre lo que alguien dice y lo que un documento muestra. Una dimensión con 2 o 3 preguntas NV se declara «perfil incompleto».

## 5. Cómo escribir una NV útil

Una buena NV dice **qué pregunta**, **a quién** y **qué documento o acceso la resolvería**. Compare:

| Floja | Mejor |
|---|---|
| «No hay información» | «Pregunta al gerente de tecnología: ¿existe un diagrama de cómo llegan los datos del sistema de pagos al tablero? Evidencia que pediría: el diagrama de arquitectura y el calendario de cargas, con la fecha de la última ejecución» |
| «Habría que investigar» | «Pregunta al jefe de control interno: ¿quién es el responsable de cada indicador del tablero? Evidencia que pediría: la ficha de cada indicador con fórmula, meta y responsable» |

Son modelos de redacción. Escriba las suyas, ajustadas a la pregunta del instrumento y a la evidencia que de verdad falta.
