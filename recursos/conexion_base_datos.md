# Guía de conexión a la base de datos de COAGUA desde Power BI

**Para:** los equipos del caso integrador (rama `fuentes-organizacionales`) · **Tiempo:** 15 minutos · **Requisito:** Power BI Desktop en Windows ([instalación](instalacion.md))

El ERP de COAGUA es una base de datos **PostgreSQL** en la nube. Para conectarse no hay que instalar nada adicional: Power BI Desktop ya trae el conector.

## 1. Los datos de conexión de su equipo

El docente le entrega a cada equipo, por un canal privado, cuatro datos:

| Dato | Ejemplo (no es real) | Dónde se usa |
|---|---|---|
| **Servidor** | `ep-cool-darkness-123456.us-east-2.aws.neon.tech` | Paso 3 |
| **Base de datos** | `neondb` | Paso 3 |
| **Usuario** | `equipo04` | Paso 4 |
| **Clave** | 20 letras y números | Paso 4 |

**Reglas de custodia (son parte de la evaluación):**
- La clave es del equipo. No la publique en el chat del curso, en GitHub, en el informe ni en capturas de pantalla.
- Power BI guarda la clave **en su computador** y no dentro del `.pbix`. Si comparte el `.pbix` con un compañero, él debe escribir la clave en su propio Power BI.
- Si cree que la clave se filtró, avise al docente: él la cambia.

## 2. Antes de empezar
- Conexión a internet. Si está en la red de la Universidad y no logra conectarse, pruebe desde otra red: algunas redes bloquean el puerto 5432, que es el de PostgreSQL.
- Power BI Desktop actualizado. Si lo instaló antes de 2020, actualícelo.

## 3. Conectarse

1. Abra Power BI Desktop y vaya a **Inicio > Obtener datos > Más…**.
2. Busque **PostgreSQL**, seleccione **Base de datos PostgreSQL** y haga clic en **Conectar**.
3. En el cuadro de diálogo, llene estos campos:
   - **Servidor:** el servidor de su equipo, sin `postgresql://`, sin usuario y sin clave. Por ejemplo, `ep-cool-darkness-123456.us-east-2.aws.neon.tech`.
   - **Base de datos:** `neondb` o la que le indicaron.
   - **Modo de conectividad de datos:** **Importar**. No use DirectQuery en el curso: consume la cuota del servidor gratuito en cada clic.
   - **Opciones avanzadas:** déjelas vacías por ahora. La práctica 06 explica cuándo escribir SQL ahí.
4. Clic en **Aceptar**. La primera vez aparece la ventana de credenciales:
   - Elija la pestaña **Base de datos** en la izquierda (no *Cuenta de Microsoft*).
   - Escriba el **Usuario** y la **Contraseña** de su equipo.
   - En *Seleccione el nivel al que se aplicará esta configuración*, elija el servidor completo.
   - Clic en **Conectar**.
5. Si Power BI le ofrece **conectarse sin cifrado**, responda **Cancelar** y revise la sección 6. El servidor del curso exige conexión cifrada, así que ese mensaje indica un problema de red o de certificado. No lo resuelva conectándose sin cifrar.
6. Se abre el **Navegador**. Las tablas aparecen con el formato *esquema.tabla*, por ejemplo `erp.pagos`. Marque `erp.centros_costo` y haga clic en **Transformar datos**, no en *Cargar*. Así revisa los datos antes de traerlos.

> **Primera conexión del día:** el servidor gratuito se suspende cuando nadie lo usa, y despertarlo puede tardar unos segundos. Si la primera vez sale un error de tiempo de espera, intente de nuevo.

## 4. Comprobar que la conexión funciona

En el editor de Power Query, la consulta de `erp.centros_costo` debe mostrar **12 filas** y las columnas `cod_ccosto`, `nombre` y `regional`. Agregue también estas consultas y compare:

| Tabla | Filas esperadas |
|---|---:|
| `erp.centros_costo` | 12 |
| `erp.terceros` | 184 |
| `cartera.creditos` | 3.200 |
| `gobierno.usuarios_tablero` | 10 |

Si los números coinciden, la conexión está lista.

**Es normal** que al abrir el esquema `nomina` aparezca *permission denied*. Ese acceso se pide con la [solicitud formal](../caso-integrador/solicitud_acceso_datos.md). Cuando el docente lo aprueba, no hay que cambiar nada en Power BI: basta con **Actualizar**.

## 5. Dejar la conexión parametrizada (obligatorio para el Avance 1)

El `.pbix` que entregue debe abrir en el computador del docente, que se conecta a **otro** servidor. Por eso el servidor y la base no se escriben fijos: van en parámetros.

1. En Power Query, vaya a **Inicio > Administrar parámetros > Nuevo parámetro**.
   - `ServidorERP`, tipo **Texto**, con el valor de su servidor.
   - `BaseERP`, tipo **Texto**, con el valor `neondb`.
2. Abra la consulta, vaya a **Inicio > Editor avanzado** y reemplace el texto fijo por los parámetros:
   ```powerquery
   // Antes
   Origen = PostgreSQL.Database("ep-cool-darkness-123456.us-east-2.aws.neon.tech", "neondb"),
   // Después
   Origen = PostgreSQL.Database(ServidorERP, BaseERP),
   ```
3. Repita el cambio en todas las consultas que lean de la base.
4. Compruebe que **ninguna** consulta contenga el usuario ni la clave. Power BI nunca los pone en el código, pero tampoco los agregue usted.

## 6. Problemas frecuentes

| Mensaje o síntoma | Qué significa | Qué hacer |
|---|---|---|
| `password authentication failed for user "equipoNN"` | Usuario o clave incorrectos | Revise mayúsculas y espacios al pegar. Para volver a escribirla: **Archivo > Opciones y configuración > Configuración de origen de datos**, seleccione el servidor, **Editar permisos > Editar** |
| `Endpoint ID is not specified` | El servidor en la nube no pudo identificar a qué base va dirigida la conexión | En la contraseña escriba `endpoint=ep-cool-darkness-123456;CLAVE`, es decir, la primera parte del servidor (hasta el primer punto), un punto y coma y la clave. ⚠ Solución documentada por el proveedor (Neon); pendiente de verificar con Power BI. Si no funciona, avise al docente |
| `No such host is known` / no se encuentra el host | El nombre del servidor está mal escrito | Copie el servidor sin espacios, sin `postgresql://` y sin `/neondb` al final |
| Tiempo de espera agotado en la primera conexión | El servidor estaba suspendido | Espere 10 segundos e intente de nuevo |
| Tiempo de espera siempre, en cualquier tabla | La red bloquea el puerto 5432 | Pruebe otra red (por ejemplo, el celular como módem) e informe al docente |
| Ofrece conectarse **sin cifrado**, o hay un error de certificado | Algo en la red intercepta la conexión cifrada | No acepte la conexión sin cifrar. Pruebe otra red y avise al docente |
| `permission denied for schema nomina` | Su equipo no tiene acceso a nómina | Es lo esperado. Vea la [solicitud de acceso](../caso-integrador/solicitud_acceso_datos.md) |
| `cannot execute ... in a read-only transaction` | Intentó modificar datos | Su usuario es de solo lectura. Las transformaciones se hacen en Power Query, no en la base |
| `canceling statement due to statement timeout` | Una consulta tardó más de 60 segundos | Filtre antes de traer datos (vea plegado de consultas en la práctica 06) |
| Pide credenciales cada vez que abre el archivo | Las credenciales se guardaron para otro nivel o se borraron | Bórrelas en *Configuración de origen de datos* (**Borrar permisos**) y conéctese de nuevo |
| El compañero abre el `.pbix` y no carga | Las credenciales no viajan con el archivo | Cada integrante escribe la clave en su propio Power BI |

## 7. ¿Y si tengo Mac?
Power BI Desktop solo existe para Windows; las alternativas están en [instalación](instalacion.md#2-mac). La conexión funciona igual desde una máquina virtual con Windows o desde la sala de cómputo. Desde la red de la Universidad, verifique antes que el puerto 5432 no esté bloqueado.
