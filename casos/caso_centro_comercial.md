# Guía de discusión · Madurez de BI en un centro comercial

**Referencia:** Ramírez-Angulo, P. J. y Chaparro-Guevara, R. A. (2020). Business intelligence readiness assessment for a shopping mall: Challenges and future directions. *Journal of Cases on Information Technology*, 22(2), 18–33. https://doi.org/10.4018/JCIT.2020040102
**Unidad:** U2 · **RA:** RA2, RA3 · **Sesión:** S2, B2 (exposición + réplica)
**Acceso:** Biblioteca UEC. Esta guía no reproduce el texto del caso.

## Contexto para la discusión
Es un caso de enseñanza sobre un centro comercial en Colombia que, antes de implementar prácticas de BI, evalúa su preparación (*readiness*) en procesos, personas y tecnología, y construye un modelo de etapas de madurez para priorizar acciones con un presupuesto limitado.

## Preguntas
1. **Método.** ¿Cómo se evaluó la preparación? ¿Qué fuentes de información se usaron y qué sesgos podrían tener?
2. **Diagnóstico.** ¿En qué etapa de madurez quedó la organización y por qué? ¿Cuál de las tres dimensiones (procesos, personas, tecnología) limitaba más?
3. **Gobierno y calidad.** ¿Qué problemas de gobierno o de calidad de datos identifica en el caso o puede inferir?
4. **Priorización.** Con un presupuesto limitado, ¿qué tres acciones priorizaría y en qué orden? Justifique con el marco de Pauwels et al. (2009) sobre el desarrollo de dashboards.
5. **Control organizacional.** ¿Qué indicadores de control podría monitorear la administración del centro comercial una vez alcance la siguiente etapa de madurez?
6. **Transferencia.** Evalúe la madurez de BI de COAGUA (o de su propia organización) con las mismas dimensiones. ¿En qué etapa está?

## Producto del equipo expositor
Presentación de 15 minutos: contexto (2'), diagnóstico (4'), análisis con un marco del curso (4'), recomendación priorizada (3') y lección para COAGUA (2').

## <a id="debrief"></a>Debrief del diagnóstico de madurez (15 minutos)

Después de la exposición, el grupo contrasta el modelo formal del caso con el instrumento que usted aplicó en la [actividad de diagnóstico de madurez de BI con evidencia](../unidad-1/actividad_madurez_bi/README.md) (U1).

| Min | Paso | Qué se hace |
|---:|---|---|
| — | **Antes del S2** | Con su entrega de la actividad, complete el **formulario anónimo** que publica el docente: los cuatro puntajes por dimensión de la Ruta A (sin el nombre de su organización) y el sector. Quien hizo la Ruta B no lo llena |
| 3 | **Agregado de la cohorte** | El docente presenta el promedio y la dispersión por dimensión y cuál fue la dimensión limitante más frecuente |
| 5 | **Contraste con el modelo formal** | ¿Qué dimensión o criterio del modelo del centro comercial no estaba en nuestro instrumento? ¿Y al revés? |
| 4 | **Metacognición** | ¿Qué cambió en su calificación cuando se exigió evidencia? |
| 3 | **Cierre** | ¿Por qué el eslabón más débil define la confiabilidad del tablero? |

---

## Capa de enseñanza · ¿Qué primero, con presupuesto limitado?

*Ejercicio propio del curso. Es ficticio y está ambientado en COAGUA: no forma parte del caso original, no lo cita y no atribuye nada a las organizaciones reales del caso.* **Uso en la exposición:** alimenta la *recomendación priorizada* (3') y la *lección para COAGUA* (2') del equipo expositor; el equipo de réplica la usa para su pregunta crítica.

**Escena.** Andrés Poveda asigna **120 millones de pesos** para fortalecer la capacidad de datos de COAGUA el próximo año. No alcanza para todo y cada área tiene un candidato:

| | **A. Gobierno y calidad del dato maestro** | **B. Formación y adopción de usuarios** | **C. Tecnología: almacén y automatización** |
|---|---|---|---|
| Qué incluye | Dueños del dato, reglas de calidad, glosario de indicadores | Formación a gerentes y analistas y acompañamiento | Almacén de datos y cargas automáticas |
| Costo | 45 millones | 30 millones | 110 millones |
| Dimensión del modelo | Procesos | Personas | Tecnología |

Solo caben **A y B (75 millones)** o **C solo (110 millones)**.

**Roles que chocan**
- **Rol A, Gerente de Riesgos (Julián Barrera):** quiere A. «Sin dueño del dato, la mejor plataforma solo acelera los errores».
- **Rol B, Director de Tecnología (Mauricio Rendón):** quiere C. «Sin automatización, cada informe depende de que alguien se acuerde».

**Microescenas**
— *Correo de Diana Peña (Finanzas):* «Con 120 millones no hago milagros. Díganme qué se aplaza y qué evidencia tienen de que ese orden es el correcto».
— *Nota de Gestión Humana:* «Los gerentes quieren aprender, pero no tienen tiempo los lunes; sin tiempo protegido, la formación no se usa».
— *Chat entre Salcedo (Control Interno) y Rendón:* «Si compras tecnología sin reglas de calidad, ¿cómo sé qué cifra es la buena?»

**Producto del equipo:** un diagnóstico de COAGUA con las **mismas dimensiones del modelo del caso** y la evidencia disponible, marcando **«no verificable»** lo que no se pueda comprobar (como en la actividad de diagnóstico de madurez, Profundización A); y una **priorización de tres acciones** con orden y justificación, usando el marco de Pauwels et al. (2009), con un indicador de avance para la primera.

**Guía de evaluación**
- *Evidencia:* el diagnóstico no afirma lo que no puede verificar.
- *Priorización:* se explica por qué se aplaza lo que se aplaza.
- *Coherencia* con el presupuesto (A y B, o C).
- *Eslabón más débil:* se identifica la dimensión que limita a las demás.

**Dos futuros.** *A) Orden correcto:* el gobierno del dato llega antes que la tecnología y el almacén se alimenta de datos confiables. *B) Tecnología sin dueño:* se instala, nadie confía en las cifras y los usuarios vuelven a sus archivos. ¿Qué indicador del primer trimestre lo anticiparía?
