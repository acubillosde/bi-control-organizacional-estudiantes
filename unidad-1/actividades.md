# Actividades · Unidad 1

## <a id="t0"></a>T0 · Del Excel al modelo (pre-S1, 3.5 h, individual —los equipos se forman en el S1—, 1%)

**RA:** RA1 · **Fecha límite:** viernes previo al S1, 23:59

**Parte A. Entorno (1 h).** Instale Power BI Desktop según [`recursos/instalacion.md`](../recursos/instalacion.md) y complete la lista de verificación del entorno. Si usa Mac, indique qué alternativa usará.

**Parte B. Exploración con tabla dinámica (2.5 h).** Abra `datos/integrador/pagos.csv` en Excel (*Datos → Desde texto/CSV*) y, con tablas dinámicas, responda:
1. ¿Cuántos pagos hay y cuál es el valor total pagado en 2025?
2. ¿Cuáles son los 5 proveedores con mayor valor pagado y qué porcentaje del total representan?
3. ¿Cómo se distribuye el valor pagado por mes? ¿Hay algún mes atípico?
4. ¿Cuántos pagos tienen el mismo usuario en `usuario_registra` y `usuario_aprueba`? ¿Por qué podría ser un problema?
5. Escriba una pregunta de control que **no** pueda responder con una tabla dinámica de un solo archivo y explique qué datos adicionales necesitaría.

**Entregable:** un PDF de máximo 2 páginas con la lista de verificación, las respuestas y una captura de cada tabla dinámica.
**Criterio:** [rúbrica de taller autónomo](../evaluacion/rubricas.md#r3-taller-autónomo).

---

## L1 · Laboratorio en clase: ETL con Power Query (S1, en equipo, 2%)

Siga la [práctica 01](../practicas-powerbi/01_power_query/README.md), pasos 1–7. Al terminar el S1, entregue el `.pbix` con:
- todas las consultas de dimensiones y hechos;
- la tabla de resultados del perfilado de calidad;
- la consulta `tExcepcionesCalidad` y una frase por regla que distinga un "problema de calidad del dato" de un "posible problema de control".

---

## <a id="t1"></a>T1 · ETL completo y documentado (semana 2, 3 h, en equipo, 2%)

**RA:** RA1 · **Fecha límite:** sábado de la semana 2, 23:59

Partiendo del `.pbix` del L1:
1. Agregue `fCreditos` con las columnas `calificacion_esperada` y `fuera_de_politica`.
2. Cree una consulta nueva que **usted** diseñe para un control adicional que no esté en la práctica (por ejemplo: proveedores sin pagos, pagos a proveedores en estado distinto de "Activo" o facturas con fecha futura). Explique qué riesgo cubre.
3. Documente el flujo ETL en una tabla con estas columnas: consulta, fuente, transformaciones clave, columnas derivadas y control que habilita.
4. Indique en qué fase de CRISP-DM está cada paso que realizó.

**Entregable:** `.pbix` + documento de 2 páginas.
**Criterio:** [rúbrica de taller autónomo](../evaluacion/rubricas.md#r3-taller-autónomo).

---

## Discusión de casos (S1)
- [Guía del caso SYSCO](../casos/caso_sysco.md)
- [Guía del caso DIARI – Contraloría General de la República](../casos/caso_diari_contraloria.md)
