# Actividades · Unidad 2

## <a id="pa"></a>PA · Profundización A: diagnóstico de madurez de BI con evidencia (semana 2, 2.75 h, individual, 2%)

**RA:** RA1, RA2 · **Fecha límite:** sábado de la semana 2 · **Guía completa:** [actividad de diagnóstico de madurez de BI con evidencia](../unidad-1/actividad_madurez_bi/README.md) · **Rúbrica:** [R6](../evaluacion/rubricas.md#r6-diagnóstico-de-madurez-de-bi-con-evidencia)

Diagnostique la madurez de BI de una organización con evidencia verificable y no con percepción: 4 dimensiones, 12 preguntas, reglas de evidencia (documento, sistema, observación, testimonio; más de 3 exige documento o sistema) y «no verificable» cuando no se puede comprobar. Hay dos rutas: su organización (Ruta A) o COAGUA con las fuentes del curso (Ruta B, [catálogo de fuentes](../caso-integrador/madurez/coagua_fuentes.md)).

1. **Instrumento (45 min):** lea las 12 preguntas y sus anclas.
2. **Evidencia (75 min):** busque y describa la evidencia de cada pregunta.
3. **Redacción (45 min):** matriz, perfil por dimensiones y análisis de 200 palabras.

**Entregable:** PDF de máximo 3 páginas (ficha de alcance, matriz, perfil, análisis y, en la Ruta A, declaración de confidencialidad) y el formulario anónimo con sus puntajes por dimensión (Ruta A). Se comenta en el [debrief del S2](../casos/caso_centro_comercial.md#debrief).

### Extensión opcional (sin nota): calidad y gobierno del maestro de clientes
Era la profundización A en versiones anteriores del curso. Se conserva para quien quiera practicar el perfilado de un dato maestro con datos personales. **No tiene entrega ni nota.**

Esta actividad **no repite** el laboratorio L1: allí se perfilaron transacciones; aquí se evalúa un **dato maestro** con datos personales y se propone su gobierno.

1. **Perfilado (1 h).** En Power Query, mida para cada dimensión al menos un indicador:

   | Dimensión | Indicador sugerido |
   |---|---|
   | Completitud | % de emails y teléfonos vacíos |
   | Unicidad | N° de documentos repetidos |
   | Validez | % de NIT con dígito de verificación inválido; emails sin "@"; fechas de nacimiento futuras; ingresos negativos |
   | Consistencia | N° de variantes de escritura por municipio |
   | Oportunidad | % de registros sin actualizar en más de 5 años |

   Para validar el dígito de verificación del NIT, implemente en Power Query el algoritmo de módulo 11: pesos 3, 7, 13, 17, 19, 23, 29, 37, 41 y 43, aplicados de derecha a izquierda; residuo r = suma mód 11; DV = r si r ∈ {0, 1}, de lo contrario 11 − r. *Contraste el algoritmo con una fuente oficial de la DIAN y cítela.*
2. **Índice de calidad (0.5 h).** Construya un índice ponderado (0–100) y justifique los pesos según el uso del dato en el control (por ejemplo, la unicidad pesa más si el maestro alimenta la verificación SARLAFT).
3. **Mini política de gobierno (1 h, máximo 2 páginas):**
   - roles (dueño del dato, custodio, usuarios) con cargos de COAGUA;
   - 5 reglas de calidad con su umbral y su responsable;
   - tratamiento de datos personales: finalidad, autorización y acceso mínimo, con referencia a la Ley 1581 de 2012;
   - cómo se monitoreará el índice en el tablero.
---

## <a id="t2"></a>T2 · Modelo estrella y medidas DAX de control (semana 3, 3 h, en equipo, 2%)

**RA:** RA1, RA2 · **Fecha límite:** viernes de la semana 3

1. Construya el modelo según la [práctica 02](../practicas-powerbi/02_modelo_datos/README.md) y capture la vista de modelo.
2. Implemente las 10 medidas mínimas de la [práctica 03](../practicas-powerbi/03_dax/README.md).
3. Diseñe **2 medidas propias** que respondan a preguntas de control que no estén en la práctica. Ejemplos: % del valor pagado a proveedores creados en el año o días promedio entre la aprobación y el pago por aprobador.
4. Elabore un diccionario de medidas con nombre, fórmula, interpretación, umbral propuesto y responsable.
5. Valide los totales contra el T0 (Excel).

**Entregable:** `.pbix` + diccionario (máximo 3 páginas).

---

## L2 (parte 1) · Laboratorio en clase: modelo y DAX (S2, en equipo)
Construir el modelo y las medidas de las carpetas 1 a 3 de [`medidas.dax`](../practicas-powerbi/03_dax/medidas.dax). Se entrega junto con la parte 2 (U3).

## Matriz de indicadores de control de COAGUA (S2, en equipo, insumo del Avance 2)

| Perspectiva | Objetivo de control | Indicador (KPI/KRI) | Fórmula (medida DAX) | Umbral verde / ámbar / rojo | Responsable | Frecuencia |
|---|---|---|---|---|---|---|
| Cumplimiento | … | … | … | … | … | … |
| Procesos | … | … | … | … | … | … |
| Financiera | … | … | … | … | … | … |
| Datos / información | … | … | … | … | … | … |

Mínimo 8 indicadores, al menos 3 de ellos KRI (indicadores de riesgo).
