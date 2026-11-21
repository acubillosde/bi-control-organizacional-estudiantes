# Práctica 06 · Conectarse a los sistemas de una organización

**Unidad:** U2 · **RA:** RA1, RA2 · **Se usa en:** Taller T1 (semana 2) y Avance 1 del caso integrador (rama `fuentes-organizacionales`)

En la práctica 01 todo era CSV. Aquí cada fuente exige una decisión técnica distinta. El mapa completo de los sistemas está en [`datos/sistemas/README.md`](../../datos/sistemas/README.md).

| Fuente | Conector de Power BI | Lo que se aprende |
|---|---|---|
| ERP en PostgreSQL | *Base de datos PostgreSQL* | Credenciales, cifrado, modo Importar o DirectQuery, plegado de consultas, SQL nativo |
| Excel de Finanzas | *Libro de Excel* | Hojas visibles y ocultas, encabezados que no empiezan en la fila 1, despivotar, unidades |
| Extractos del banco | *Carpeta* | Combinar archivos cuyo formato cambia, codificación, cultura de los números |
| Facturas XML | *Carpeta* + `Xml.Document` | Leer documentos jerárquicos con espacios de nombres |
| API de TRM | *Web* | JSON, parámetros de consulta, actualización desde la web |

**Antes de empezar:** conéctese a la base siguiendo la [guía de conexión](../../recursos/conexion_base_datos.md) y compruebe las filas esperadas.

## Parámetros
Cree tres parámetros de texto (*Inicio > Administrar parámetros*):

| Parámetro | Ejemplo |
|---|---|
| `ServidorERP` | `ep-xxxx.us-east-2.aws.neon.tech` (lo entrega el docente) |
| `BaseERP` | `neondb` |
| `RutaSistemas` | `C:\Cursos\bi-control-organizacional\datos\sistemas\` |

## Paso 1 · ERP: navegar y dejar que el servidor trabaje
Use la consulta `fPagosERP` de [`consultas_base.m`](consultas_base.m). Luego, en el editor de Power Query, haga clic derecho sobre el último paso y elija **Ver consulta nativa**. Si la opción está activa, el filtro se **plegó**: lo ejecuta PostgreSQL y a Power BI solo llegan las filas que necesita.

**Preguntas:**
1. Agregue una columna personalizada con `Text.Select` después del filtro. ¿Sigue activa *Ver consulta nativa*? ¿Por qué importa con millones de filas?
2. ¿Por qué el curso recomienda **Importar** y no **DirectQuery** para un tablero de control que el comité revisa una vez al mes? Piense en tres cosas: el costo de cómputo del servidor, la velocidad de respuesta y qué DAX se puede usar.

## Paso 2 · Excel hecho para leer, no para analizar
`fnHojaPresupuestoBase` lee **una** hoja. Pruébela con la hoja Bogotá. Después, construya usted la consulta que combina todas las hojas. Antes de combinar, revise:
- ¿Qué hojas tiene el libro? Mire la columna `Hidden` de `Excel.Workbook`.
- ¿Todas las hojas están en la misma unidad? Lea la fila 3 de cada una.
- ¿Los códigos de centro de costo cruzan con `erp.centros_costo`?
- ¿La hoja *Resumen* cuadra con el detalle?

## Paso 3 · Una carpeta de extractos
`fnExtractoA` lee los archivos de enero a junio. Abra un archivo de julio en un editor de texto (por ejemplo, el Bloc de notas) y escriba usted `fnExtractoB`. Tenga en cuenta tres cosas:
- `Csv.Document` acepta `Encoding = 1252` y `Columns = 5`.
- `Table.Skip` sirve para el preámbulo.
- `Table.TransformColumnTypes(..., "es-CO")` interpreta la coma decimal y las fechas dd/mm/aaaa.

Combine los dos formatos en una sola tabla `fBanco` con las columnas `fecha`, `detalle`, `documento`, `valor` (negativo = débito) y `saldo`.

**Control de calidad:** el saldo de cada movimiento debe ser el saldo anterior más el valor. Si no cuadra en algún punto, la lectura está mal.

## Paso 4 · Facturas XML
`fnHijo` y `fFacturaUna` leen un solo XML. Conviértalo en una consulta de carpeta que devuelva una fila por factura: número, fecha, NIT del emisor, CUFE y valor total.

## Paso 5 · API de TRM
`dTRM` consulta la API pública. Revise:
1. ¿Cuántos registros devuelve y cuántos días calendario hay entre el primero y el último? ¿Por qué no coinciden?
2. ¿Qué TRM le corresponde a un pago hecho un domingo?

## Problemas frecuentes

| Síntoma | Causa probable | Solución |
|---|---|---|
| Power BI ofrece conectar sin cifrado, o hay un error de certificado | Algo en la red intercepta la conexión cifrada | No acepte la conexión sin cifrar; pruebe otra red. Más casos en la [guía de conexión](../../recursos/conexion_base_datos.md#6-problemas-frecuentes) |
| `Endpoint ID is not specified` (Neon) | El cliente no envió el nombre del servidor en la negociación TLS (SNI) | Escriba la clave como `endpoint=<id-del-endpoint>;<clave>`, donde el identificador es la primera parte del servidor (`ep-xxxx`). ⚠ Solución documentada por Neon para clientes sin SNI; **pendiente de verificación** con la versión actual de Power BI Desktop |
| `permission denied for schema nomina` | Su usuario no tiene acceso a nómina | Es lo esperado: haga la [solicitud de acceso](../../caso-integrador/solicitud_acceso_datos.md) |
| `canceling statement due to statement timeout` | La consulta tardó más de 60 s | Filtre en el servidor (plegado) o use Importar en lugar de DirectQuery |
| La primera conexión del día tarda unos segundos | El servidor gratuito se suspende cuando no se usa | Espere y vuelva a intentar |
| Las tildes salen como `Ã³` | Codificación equivocada | UTF-8 (65001) de enero a junio, Windows-1252 (1252) de julio a diciembre |
| Los valores del banco quedan multiplicados por 100 o vacíos | Cultura equivocada | `"es-CO"` para el formato nuevo |
