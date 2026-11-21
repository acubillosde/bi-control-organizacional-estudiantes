# Guía de discusión · Business Intelligence Software at SYSCO

**Referencia:** McAfee, A. y Wagonfeld, A. (2004). *Business Intelligence Software at SYSCO*. Harvard Business School. *(El número de caso y la autoría exacta están pendientes de verificar en el catálogo oficial de Harvard Business Publishing.)*
**Unidad:** U1 · **RA:** RA1 · **Sesión:** S1, B2 (25' en equipos + plenaria)
**Acceso:** Biblioteca UEC. Esta guía no reproduce el texto del caso.
**Si no se dispone del caso:** use el [caso ficticio de la Distribuidora Andina](caso_distribuidora_andina.md), escrito para este curso, con el mismo dilema y la misma estructura de preguntas.

## Contexto para la discusión
El caso presenta a una gran distribuidora de alimentos ante la decisión de adoptar software de inteligencia de negocios y definir su alcance. Es de 2004: léalo como **contexto histórico** de cómo se planteaba la inversión en BI antes de la nube, los modelos de autoservicio y el aprendizaje automático.

## Preguntas
1. **Problema de decisión.** ¿Qué decisión debe tomar la empresa? ¿Quién la toma y con qué criterios?
2. **Arquitectura.** Ubique en el caso los componentes de BI vistos en clase (fuentes, ETL, almacenamiento, informes). ¿Cuál parece el más débil?
3. **Valor.** ¿Cómo se justifica económicamente la inversión? ¿Qué beneficios son medibles y cuáles intangibles?
4. **Organización.** ¿Qué tensiones aparecen entre las unidades operativas y el nivel corporativo frente a la información? ¿Qué implicaciones tiene eso para el **control**?
5. **BI vs. BA.** ¿Las capacidades que se discuten son de BI, de BA o de ambas?
6. **Vigencia.** ¿Qué decisiones del caso serían distintas hoy? ¿Qué problema organizacional sigue igual?
7. **Transferencia.** Si COAGUA enfrentara una decisión similar, ¿qué tres preguntas haría el comité de auditoría antes de aprobarla?

## Producto
Respuestas a las preguntas 1, 4 y 7 (media página por equipo). Se discuten en plenaria junto con el [caso DIARI](caso_diari_contraloria.md).

---

## Capa de enseñanza · ¿Qué hace COAGUA con el tablero cuando termine el curso?

*Ejercicio propio del curso. Es ficticio y está ambientado en COAGUA: no forma parte del caso original, no lo cita y no atribuye nada a las organizaciones reales del caso.* Sirve igual para este caso y para la [Distribuidora Andina](caso_distribuidora_andina.md). **Uso:** amplía la pregunta 7. Con tiempo, los equipos resuelven esto en vez de listar tres preguntas.

**Escena.** Han pasado siete semanas. El comité de auditoría de COAGUA vio el tablero y quiere que siga vivo cuando el equipo consultor se vaya. Andrés Poveda, el gerente general, lo resume: *«Si el tablero vive en el computador de una persona, el día que esa persona se vaya volvemos a la carpeta»*. Hay tres caminos.

| | **A. Un analista interno** | **B. Almacén corporativo en Tecnología** | **C. Servicio gestionado en la nube** |
|---|---|---|---|
| Qué es | Una persona de COAGUA mantiene el archivo del tablero | Tecnología aloja los datos y el modelo y los actualiza | Un proveedor externo aloja y actualiza, con cobro por usuario |
| Fortaleza | Barata y rápida de arrancar | Gobierno claro; Tecnología es custodio | Rápida; menos carga para Tecnología |
| Riesgo | Depende de una persona; poco rastro de cambios | Tiempos de respuesta; Tecnología como cuello de botella | Datos fuera del perímetro; dependencia del proveedor |
| Consecuencia interna | Control Interno carga con una tarea que no es suya | Cambia el equilibrio entre Tecnología y los dueños del dato | Exige un contrato y reglas de acceso; Jurídica entra al proyecto |

**Roles que chocan**
- **Rol A, Gerente general (Poveda):** decide qué opción financiar y qué exige a cambio. Responde por la inversión y por que se use.
- **Rol B, Jefa de Control Interno (Clara Inés Salcedo):** fija las condiciones de control sin las cuales no firmará: rastro de cambios, quién modifica las medidas, quién ve qué.

**Microescenas**
— *Correo de Poveda a Tecnología y Control Interno:* «No quiero comprar nada que nadie use. Díganme cuánto cuesta, quién lo mantiene y cómo sabremos en seis meses que se usa».
— *Chat entre Mauricio Rendón (Tecnología) y Salcedo:* «Eso lo mantenemos nosotros en el servidor». «¿Y cómo queda el rastro de quién cambió una fórmula y cuándo?»
— *Nota del comité:* «Un informe crítico que solo una persona sabe actualizar es un riesgo operativo. Queremos saber cómo se evita».

**Producto del equipo:** una tabla comparativa de A, B y C con cinco criterios (costo anual, dependencia de personas, control de cambios, seguridad y acceso por rol, adopción medible); la opción que recomiendan con **tres condiciones medibles**; y las **tres preguntas** que haría el comité antes de aprobar.

**Guía de evaluación**
- *Coherencia* entre la opción recomendada y los criterios.
- *Gobierno:* quién es dueño del dato y quién es custodio.
- *Adopción:* cómo se mide el uso, no solo el costo.
- *Control:* trazabilidad de cambios y reglas de acceso.

**Dos futuros.** *A) Tablero vivo:* tiene dueño del dato, control de cambios y medición de uso; a los seis meses el comité lo abre cada mes. *B) Tablero huérfano:* nadie lo actualiza, las cifras dejan de coincidir con la contabilidad y vuelven los archivos por correo. ¿Qué señales del primer mes distinguirían uno de otro?
