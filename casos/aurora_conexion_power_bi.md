# Conecte Power BI a la base de datos de Aurora

**Rama:** `fuentes-organizacionales` · **Tiempo:** 20 minutos · **Requisito:** Power BI Desktop en Windows ([instalación](../recursos/instalacion.md)) y los datos de conexión de su equipo

Esta guía lleva las tablas de [Aurora](aurora_base_de_datos.md) a Power BI y las deja listas para las [verificaciones](verificacion_aurora.md). Es la misma base y la misma conexión que usa para COAGUA; solo cambia el esquema: Aurora vive en `aurora` (modelo limpio) y `aurora_crudo` (los CSV tal cual).

## 1. Lo que necesita

El docente le entrega, por un canal privado, cuatro datos:

| Dato | Ejemplo (no es real) |
|---|---|
| **Servidor** | `ep-cool-darkness-123456.us-east-2.aws.neon.tech` |
| **Base de datos** | `neondb` |
| **Usuario** | `equipo04` |
| **Clave** | 20 letras y números |

La clave es del equipo: no la publique en el chat, en GitHub, en un informe ni en capturas. Power BI la guarda en su computador y no dentro del `.pbix`.

## 2. Conectarse

1. Abra Power BI Desktop. **Inicio → Obtener datos → Más…**
2. Busque **PostgreSQL**, elija **Base de datos PostgreSQL** y pulse **Conectar**.
3. Llene:
   - **Servidor:** solo el nombre del servidor, sin `postgresql://`, sin usuario, sin clave y sin `/neondb`.
   - **Base de datos:** `neondb`
   - **Modo de conectividad de datos:** **Importar**. No use DirectQuery: cada clic consulta el servidor y gasta su cuota gratuita.
4. **Aceptar.** En la ventana de credenciales elija la pestaña **Base de datos** (no *Cuenta de Microsoft*), escriba usuario y clave, deje el nivel en el servidor completo y pulse **Conectar**.
5. Si Power BI ofrece conectarse **sin cifrado**, responda **Cancelar**. El servidor exige conexión cifrada; ese mensaje indica un problema de red. No lo resuelva conectándose sin cifrar.

> **Primera conexión del día:** el servidor gratuito se suspende cuando nadie lo usa y despertarlo tarda unos segundos. Si sale un error de tiempo de espera, intente de nuevo.

Si algo falla, la tabla de problemas está en la [guía general de conexión](../recursos/conexion_base_datos.md#6-problemas-frecuentes) (sección 6).

## 3. Elegir las tablas de Aurora

En el **Navegador** abra el esquema `aurora`. Marque estas cuatro:

| Tabla o vista | Qué es | Nómbrela en Power BI |
|---|---|---|
| `aurora.v_pagos_control` | Los pagos, con las columnas de control ya calculadas | `fPagos` |
| `aurora.ventas_diarias` | Una fila por tienda y día | `fVentas` |
| `aurora.proveedores` | El maestro de proveedores, ya limpio | `dProveedores` |
| `aurora.tiendas` | Las 12 tiendas | `dTiendas` |

Pulse **Transformar datos**, no *Cargar*: así revisa antes de traer.

> **Use `v_pagos_control` y no `pagos`.** La vista trae `mismo_usuario`, `aprobacion_dia_no_habil`, `factura_normalizada`, `es_duplicado` y `sobre_limite`. Son las columnas que en las verificaciones V03 y V07 se construyen a mano; aquí ya vienen. Construirlas usted igual y comparar con las de la base es un buen ejercicio.

### Los empleados: una consulta propia

No marque `aurora.empleados` en el Navegador. Su usuario no puede leer `nombre` ni `cuenta_nomina` (datos personales) y Power BI suele leer todas las columnas de la tabla que se marca, y entonces sale *permission denied*. Cree una consulta con solo lo permitido:

1. **Inicio → Obtener datos → Base de datos PostgreSQL**, el mismo servidor y la misma base.
2. Abra **Opciones avanzadas** y en **Instrucción SQL** escriba:
   ```sql
   SELECT id_empleado, usuario_sistema, cargo, id_tienda
   FROM aurora.empleados
   ```
3. **Aceptar** y nombre la consulta `dEmpleados`.

Quedan 36 filas. Si su equipo necesita el nombre o la cuenta de nómina (por ejemplo, para la verificación V17), pídalos con una solicitud formal; el docente concede el acceso y no hay que cambiar nada en Power BI, basta con **Actualizar**.

## 4. Comprobar que cargó bien

En Power Query, cada consulta debe mostrar estas filas (ver el recuento en **Vista → Perfil de columna basado en todo el conjunto de datos**):

| Consulta | Filas esperadas |
|---|---:|
| `fPagos` | 1.808 |
| `fVentas` | 4.371 |
| `dProveedores` | 47 |
| `dTiendas` | 12 |
| `dEmpleados` | 36 |

Si los números coinciden, es la verificación **V01** resuelta con la base en lugar de los CSV.

Compruebe también los tipos de columna: las fechas (`fecha_factura`, `fecha_aprobacion`, `fecha_pago`, `fecha`) en **Fecha**, y `valor`, `ventas`, `tickets` y `devoluciones` en **Número entero**. Las columnas de control (`mismo_usuario`, `aprobacion_dia_no_habil`, `es_duplicado`) son 0 o 1.

Pulse **Cerrar y aplicar**.

## 5. Armar el modelo

En la **Vista de modelo** compruebe, o cree, estas relaciones (de uno a varios, un solo sentido de filtro):

| Desde (uno) | Hacia (varios) |
|---|---|
| `dProveedores[id_proveedor]` | `fPagos[id_proveedor]` |
| `dTiendas[id_tienda]` | `fPagos[id_tienda]` |
| `dTiendas[id_tienda]` | `fVentas[id_tienda]` |

Power BI puede detectar algunas solas: revíselas, porque a veces se equivoca de columna o de sentido. El calendario y la segunda relación con `fecha_pago` (inactiva) se agregan en las verificaciones V04 y V07.

## 6. Una prueba rápida

Cree una tarjeta con la suma de `fPagos[valor]` y un segmentador de mes sobre una columna de fecha. Compare con la verificación **V07**: marzo de 2025 por fecha de aprobación debe dar **$958,0 millones**.

Si coincide con lo que obtiene en la base, con lo que da `python casos/verificacion_aurora.py V07` y con lo que dice la guía, las tres herramientas están de acuerdo. Si una difiere, una tiene el error: búsquelo antes de seguir.

## 7. Qué cambia frente a los CSV

| Con CSV | Con la base de datos |
|---|---|
| Carga de seis archivos, uno por uno | Una conexión, varias tablas |
| Columnas de control: las construye usted | Ya vienen en `v_pagos_control` |
| Ciudades y NIT sin limpiar | `dProveedores` ya viene limpio; el original está en `aurora_crudo` |
| Actualizar es volver a cargar un archivo | **Actualizar** consulta la base |
| Cualquiera ve todo | Usted no ve nombre ni cuenta de nómina |

Para ver el «antes», puede importar `aurora_crudo.proveedores` y comparar sus ciudades con las de `aurora.proveedores`: de 8 maneras de escribirlas se pasa a 5.

## 8. Antes de entregar un `.pbix`

- **Sin credenciales dentro del archivo.** Power BI nunca las pone en el código ni las agregue usted.
- **Servidor y base en parámetros** (`ServidorERP` y `BaseERP`), como en la [guía general](../recursos/conexion_base_datos.md#5-dejar-la-conexión-parametrizada-obligatorio-para-el-avance-1). El archivo debe abrir en otro computador y con otro servidor.
- **La consulta SQL de `dEmpleados` también.** Cámbiele el servidor y la base por los parámetros.
- **Un compañero que abre su `.pbix`** escribe la clave en su propio Power BI; las credenciales no viajan con el archivo.
