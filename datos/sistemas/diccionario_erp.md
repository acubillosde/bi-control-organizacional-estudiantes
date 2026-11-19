# Diccionario de datos del ERP · COAGUA

> Documento de la Dirección de Tecnología (ficticio), versión 1.3, última actualización: marzo de 2024.
> **Nota del curso:** este diccionario es parte del caso. Como en muchas organizaciones, la documentación puede estar desactualizada o equivocada. Contraste cada afirmación con los datos y registre las diferencias en la memoria técnica.

## Esquema `erp`

### `erp.terceros` · maestro de proveedores
| Campo | Tipo | Descripción |
|---|---|---|
| `cod_tercero` | texto | Código interno del tercero (P0001…). Llave primaria |
| `nit`, `dv` | texto, entero | NIT sin dígito de verificación y dígito de verificación |
| `razon_social` | texto | Nombre registrado |
| `pais` | texto | País del tercero |
| `categoria` | texto | Categoría de compra |
| `ciudad`, `departamento` | texto | Ubicación |
| `banco`, `cuenta_bancaria` | texto | Cuenta inscrita para pagos |
| `fec_creacion`, `usr_creacion` | fecha, texto | Alta del tercero y usuario que la hizo |
| `estado` | texto | `ACTIVO` o `INACTIVO` |
| `fec_inactivacion` | fecha | Fecha desde la cual el tercero queda inactivo. **El sistema no permite registrar pagos a terceros inactivos** |

### `erp.pagos` · pagos a proveedores
| Campo | Tipo | Descripción |
|---|---|---|
| `id_pago` | texto | Consecutivo del pago. Llave primaria |
| `cod_tercero` | texto | → `erp.terceros` |
| `num_factura` | texto | Número de la factura del proveedor, tal como se digitó |
| `fec_factura`, `fec_registro`, `fec_aprobacion`, `fec_pago` | fecha | Ciclo del pago |
| `cod_ccosto` | texto | → `erp.centros_costo` |
| `vlr_pago` | decimal | Valor pagado en pesos colombianos, IVA incluido |
| `moneda` | texto | Moneda del pago. **Todos los pagos de COAGUA se hacen en COP** |
| `vlr_moneda_ext`, `trm_aplicada` | decimal | Reservados para uso futuro |
| `medio_pago` | texto | `Transferencia` o `Cheque` |
| `num_documento` | texto | Número de la transferencia (`TR-`) o del cheque (`CH-`) que reporta el banco |
| `usr_registra`, `usr_aprueba` | texto | Usuarios del sistema. **El ERP impide que el mismo usuario registre y apruebe un pago** |
| `estado` | texto | Estado del pago. **Los pagos anulados se eliminan de la tabla en el cierre diario** |
| `fec_anulacion` | fecha | Ver `estado` |

### `erp.centros_costo`
`cod_ccosto`, `nombre`, `regional`.

### `erp.limites_aprobacion`
`cargo`, `limite_aprobacion` (COP). Política de atribuciones por cargo.

### `erp.festivos`
`fecha`, `nombre`. Festivos de Colombia, 2022–2026.

## Esquema `cartera`
- `cartera.creditos`: mismos campos que `creditos.csv` (vea [`datos/README.md`](../README.md)).
- `cartera.politica_lineas`: `linea`, `monto_maximo`, `tasa_min_ea`, `tasa_max_ea`.

## Esquema `nomina` (acceso restringido)
- `nomina.v_empleados_control`: `id_empleado`, `cargo`, `area`, `usuario_sistema`, `banco`, `cuenta_bancaria`, `fec_ingreso`. Sin nombres ni datos de contacto.
- La tabla `nomina.empleados` no está disponible para consulta.

## Esquema `gobierno`
- `gobierno.usuarios_tablero`: `correo`, `rol`, `regional` (`Todas` o el nombre de la regional). Correos ficticios del dominio reservado `coagua.example`.
