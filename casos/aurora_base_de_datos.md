# Aurora en una base de datos: del CSV al modelo con reglas

**Rama:** `fuentes-organizacionales` · **Tiempo:** 30 minutos · **Requisito:** los datos de conexión de su equipo y la [guía de conexión](../recursos/conexion_base_datos.md)

En el caso de [Tiendas Aurora](caso_tiendas_aurora.md) los datos llegan en seis archivos CSV. Los hallazgos del caso (tres cifras para «el pago del mes», ciudades mal escritas, un NIT repetido, pagos duplicados) existen **porque nada impide que ocurran**. Aquí Aurora vive en la misma base PostgreSQL de COAGUA, en dos esquemas:

| Esquema | Qué contiene | Es el… |
|---|---|---|
| `aurora_crudo` | Los seis CSV tal como llegan: todo texto, sin reglas | «antes» |
| `aurora` | El modelo limpio, con llaves, relaciones, restricciones y vistas | «después» |

Nada se borra. Lo que el proceso de carga (ETL) corrige o deja en revisión queda anotado en `aurora.bitacora_calidad`, y el original sigue en `aurora_crudo`.

## 1. Conéctese y vea las tablas

Siga la [guía de conexión](../recursos/conexion_base_datos.md) con el usuario de su equipo. En el Navegador, abra el esquema `aurora` y verá las tablas `tiendas`, `proveedores`, `pagos`, `ventas_diarias`, `empleados`, `limites_aprobacion`, `bitacora_calidad` y las vistas `v_pagos_control`, `v_pago_del_mes`, `v_pagos_por_aprobacion` y `v_hallazgos`.

Su usuario es **de solo lectura**. En `empleados` solo puede ver el usuario del sistema, el cargo y la tienda: el nombre y la cuenta de nómina son datos personales y requieren una solicitud aprobada (ver el apartado 5).

Las consultas de abajo puede escribirlas en Power BI (*Obtener datos → Base de datos PostgreSQL → Opciones avanzadas → Instrucción SQL*) o en cualquier cliente de PostgreSQL.

## 2. Prediga y compruebe

Haga como en las [verificaciones](verificacion_aurora.md): primero prediga, después consulte, después compare.

### A. ¿Qué limpió el ETL? (V02 y V08)
**Prediga:** ¿cuántas ciudades distintas hay en `aurora_crudo.proveedores`? ¿Y en `aurora.proveedores`?
```sql
SELECT (SELECT count(DISTINCT ciudad) FROM aurora_crudo.proveedores) AS ciudades_antes,
       (SELECT count(DISTINCT ciudad) FROM aurora.proveedores)       AS ciudades_despues,
       (SELECT count(DISTINCT nit_digitos) FROM aurora.proveedores)  AS nit_distintos;
```
Esperado: **8, 5 y 46**. Los 47 proveedores tienen 46 NIT distintos: uno se repite.
```sql
SELECT regla, count(*) AS registros FROM aurora.bitacora_calidad GROUP BY regla ORDER BY regla;
SELECT llave, antes, despues, detalle FROM aurora.bitacora_calidad WHERE regla = 'nit_repetido';
```
Esperado: 8 ciudades estandarizadas, 1 NIT repetido (P047, que repite el de P009) y 16 pagos duplicados. **El proveedor P047 no se borró:** quedó en `en_revision` hasta que compras confirme si es el mismo.

### B. «El pago del mes» con una sola definición (V07)
**Prediga:** en marzo de 2025, ¿cuál de las tres cifras es «el pago del mes»?
```sql
SELECT round(a.por_fecha_de_aprobacion / 1e6, 1)         AS por_aprobacion,
       round(m.por_fecha_de_pago / 1e6, 1)               AS por_pago,
       round(a.por_aprobacion_sin_duplicados / 1e6, 1)   AS aprobacion_sin_duplicados,
       round(m.pago_del_mes / 1e6, 1)                    AS pago_del_mes_definicion_unica
FROM aurora.v_pago_del_mes m JOIN aurora.v_pagos_por_aprobacion a USING (mes)
WHERE mes = '2025-03-01';
```
Esperado: **958,0 · 956,8 · 909,7** (las tres cifras del correo de marzo) y **905,7** (por fecha de pago y sin duplicados). Esa última es la definición de la matriz de indicadores, escrita **una sola vez** en la vista `v_pago_del_mes`: quien la consulte, de compras o de contabilidad, obtiene la misma cifra.

### C. Los hallazgos de control (V03, V14 a V16)
```sql
SELECT * FROM aurora.v_hallazgos;
```
Esperado: 8 ciudades corregidas · 1 NIT repetido · **16** pagos duplicados · **18** pagos con el mismo usuario · **14** aprobaciones en día no hábil · **34** pagos entre el 95% y el 100% del límite del jefe de compras.

Compare con Power BI y con `python casos/verificacion_aurora.py`: las tres herramientas deben dar lo mismo. Si no, una tiene el error.

### D. ¿Qué reglas impone la base? 
**Prediga:** ¿qué pasaría si alguien intenta registrar un pago donde quien lo registra también lo aprueba?
```sql
SELECT conrelid::regclass AS tabla, conname AS regla, pg_get_constraintdef(oid) AS definicion
FROM pg_constraint
WHERE connamespace = 'aurora'::regnamespace AND contype IN ('c', 'u')
ORDER BY 1, 2;
SELECT indexname, indexdef FROM pg_indexes WHERE schemaname = 'aurora' AND indexname IN ('pagos_sin_duplicados', 'proveedores_nit_unico');
```
Verá `quien_registra_no_aprueba`, `aprobacion_en_dia_habil`, `registro_despues_de_factura`, la lista cerrada de cinco ciudades y los índices que impiden un segundo pago con el mismo proveedor, factura y valor. Como su usuario es de solo lectura, el docente muestra en vivo cómo la base **rechaza** esos pagos.

> **Los pagos antiguos que ya incumplen no se borraron.** Esas tres reglas se crearon con `NOT VALID`: valen para todo pago **nuevo**, y el histórico (18 pagos con el mismo usuario, 14 en día no hábil y 9 registrados antes de la factura) queda a la vista como hallazgo. Es lo que se hace en una organización cuando se endurece un control sobre datos que ya existen.

## 3. Úselo en Power BI

En lugar de importar los CSV, importe del esquema `aurora` las tablas `pagos`, `proveedores`, `tiendas`, `ventas_diarias` y, si le sirven, las vistas. Las columnas de control de la verificación V03 (`mismo_usuario`, `aprobacion_dia_no_habil`, `factura_normalizada`) y la marca de duplicado (`es_duplicado`) ya vienen calculadas en `v_pagos_control`. Compruebe que sus medidas DAX dan lo mismo que antes.

Pregunta para discutir: si las columnas de control ya vienen de la base, ¿qué ganó Aurora y qué perdió el analista, que antes las construía en Power Query?

## 4. Qué cambió frente a los CSV

| Antes (CSV) | Ahora (base de datos) |
|---|---|
| Cada área calcula «el pago del mes» a su manera | Una vista con una sola definición |
| Una ciudad puede escribirse de ocho maneras | Una lista cerrada de cinco ciudades |
| Un NIT o un pago pueden repetirse sin aviso | Un índice único lo impide para registros nuevos |
| Quien registra puede aprobar | La base rechaza el pago nuevo |
| Cualquiera que reciba el archivo ve todo | Permisos por rol; datos personales aparte |

La base no arregla por sí sola un proceso mal diseñado, pero hace que el control deje de depender de que alguien se acuerde.

## 5. El cruce de cuentas bancarias (V17)

Cruzar las cuentas de los proveedores con las de nómina es un control legítimo, pero el resultado identifica a una persona. Por eso la vista `v_cuenta_compartida` y los campos `nombre` y `cuenta_nomina` de `empleados` **no** están disponibles con el permiso básico. El equipo debe pedirlos con una solicitud formal, como la de nómina de COAGUA, y el docente los concede o los niega. Con el permiso concedido:
```sql
SELECT * FROM aurora.v_cuenta_compartida;
```
Esperado: un proveedor, **P046**, con 5 pagos por $34,4 millones. Se entrega a quien debe investigar; no se publica en un tablero general.
