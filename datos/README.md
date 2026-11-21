# Datos del curso (sintéticos)

> **Todos los datos son ficticios.** Fueron generados por script con una semilla fija. No contienen información de ninguna entidad, persona, proveedor ni cliente real; cualquier coincidencia de nombres o números es accidental. Los bancos se llaman "Banco Alfa", "Banco Beta", etc. Los NIT y las cuentas son números aleatorios.

## Organización ficticia

**Cooperativa Agrofinanciera Los Guaduales (COAGUA)**: cooperativa de ahorro y crédito orientada a productores agropecuarios, con sede en Bogotá D.C. y oficinas en Meta, Huila, Tolima, Córdoba, Casanare, Risaralda y Cauca. Tiene 60 empleados, 184 proveedores, cerca de 6.300 pagos en 2025 y una cartera de 3.200 créditos agropecuarios. La narrativa completa está en el [enunciado del caso integrador](../caso-integrador/README.md).

Los datos **contienen irregularidades** de control interno y de calidad. Encontrarlas, cuantificarlas y explicarlas es el trabajo del curso.

## `sistemas/` (rama `fuentes-organizacionales`)
Las fuentes del caso integrador tal como existen en COAGUA: ERP en PostgreSQL, Excel de Finanzas, extractos bancarios, facturas XML y API de TRM. Vea el [mapa de sistemas](sistemas/README.md).

## `integrador/`

| Archivo | Filas | Descripción |
|---|---:|---|
| `pagos.csv` | ≈ 6.300 | Pagos a proveedores, 2025 |
| `proveedores.csv` | 184 | Maestro de proveedores |
| `empleados.csv` | 60 | Empleados y usuarios del sistema |
| `centros_costo.csv` | 12 | Centros de costo |
| `presupuesto.csv` | 144 | Presupuesto mensual por centro de costo |
| `creditos.csv` | 3.200 | Cartera de créditos agropecuarios |
| `limites_aprobacion.csv` | 5 | Política (ficticia) de atribuciones de aprobación por cargo |
| `politica_lineas_credito.csv` | 7 | Política (ficticia) de topes y tasas por línea de crédito |
| `festivos.csv` | 89 | Festivos de Colombia 2022–2026, calculados según la Ley 51 de 1983 y las fechas religiosas móviles |

### `pagos.csv`
| Campo | Tipo | Descripción |
|---|---|---|
| `id_pago` | texto | Identificador del pago (PG000001…) |
| `id_proveedor` | texto | Proveedor (→ `proveedores.csv`) |
| `numero_factura` | texto | Número de la factura del proveedor |
| `fecha_factura`, `fecha_registro`, `fecha_aprobacion`, `fecha_pago` | fecha (aaaa-mm-dd) | Fechas del ciclo de pago |
| `id_centro_costo` | texto | Centro de costo (→ `centros_costo.csv`) |
| `valor` | entero (COP) | Valor pagado |
| `medio_pago` | texto | Transferencia o cheque |
| `usuario_registra`, `usuario_aprueba` | texto | Usuarios del sistema (→ `empleados.usuario_sistema`) |

### `proveedores.csv`
`id_proveedor`, `nit` (9 dígitos), `dv` (dígito de verificación), `razon_social`, `categoria`, `ciudad`, `departamento`, `banco`, `cuenta_bancaria`, `fecha_creacion`, `creado_por`, `estado`.

### `empleados.csv`
`id_empleado`, `nombre`, `cargo` (Analista, Coordinador, Jefe, Director, Gerente), `area`, `usuario_sistema`, `banco`, `cuenta_bancaria`, `fecha_ingreso`.

### `creditos.csv`
| Campo | Descripción |
|---|---|
| `id_credito`, `id_cliente` | Identificadores |
| `municipio`, `departamento` | Ubicación del productor |
| `linea` | Café, Arroz, Ganadería bovina, Cacao, Aguacate, Maíz, Palma |
| `fecha_desembolso`, `monto_desembolsado`, `saldo_capital` | Condiciones del crédito (COP) |
| `tasa_ea` | Tasa efectiva anual en decimal (0.18 = 18%) |
| `plazo_meses`, `garantia` | Condiciones |
| `score_buro` | Puntaje de buró **ficticio** (350–900) |
| `antiguedad_cliente_anios` | Años como asociado |
| `id_asesor` | Asesor comercial |
| `dias_mora` | Días de mora a la fecha de corte |
| `calificacion` | Calificación registrada (A–E) |
| `incumplimiento_12m` | 1 si el crédito incumplió en los 12 meses posteriores al desembolso (variable objetivo para ML) |

**Política interna ficticia de calificación por mora:** A 0–30 días, B 31–60, C 61–90, D 91–180, E más de 180. *No corresponde a la norma de ninguna superintendencia; es una regla del caso.*
**Límite por cliente (ficticio):** 300 millones de saldo total.

## `profundizacion/`

| Archivo | Filas | Uso |
|---|---:|---|
| `clientes_maestro.csv` | ≈ 1.250 | Extensión opcional de la profundización A: perfilado de calidad y gobierno de datos |
| `gastos_viaje_retail.csv` | ≈ 2.550 | Profundización B: gastos de viaje de "Almacenes Mirador" (cadena de retail ficticia) |

`gastos_viaje_retail.csv`: `id_gasto`, `id_empleado`, `fecha`, `ciudad`, `categoria` (Hotel, Alimentación, Transporte aéreo, Taxi), `valor`, `numero_recibo`, `tope_politica`, `aprobado_por`.

## `resultados/` (precalculados)
Salidas de `scripts/deteccion_anomalias.py` y `scripts/modelo_credito.py`: `alertas_pagos.csv`, `puntaje_pagos.csv`, `benford_resumen.csv` y `creditos_puntaje.csv`. Se incluyen en el repositorio para quien no tenga Python (por ejemplo, en Mac). Al volver a ejecutar los scripts se regeneran.

## Reproducibilidad
Los datos se generaron con semilla fija. **No modifique los CSV**: todos los equipos deben trabajar sobre los mismos datos para que los resultados sean comparables.
