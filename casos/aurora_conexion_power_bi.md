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

## 6. Una prueba rápida: los pagos de marzo

Va a reproducir una cifra de la verificación **V07**: lo que sumaron los pagos **aprobados en marzo de 2025**. Todavía no tiene tabla calendario (se crea en V04), así que el filtro de marzo se hace con un segmentador de rango de fechas.

**Prediga primero:** ¿cuánto cree que sumaron los pagos aprobados en marzo? ¿Cuántos pagos fueron? Anótelo antes de seguir.

### Paso 1. La suma de los pagos
1. En la **Vista de informe**, en una página en blanco, seleccione el visual **Tarjeta** en el panel *Visualizaciones*.
2. Arrastre `fPagos[valor]` al campo de la tarjeta. Debajo del campo debe decir **Suma de valor**. Si dice *Recuento* o *Promedio*, pulse la flecha del campo y elija **Suma**.
3. La tarjeta muestra hoy el total de todo el año, no de marzo. Es normal.

### Paso 2. El número de pagos
1. Haga clic en un espacio vacío de la página y agregue otra **Tarjeta**.
2. Arrastre `fPagos[id_pago]` y cambie el campo a **Recuento**. Esta tarjeta debe decir 1.808 mientras no haya filtro.

### Paso 3. El filtro de marzo
1. Haga clic en un espacio vacío y agregue un **Segmentador**.
2. Arrastre `fPagos[fecha_aprobacion]` al campo del segmentador. **Importante:** use la columna **fecha_aprobacion**, no `fecha_pago` ni `fecha_factura`. En V07 se verá que cada fecha da una cifra distinta.
3. Si el campo aparece como una jerarquía (Año, Trimestre, Mes, Día), pulse la flecha junto al campo en el panel y elija **fecha_aprobacion** en lugar de *Jerarquía de fechas*. Así el segmentador muestra fechas completas.
4. En el segmentador, pulse los tres puntos o la flecha de la esquina y elija el estilo **Entre**. Quedan dos casillas de fecha.
5. Escriba **1/03/2025** en la primera casilla y **31/03/2025** en la segunda. El formato (día/mes/año) depende de la configuración regional de su computador: si no acepta la fecha, use el que le muestre el segmentador.

*Otra forma, sin segmentador:* seleccione la tarjeta, abra el panel **Filtros**, arrastre `fecha_aprobacion` a «Filtros en este objeto visual», elija **Filtrado avanzado**, y escriba «es posterior o igual a» 1/03/2025 **y** «es anterior o igual a» 31/03/2025.

### Paso 4. Lea el resultado
Con el filtro puesto, las tarjetas deben mostrar:

| Tarjeta | Resultado esperado |
|---|---|
| Suma de valor | **957.980.305** (es decir, **$958,0 millones**) |
| Recuento de id_pago | **150** pagos |

Power BI puede mostrar la suma abreviada, como «958 M» o «958 mill.». Para ver el número completo, seleccione la tarjeta, vaya a **Formato → Valor de datos → Unidades de presentación** y elija **Ninguna**. Para verlo en millones con un decimal, elija **Millones** y ponga 1 en *Posiciones decimales de valor*.

### Paso 5. Compare
Este valor debe coincidir con tres fuentes independientes:
- La guía: V07, «Por fecha de aprobación = $958,0 millones».
- Python: `python casos/verificacion_aurora.py V07` imprime «Por fecha de aprobación: 958,0».
- Su propia predicción del inicio.

Si las tres coinciden, la conexión, la carga y el modelo están bien. Si alguna difiere, una tiene el error: búsquelo antes de seguir.

### Si no le da 957.980.305
| Qué ve | Probable causa |
|---|---|
| 956,8 millones y 155 pagos | Filtró por `fecha_pago` y no por `fecha_aprobacion` |
| Un valor menor, y menos de 150 pagos | El rango termina antes del 31/03, o la fecha inicial es posterior al 1/03 |
| Un valor muchísimo mayor, 1.808 pagos | El filtro no se aplicó: el segmentador está en otra página o conectado a otro visual |
| Un número pequeño, como un promedio | El campo dice *Promedio* o *Recuento* en lugar de *Suma* |
| El total sale en blanco o con error | `valor` está como Texto: cámbielo a **Número entero** en Power Query |

> **No se preocupe por los 4 duplicados de marzo.** En esta prueba están incluidos, porque la cifra de 958,0 es «por fecha de aprobación» con todos los pagos. Quitarlos (909,7) se hace en V07, con la columna `es_duplicado`.

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
