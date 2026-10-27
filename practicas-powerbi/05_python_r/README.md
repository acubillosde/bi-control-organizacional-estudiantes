# Práctica 05 · Modelos de Python y R consumidos desde Power BI

**Unidad:** U4 · **RA:** RA3 · **Se usa en:** L3 (S3), profundización C

Hay tres formas de llevar un modelo de aprendizaje automático (ML) a Power BI. El curso usa las dos primeras.

| Opción | Cómo | Cuándo usarla |
|---|---|---|
| A. Precalcular fuera de Power BI | Ejecutar `scripts/deteccion_anomalias.py` o `scripts/modelo_credito.py` y cargar el CSV resultante (`datos/resultados/`) | Recomendada. Es reproducible y no depende de la configuración de Python en Power BI |
| B. Script en Power Query | *Transformar → Ejecutar script de Python/R* sobre una consulta | Para demostrar la integración. Requiere Python o R instalado y configurado |
| C. Visual de Python/R | Visual que ejecuta código con los campos seleccionados | Solo para gráficos especializados. No sirve para alimentar medidas |

## Opción A (todos)
```bash
pip install -r scripts/requirements.txt
python scripts/deteccion_anomalias.py      # genera alertas_pagos.csv, puntaje_pagos.csv, benford_resumen.csv
python scripts/modelo_credito.py           # genera creditos_puntaje.csv
```
Luego, en Power Query, cree `fAlertas` y `fPuntajePagos` (ver `01_power_query/consultas.m`) y una consulta análoga para `creditos_puntaje.csv`, relacionada 1:1 con `fCreditos`.

## Opción B · Python (profundización C)
1. *Archivo → Opciones y configuración → Opciones → Scripts de Python*: seleccione su instalación de Python, que debe tener pandas y scikit-learn.
2. Duplique la consulta `fPagos` y llámela `fPagosIF`.
3. *Transformar → Ejecutar script de Python* y pegue [`isolation_forest_powerquery.py`](isolation_forest_powerquery.py).
4. En la tabla resultante, expanda `resultado`.
5. Relacione `fPagosIF[id_pago]` con `fPagos[id_pago]` (1:1).

## Opción B · R (alternativa)
Igual que la anterior, sobre `fCreditos` y con [`regresion_logistica_powerquery.R`](regresion_logistica_powerquery.R). Solo requiere R base.

## Limitaciones que debe conocer el estudiante
- Los scripts de Python y R en Power Query se ejecutan **en el equipo local**. Para actualizar en Power BI Service se requiere una puerta de enlace personal (*gateway*), y sus condiciones dependen de la licencia (**pendiente de verificación** con la documentación vigente de Microsoft).
- Power BI aplica límites de tiempo y de tamaño a la ejecución de scripts. Por eso la opción A es la recomendada para datasets grandes.
- **Mac:** las opciones B y C solo funcionan dentro de Power BI Desktop (Windows o máquina virtual). La opción A funciona en cualquier sistema.

## Profundización C · Enunciado
Ver [`unidad-4/actividades.md#pc`](../../unidad-4/actividades.md#pc).
