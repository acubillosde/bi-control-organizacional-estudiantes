# Práctica 03 · Medidas DAX de control

**Unidad:** U2 (y U4 para Benford y alertas) · **RA:** RA1, RA2 · **Se usa en:** L2, T2, T4, Avance 2, entrega final

Todas las medidas están en [`medidas.dax`](medidas.dax), organizadas en 7 carpetas. Esta guía explica los conceptos que el estudiante debe dominar. No basta con copiar.

## Conceptos clave

| Concepto | Dónde se ve | Pregunta de comprensión |
|---|---|---|
| Medida vs. columna calculada | `Total pagado` vs. `fPagos[mismo_usuario]` (creada en Power Query) | ¿Por qué el % de pagos sin segregación debe ser una medida? |
| `DIVIDE` | Todos los porcentajes | ¿Qué devuelve `DIVIDE` si el denominador es 0? ¿Por qué es preferible al operador `/`? |
| `CALCULATE` y la transición de contexto | `Pagos en día no hábil`, `Pagos en grupos duplicados` | ¿Por qué `CALCULATE(COUNTROWS(fPagos))` dentro de `ADDCOLUMNS` cuenta por grupo? |
| Relación inactiva | `Total pagado por fecha de aprobación` | ¿En qué pregunta de auditoría importa la fecha de aprobación y no la de pago? |
| Inteligencia de tiempo | `Var % mensual pagado` | ¿Qué requisito del modelo hace que funcione `DATEADD`? |
| Iteradores (`SUMX`, `AVERAGEX`) | Duplicados, `MAD Benford` | ¿Qué fila recorre `AVERAGEX` en la MAD? |
| `TREATAS` | `Valor de pagos con alerta` | ¿Qué pasaría sin `TREATAS` si un pago tiene 3 alertas? |
| Medidas de texto | `Titular alertas` | ¿Cómo apoyan el storytelling los titulares dinámicos? |

## Taller T2 · Medidas mínimas

Implemente y documente en un diccionario (nombre, fórmula, interpretación, umbral) al menos estas 10 medidas: `Total pagado`, `N° pagos`, `Ejecución presupuestal %`, `% pagos en día no hábil`, `% pagos sin segregación`, `Pagos antes de aprobación`, `Pagos sobre límite de aprobación`, `Pagos en grupos duplicados`, `Indicador de cartera vencida` y `Concentración top 10 clientes`.

## Validación cruzada
Verifique en una tabla de Power BI que `N° pagos` total coincide con el número de filas de `pagos.csv` (ver Excel del T0). Si no coincide, el modelo tiene un problema de relaciones o de carga.
