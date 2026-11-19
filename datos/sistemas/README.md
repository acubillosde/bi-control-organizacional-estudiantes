# Sistemas de información de COAGUA (rama `fuentes-organizacionales`)

> **Todos los datos son ficticios**, igual que en el resto del curso. La TRM es la única excepción: es la tasa oficial publicada en datos.gov.co.

En una organización real los datos no llegan como un paquete de CSV limpios. Cada área los guarda en su sistema, con su formato y su responsable. Este es el panorama que encuentra su equipo al llegar a COAGUA:

| Sistema | Dueño (ficticio) | Dónde está | Cómo se accede | Qué contiene |
|---|---|---|---|---|
| **ERP · cuentas por pagar** | Dirección de Tecnología | PostgreSQL en la nube, esquema `erp` | Usuario y clave del equipo (los entrega el docente). Solo lectura | Terceros (proveedores), pagos, centros de costo, límites de aprobación, festivos |
| **Cartera** | Gerencia de Riesgos | PostgreSQL, esquema `cartera` | El mismo usuario | Créditos y política de líneas |
| **Nómina** | Gestión Humana | PostgreSQL, esquema `nomina` | **Restringido.** Requiere una [solicitud formal de acceso](../../caso-integrador/solicitud_acceso_datos.md) aprobada | Datos de empleados |
| **Usuarios del tablero** | Control interno | PostgreSQL, esquema `gobierno` | El mismo usuario | Quién puede ver qué regional (seguridad por filas) |
| **Presupuesto** | Dirección Financiera | [`finanzas/Presupuesto_2025_v3_FINAL.xlsx`](finanzas/) | Archivo compartido por correo | Presupuesto 2025 por regional y centro de costo |
| **Extractos bancarios** | Tesorería | [`banco/`](banco/) | Descarga mensual del portal del banco | Movimientos de la cuenta corriente pagadora, enero a diciembre de 2025 |
| **Facturas electrónicas** | Contabilidad | [`facturas_electronicas/`](facturas_electronicas/) | Exportación del buzón de facturación | XML de las facturas recibidas en el 4.º trimestre de 2025 |
| **Tasa de cambio (TRM)** | Superintendencia Financiera (vía datos.gov.co) | API pública: `https://www.datos.gov.co/resource/32sa-8pi3.json` | Sin autenticación | TRM oficial diaria |

La documentación técnica del ERP está en el [diccionario de datos](diccionario_erp.md). Fue escrita por TI hace dos años: **verifíquela contra los datos antes de confiar en ella**, como haría un auditor.

## Lo que comentó cada área cuando su equipo pidió los datos

- **Tecnología:** «La base está en la nube. Conéctense con el conector de PostgreSQL de Power BI y marquen *Cifrar conexiones*. Les dejamos permisos de solo lectura y las consultas de más de un minuto se cancelan. Si necesitan nómina, eso no lo decidimos nosotros: hablen con Gestión Humana».
- **Finanzas:** «El presupuesto es el Excel que presentamos al consejo. Tiene una hoja por regional y un resumen. Lo armamos a mano, así que no es una base de datos».
- **Tesorería:** «Los extractos los descargamos del portal del banco. En julio el banco cambió de plataforma y desde entonces los archivos salen distintos».
- **Contabilidad:** «Los XML los exportamos del buzón de facturación electrónica. Solo tenemos el último trimestre a mano. Los proveedores del exterior no facturan electrónicamente en Colombia».

## Conexión a la base de datos desde Power BI Desktop

1. *Obtener datos* > *Base de datos PostgreSQL*.
2. **Servidor:** el host que entrega el docente (por ejemplo, `ep-xxxx.region.aws.neon.tech`). **Base de datos:** la que indique el docente.
3. Modo **Importar** (recomendado para el curso; vea la [práctica 06](../../practicas-powerbi/06_fuentes_organizacionales/README.md)).
4. Credenciales: pestaña *Base de datos*, con el usuario `equipoNN` y la clave del equipo.
5. Si aparece un error de conexión, revise la sección de problemas frecuentes de la práctica 06.

**Nunca** escriba la clave dentro de una consulta, en el `.pbix` que entrega ni en el informe. Power BI la guarda aparte, en la configuración de origen de datos del equipo.
