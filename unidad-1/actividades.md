# Actividades · Unidad 1

## <a id="t0"></a>T0 · Del dato al modelo (pre-S1, 3.5 h, individual —los equipos se forman en el S1—, 1%)

**RA:** RA1 · **Fecha límite:** viernes previo al S1, 23:59

**Parte A. Entorno (1 h).** Instale Power BI Desktop según [`recursos/instalacion.md`](../recursos/instalacion.md) y complete la lista de verificación del entorno. Si usa Mac, indique qué alternativa usará.

**Parte B. Exploración en Python (2.5 h).** Use el cuaderno [`t0_exploracion_pagos.ipynb`](t0_exploracion_pagos.ipynb) con *pandas* para cargar `datos/integrador/pagos.csv` y responder las preguntas siguientes. Puede ejecutarlo en **Google Colab, sin instalar nada**, o en Jupyter o VS Code (ver [instalación](../recursos/instalacion.md)). El cuaderno trae la carga de los datos, una tabla de equivalencias con Excel y la pregunta 1 resuelta como ejemplo; en las demás usted completa las líneas marcadas con `TODO`. No hace falta saber Python de antemano.
1. ¿Cuántos pagos hay y cuál es el valor total pagado en 2025?
2. ¿Cuáles son los 5 proveedores con mayor valor pagado y qué porcentaje del total representan?
3. ¿Cómo se distribuye el valor pagado por mes? ¿Hay algún mes atípico?
4. ¿Cuántos pagos tienen el mismo usuario en `usuario_registra` y `usuario_aprueba`? ¿Por qué podría ser un problema?
5. Escriba una pregunta de control que **no** pueda responder con un solo archivo y explique qué datos adicionales necesitaría.

**Entregable:** un PDF de máximo 2 páginas con la lista de verificación, las respuestas y una captura de cada resultado (la salida de la celda de código que lo produce).
**Criterio:** [rúbrica de taller autónomo](../evaluacion/rubricas.md#r3-taller-autónomo).

---

## <a id="l1"></a>L1 · Laboratorio en clase: del diagnóstico al plan de transformación (S1, en equipo, 2%)

**Sin computador ni Power BI.** El ETL guiado se trabaja en el [T1](#t1) (semana 2). En el S1, los equipos usan la tarde para entender la pregunta del caso de COAGUA, diagnosticar su madurez de BI y proponer cómo mejorarla.

**Parte 1 (13:00–14:50).** Cada equipo hace cuatro tareas:
1. **Pregunta y anomalía (15'):** qué decisión necesita tomar el comité, cómo definen ustedes una *anomalía* y cuál es el apetito de riesgo (fase 1 de CRISP-DM). Dejen tres preguntas de control priorizadas. Escriban la definición **antes** de mirar las fuentes.
2. **Inventario de fuentes (15'):** con el [catálogo de COAGUA](../caso-integrador/madurez/coagua_fuentes.md) y el [diccionario de datos](../datos/README.md), liste qué fuentes hay, qué contiene cada una, quién podría ser el dueño y qué riesgo tiene. **No se abren los datos.**
3. **Diagnóstico rápido de madurez (35'):** una pregunta por dimensión (D1.1, D2.1, D3.3 y D4.3) y las cuatro banderas, con la regla de evidencia y la respuesta **NV** de la [actividad de diagnóstico](actividad_madurez_bi/README.md). Marquen el **frente crítico**.
4. **Plan de transformación (35' + 10' de galería):** una hoja con frentes críticos, nivel objetivo a 12 meses, ruta en tres horizontes (90 días, 6 y 12 meses), esfuerzo con incertidumbre, riesgos y la decisión que se le pide al comité. Ver [la guía del plan](actividad_madurez_bi/plan_transformacion.md) y su [plantilla de Excel](actividad_madurez_bi/plantilla_diagnostico_rapido.xlsx).

**Parte 2 (15:50–16:40), clínica de calidad.** Escriban **una regla de validación por cada dimensión de calidad** (completitud, unicidad, validez, consistencia, oportunidad y exactitud) para las fuentes de COAGUA: enunciado, campo, fuente y cómo se medirá. Clasifiquen cada regla como *error de calidad* o *posible falla de control* (o «por confirmar») e intercambien con otro equipo.

**Entregable (al cierre del S1):** dos hojas: el **plan de datos** (pregunta y anomalía, inventario de fuentes y tabla de reglas de calidad) y el **diagnóstico rápido con el plan de transformación**. Las reglas se implementan en el T1 como `tExcepcionesCalidad`.
**Criterio:** [rúbrica R7](../evaluacion/rubricas.md#r7-plan-de-transformación-de-la-madurez-de-bi).

---

## <a id="t1"></a>T1 · ETL completo y documentado (semana 2, 5.5 h, en equipo, 2%)

**RA:** RA1 · **Fecha límite:** sábado de la semana 2, 23:59

Aquí se hace el ETL que antes se hacía en clase y, en esta versión del curso, también la conexión a las fuentes de COAGUA. Parta del **plan de datos** del L1 (inventario de fuentes y reglas de calidad).
1. **ETL guiado con CSV (≈ 2 h).** Pasos 1 a 4 de la [práctica 01](../practicas-powerbi/01_power_query/README.md): parámetro `RutaDatos`, función `fnLeerCsv`, dimensiones y hechos, incluidos `fCreditos` con `calificacion_esperada` y `fuera_de_politica`. Es el entrenamiento en las técnicas que usará con los sistemas.
2. **Perfilado y excepciones (≈ 0.5 h).** Pasos 5 y 6: `tExcepcionesCalidad` con las **reglas que su equipo escribió en el L1**. Una frase por regla: ¿error de calidad o posible falla de control?
3. **Conexión a las fuentes de COAGUA (≈ 2.5 h).** Siga la [práctica 06](../practicas-powerbi/06_fuentes_organizacionales/README.md), pasos 1 a 5: ERP en PostgreSQL y cartera (con la [guía de conexión](../recursos/conexion_base_datos.md)), Excel de Finanzas, extractos del banco, facturas XML y API de TRM. Use los parámetros `ServidorERP`, `BaseERP` y `RutaSistemas`, **sin credenciales** dentro de las consultas.
4. **Documentación (≈ 0.5 h).** Tabla del flujo ETL: consulta, fuente, transformaciones clave, columnas derivadas y control que habilita; y la fase de CRISP-DM de cada paso.

Las columnas de control propias y el modelo se hacen en el [Avance 1](../caso-integrador/avance_1.md).

**Entregable:** `.pbix` + documento de 2 páginas.
**Criterio:** [rúbrica de taller autónomo](../evaluacion/rubricas.md#r3-taller-autónomo).

---

## Discusión de casos (S1)
- [Guía del caso SYSCO](../casos/caso_sysco.md) (o el [caso ficticio de la Distribuidora Andina](../casos/caso_distribuidora_andina.md), si el docente lo indica)
- [Guía del caso DIARI – Contraloría General de la República](../casos/caso_diari_contraloria.md)
