# Guía de discusión · La construcción de Watson

**Referencia:** Shih, W. (2012). *La construcción de Watson: ¡no tan elemental, querido!* Harvard Business School. *(El número de caso y las páginas están pendientes de verificación en el catálogo oficial.)*
**Unidad:** U4 · **RA:** RA3 · **Sesión:** S3, B2 (exposición + réplica)
**Acceso:** Biblioteca UEC. Esta guía no reproduce el texto del caso.

## Contexto para la discusión
El caso narra el desarrollo de un sistema de inteligencia artificial capaz de responder preguntas en lenguaje natural, y los desafíos de gestión de un proyecto de investigación de alto riesgo. Leído desde el aseguramiento, permite discutir qué puede y qué no puede hacer la IA, cómo se mide su desempeño y qué gobierno requiere.

## Preguntas
1. **Gestión del proyecto.** ¿Qué decisiones de organización y de gestión permitieron avanzar en un problema técnicamente incierto?
2. **Medición del desempeño.** ¿Cómo se medía si el sistema "funcionaba"? Relacione con la precisión y la exhaustividad de nuestras alertas.
3. **Confianza y calibración.** ¿Qué papel juega que el sistema estime su propia confianza en la respuesta? ¿Por qué es crítico para un auditor que use un modelo?
4. **De la demostración a la operación.** ¿Qué diferencia hay entre ganar una demostración pública y operar en un dominio regulado (salud, finanzas, auditoría)?
5. **Límites.** Con la lectura de la Royal Society (2017), identifique tres límites del aprendizaje automático que el caso ilustra o anticipa.
6. **Gobierno de la IA en el aseguramiento.** Si COAGUA quisiera usar un modelo para priorizar auditorías, ¿qué controles exigiría el comité: documentación, validación independiente, explicabilidad, supervisión humana?

## Producto del equipo expositor
Presentación de 15 minutos con una recomendación final: "¿Debería la auditoría interna de COAGUA usar IA para priorizar su plan? ¿Bajo qué condiciones?"

---

## Capa de enseñanza · Un modelo que prioriza auditorías

*Ejercicio propio del curso. Es ficticio y está ambientado en COAGUA: no forma parte del caso original, no lo cita y no atribuye nada a las organizaciones reales del caso.* **Uso en la exposición:** alimenta la recomendación final («¿Debería la auditoría interna de COAGUA usar IA para priorizar su plan?») y la pregunta 6 de la guía; el equipo de réplica la usa para su pregunta crítica.

**Escena.** Control Interno de COAGUA considera usar el puntaje de un modelo de detección de anomalías, como el visto en el curso, para decidir **qué revisar primero**. Elvira Montoya, presidenta del comité, pregunta: *«Si el modelo prioriza y se nos escapa algo, ¿quién responde?»*

| | **A. Solo reglas** | **B. El modelo decide el orden** | **C. El modelo sugiere; una persona decide y deja registro** |
|---|---|---|---|
| Qué es | Reglas de control declaradas, sin modelo | La lista del modelo es la agenda de auditoría | El modelo propone; Control Interno decide y documenta por qué |
| Fortaleza | Explicable | Encuentra lo inesperado | Combina descubrimiento y responsabilidad |
| Riesgo | Solo encuentra lo imaginado | Decisiones sin responsable; sesgos no vistos | Costo de la revisión humana |
| Consecuencia interna | Poco cambio | La responsabilidad se difumina | Exige un protocolo de uso y un monitoreo del modelo |

**Roles que chocan**
- **Rol A, Líder de analítica del equipo consultor:** responde por el modelo y por sus límites declarados.
- **Rol B, Jefa de Control Interno (Salcedo):** responde ante el comité y la revisoría por cada decisión de qué revisar y qué no.

**Microescenas**
— *Nota de la revisoría fiscal:* «Aceptamos el uso de modelos como apoyo si la decisión final es humana, está documentada y el modelo se puede explicar y vigilar».
— *Chat entre Poveda y Salcedo:* «¿Y si el modelo se equivoca con una regional?» «Por eso quiero ver qué mira y cuánto se equivoca antes de apoyarme en él».
— *Correo del líder de analítica:* «El modelo marca lo que marca, pero no sé qué deja sin marcar. Necesito compararlo con las reglas antes de recomendarlo como única fuente».

**Producto del equipo:** una **nota de uso del modelo** con: dominio de uso (para qué sí y para qué no), qué decide una persona, qué se documenta, cada cuánto se revisa y se recalibra el modelo, y cómo se detecta un sesgo por regional.

**Guía de evaluación**
- *Responsabilidad:* queda claro quién responde por cada decisión.
- *Límites:* se reconocen los falsos positivos y los casos que el modelo no ve.
- *Explicabilidad:* una regional entendería por qué su caso quedó en la lista.
- *Monitoreo:* hay una forma de saber si el modelo se degrada.

**Dos futuros.** *A) Apoyo con criterio:* el modelo ayuda a priorizar, Control Interno decide y documenta, y la revisoría lo acepta. *B) Piloto automático:* la lista se vuelve la agenda sin revisión, un sesgo regional pasa inadvertido y nadie asume la responsabilidad cuando se escapa un caso. ¿Qué señal temprana lo anticiparía?
