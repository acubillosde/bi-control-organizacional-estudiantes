# Plantilla · Diagnóstico de madurez de BI con evidencia

**Versión de Excel con cálculo automático: [`plantilla_diagnostico.xlsx`](plantilla_diagnostico.xlsx).** Descárguela y complete las celdas amarillas: calcula sola el perfil por dimensiones, los NV, el «perfil incompleto» y la dimensión limitante, dibuja el radar y marca en rojo lo que incumple las reglas de evidencia. Esta versión en texto sirve de referencia.

Copie este archivo, complételo y expórtelo a PDF (máximo **3 páginas**). Las instrucciones en cursiva se borran al entregar. La guía completa está en el [README de la actividad](README.md).

---

## 1. Ficha de alcance

| Campo | Su respuesta |
|---|---|
| Ruta | A (organización propia) / B (COAGUA) |
| Organización | *Nombre, o «Entidad A» si anonimiza* |
| Unidad, gerencia o proceso evaluado | *Ruta B: COAGUA completa* |
| Sector | |
| Tamaño (por rangos) | *Por ejemplo: menos de 50, 50–250, más de 250 empleados* |
| Su rol | *Ruta B: consultor de analítica para el control* |

## 2. Matriz de diagnóstico

*Puntaje: 1 a 5, o **NV**. Tipo de evidencia: D, S, O o T (si hay varias, escriba la de mayor peso primero). Confianza: A, M o B. Recuerde: más de 3 exige D o S.*

*Qué significan las siglas (se borra al entregar):*

| Columna | Sigla | Significa |
|---|---|---|
| **Puntaje** | 1 a 5 | Nivel que describe lo que usted **verificó**, según las anclas del instrumento |
| | **NV** | **No verificable:** no hay evidencia. No se promedia; anote en la sección de pendientes qué evidencia haría falta |
| **Tipo** (de dónde viene la evidencia) | **D** | **Documento:** política, manual, glosario, diagrama, acta o reporte |
| | **S** | **Sistema:** usted vio funcionar el sistema, el modelo o el tablero, o tiene acceso a él |
| | **O** | **Observación directa** de un proceso en operación |
| | **T** | **Testimonio:** alguien se lo dijo |
| **Confianza** (qué tan sólida es la evidencia) | **A** | **Alta:** evidencia D o S vigente |
| | **M** | **Media** |
| | **B** | **Baja:** solo testimonio (T) |

*Orden de peso de la evidencia: D y S pesan más que O, y O más que T. Con solo O o T, el puntaje máximo es 3.*

| Cód. | Pregunta | Puntaje | Tipo | Descripción de la evidencia (tipo, nombre genérico, fecha, quién la mantiene) | Confianza |
|---|---|:-:|:-:|---|:-:|
| D1.1 | ¿Los indicadores clave tienen definición única y dueño? | | | | |
| D1.2 | ¿Se mide la calidad de los datos críticos? | | | | |
| D1.3 | ¿Están definidos dueño y custodio del dato y la protección de datos personales? | | | | |
| D2.1 | ¿Cómo se integran las fuentes? | | | | |
| D2.2 | ¿El procedimiento que produce el dato lo puede repetir otra persona? | | | | |
| D2.3 | ¿Existe un modelo compartido y seguridad por rol? | | | | |
| D3.1 | ¿Cuánto tarda en estar disponible la información de un proceso crítico? | | | | |
| D3.2 | ¿Cómo se gestionan los requerimientos de información? | | | | |
| D3.3 | ¿Los indicadores tienen fórmula, meta, umbral y responsable? | | | | |
| D4.1 | ¿Se documentan decisiones apoyadas en los informes? | | | | |
| D4.2 | ¿Los usuarios usan y entienden los datos? | | | | |
| D4.3 | ¿Hay patrocinio con presupuesto? | | | | |

**Si puso un 2 o un 4,** justifique entre qué anclas está:

> *(una línea por cada 2 o 4)*

**Preguntas NV** *(obligatorio para cada NV)*

| Cód. | Qué evidencia haría falta | Ruta B: pregunta al gerente de COAGUA |
|---|---|---|
| | | |

**Banderas de riesgo de control** *(sí / no / no sé, con una línea de evidencia; no entran al promedio)*

| Cód. | Bandera | Respuesta | Evidencia |
|---|---|:-:|---|
| B1 | ¿Hay informes críticos en hojas de cálculo que solo una persona sabe actualizar? | | |
| B2 | ¿Circulan por correo archivos con datos personales o sensibles? | | |
| B3 | ¿Un mismo indicador tiene cifras distintas entre áreas? | | |
| B4 | ¿Los cambios a fórmulas o consultas críticas quedan sin rastro? | | |

## 3. Perfil por dimensiones

| Dimensión | Preguntas | Puntaje | N.º de NV | ¿Perfil incompleto? |
|---|---|:-:|:-:|:-:|
| 1. Datos y gobierno | D1.1–D1.3 | | | |
| 2. Arquitectura y tecnología | D2.1–D2.3 | | | |
| 3. Procesos y entrega | D3.1–D3.3 | | | |
| 4. Cultura y uso | D4.1–D4.3 | | | |

**Dimensión limitante:** *(la de menor puntaje)*

*Opcional: gráfico de radar con los cuatro puntajes. No calcule un nivel global promedio.*

### Cómo calcularlo en Excel
Copie los puntajes de la matriz a una hoja, con una fila por pregunta. Si el puntaje es NV, escriba el texto `NV` en la celda: las funciones de promedio **ignoran el texto**, así que las NV quedan fuera del promedio sin más pasos.

| Qué | Fórmula (Excel en español) | Fórmula (Excel en inglés) |
|---|---|---|
| Puntaje de la dimensión 1 (celdas C2:C4) | `=SI.ERROR(PROMEDIO(C2:C4);"sin datos")` | `=IFERROR(AVERAGE(C2:C4),"sin datos")` |
| N.º de NV de la dimensión 1 | `=CONTAR.SI(C2:C4;"NV")` | `=COUNTIF(C2:C4,"NV")` |
| ¿Perfil incompleto? | `=SI(CONTAR.SI(C2:C4;"NV")>=2;"Sí";"No")` | `=IF(COUNTIF(C2:C4,"NV")>=2,"Yes","No")` |
| Dimensión limitante (puntajes en F2:F5, nombres en A2:A5) | `=INDICE(A2:A5;COINCIDIR(MIN(F2:F5);F2:F5;0))` | `=INDEX(A2:A5,MATCH(MIN(F2:F5),F2:F5,0))` |

*Si una dimensión quedó con las tres preguntas en NV, la fórmula del puntaje devuelve «sin datos»: no puede ser la dimensión limitante y debe declararse perfil incompleto. Si su Excel usa coma como separador de argumentos, use las fórmulas en inglés o reemplace `;` por `,`.*

## 4. Análisis (máximo 200 palabras)

*Incluya:*
1. *la dimensión limitante y por qué define la confiabilidad del tablero;*
2. *el riesgo de control concreto que genera, con referencia al **principio 13 de COSO 2013** (información relevante y de calidad);*
3. *una acción realizable en 90 días, con responsable.*

> 

## 5. Declaración de confidencialidad *(solo Ruta A)*

> *Una frase. Por ejemplo:* «Declaro que este documento no reproduce documentos, cifras ni datos personales de la organización evaluada, y que la evidencia se describe sin transcribirla».

## Lista de verificación antes de entregar
- [ ] Todo puntaje mayor a 3 tiene evidencia tipo D o S.
- [ ] Cada NV tiene la evidencia que haría falta (y, en la Ruta B, la pregunta al gerente).
- [ ] No calculé un nivel global promedio.
- [ ] El análisis tiene 200 palabras o menos y propone una acción a 90 días.
- [ ] Ruta A: no adjunté ni transcribí documentos ni datos de la organización.
- [ ] Ruta B: usé solo fuentes del repositorio y no afirmé nada sobre irregularidades en los datos.
- [ ] El PDF tiene 3 páginas o menos.
