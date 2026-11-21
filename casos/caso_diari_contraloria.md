# Guía de discusión · DIARI: analítica de datos para el control fiscal en Colombia

**Propósito:** complementar el caso SYSCO (2004) con un caso colombiano actual y verificable de uso de datos para el control.
**Unidad:** U1 (y anticipa U2 y U4) · **RA:** RA1, RA2 · **Sesión:** S1, B2

## Fuentes (de acceso abierto)
- OCDE (2021). *El control preventivo y concomitante de la Entidad Fiscalizadora Superior de Colombia*. OECD Publishing. Capítulo sobre la Dirección de Información, Análisis y Reacción Inmediata (DIARI). Según este informe, la DIARI tiene unidades de información, de análisis y de reacción inmediata, y la de análisis usa, entre otras, técnicas de big data para identificar riesgos para el patrimonio público.
- Normativa de contexto: reforma del control fiscal (Acto Legislativo 04 de 2019) y reestructuración de la Contraloría General de la República (Decreto 2037 de 2019, según fuentes secundarias). **Pendiente de verificación** de los números y del alcance en el texto oficial.

> El docente debe verificar, antes de la sesión, la vigencia de la estructura y del nombre de la dependencia en el sitio oficial de la Contraloría. Una fuente periodística de 2025 usa una denominación distinta.

## Contexto para la discusión
La Contraloría General de la República creó una dependencia dedicada a integrar fuentes de datos públicas, analizarlas y generar alertas tempranas sobre riesgos para los recursos públicos. A diferencia de SYSCO, el objetivo no es comercial sino de **control**. Además, opera dentro de un marco legal que define qué puede hacer con las alertas (control preventivo y concomitante, sin coadministración).

## Preguntas
1. **Arquitectura.** Dibuje el flujo de la DIARI con los componentes de BI vistos en clase: fuentes, integración, análisis, alerta y reacción.
2. **BI y BA.** ¿Qué parte del trabajo es BI (consolidar e informar) y qué parte es BA (detectar y anticipar)?
3. **Gobierno de datos.** ¿Qué problemas de calidad, interoperabilidad y protección de datos personales enfrenta un sistema que cruza bases de varias entidades?
4. **Límites.** ¿Qué riesgo hay en que una alerta analítica se interprete como prueba de un detrimento? ¿Cómo se relaciona con la diferencia entre señal y evidencia que veremos en U4?
5. **Comparación con SYSCO.** ¿Qué cambió en 20 años (tecnología, volumen, regulación) y qué sigue igual (patrocinio, adopción, cultura)?
6. **Transferencia al sector privado.** ¿Qué elementos del modelo de la DIARI podría adoptar la auditoría interna de COAGUA?

## Producto
Respuestas a las preguntas 1, 4 y 6 (media página por equipo).

---

## Capa de enseñanza · Una alerta, ¿y después?

*Ejercicio propio del curso. Es ficticio y está ambientado en COAGUA: no forma parte del caso original, no lo cita y no atribuye nada a las organizaciones reales del caso.* **Uso:** amplía la pregunta de transferencia a COAGUA. La DIARI muestra un sistema donde la alerta activa una acción de control; aquí se diseña ese protocolo para COAGUA.

**Escena (hipotética).** Imaginen que, dentro de unos meses, el tablero de COAGUA genera una alerta sobre una regional cualquiera (para el ejercicio, el Meta). La alerta no dice que haya una irregularidad: dice que algo merece una pregunta. Al mismo tiempo, una entidad externa pide los datos para un análisis conjunto. Clara Inés Salcedo, jefa de Control Interno, tiene que decidir **qué hacer, en qué orden y con quién**.

| | **A. Escalar de inmediato** | **B. Revisión interna primero** | **C. Revisión interna con consulta escalonada** |
|---|---|---|---|
| Qué es | La alerta va al comité el mismo día | Control Interno revisa 10 días hábiles antes de escalar | Revisión interna, consulta confidencial a la regional y escalamiento según la gravedad |
| Fortaleza | Transparencia total | Evita falsas alarmas | Equilibra rapidez, justicia y evidencia |
| Riesgo | Se acusa sin evidencia; la regional se entera por terceros | Se retrasa lo grave; sospecha de encubrimiento | Complejidad; exige criterios escritos de gravedad |
| Consecuencia interna | Las regionales dejan de colaborar | El comité pierde confianza en la oportunidad | Requiere un protocolo y su cumplimiento |

**Roles que chocan**
- **Rol A, Jefa de Control Interno (Salcedo):** quiere actuar a tiempo y con evidencia.
- **Rol B, Asesora jurídica (Paola Ibáñez):** responde por que lo que se comparta y lo que se escale cumpla con la protección de datos personales y con el debido proceso interno.

**Microescenas**
— *Correo de la presidenta del comité, Elvira Montoya:* «¿Esto es un hallazgo o una alerta? No quiero enterarme por un rumor y tampoco por una acusación».
— *Nota jurídica:* «Compartir datos con un externo exige una finalidad concreta, un acuerdo escrito y el mínimo de datos. No se comparte lo que no se necesita para el análisis».
— *Chat entre Salcedo y Ruth Mery Cuéllar, gerente regional (ejercicio):* «Antes de que lo vea el comité quiero entender si hay una explicación». «Gracias por avisarme. ¿Qué necesitas de mí?»

**Producto del equipo:** un **protocolo de una página** con estados (abierta, en revisión, cerrada), plazos, evidencia mínima, criterio de cierre, quién informa a quién y reglas para compartir datos con terceros.

**Guía de evaluación**
- *Distinción* entre alerta, hallazgo y conclusión.
- *Debido proceso:* la regional es informada y puede explicar antes de ser señalada.
- *Datos personales:* finalidad, mínimo necesario y acuerdo escrito.
- *Operatividad:* plazos y responsables que Control Interno pueda cumplir.

**Dos futuros.** *A) Confianza:* el protocolo se cumple, las alertas se cierran en plazo y las regionales colaboran. *B) Desgaste:* las alertas no tienen dueño, una filtra a un tercero, las regionales se ponen a la defensiva y el comité desconfía. ¿Qué señales del primer mes distinguirían uno de otro?
