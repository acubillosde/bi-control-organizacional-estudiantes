# Prácticas de Power BI

Power BI Desktop es la herramienta única de visualización del curso. Este repositorio **no incluye archivos `.pbix`**: cada estudiante construye el suyo a partir de los scripts y guías siguientes. Así se aprende el proceso completo y se evitan problemas de versiones.

| # | Práctica | Contenido | Unidad | Actividades |
|---|---|---|---|---|
| 01 | [Power Query (M)](01_power_query/README.md) | Parámetro de ruta, función de lectura, dimensiones, hechos, calendario con festivos, tabla de excepciones | U1, U2 | L1, T1, AV1 |
| 02 | [Modelo de datos](02_modelo_datos/README.md) | Esquema estrella, relaciones activas e inactivas, tabla de fechas | U2 | L2, T2, AV1 |
| 03 | [Medidas DAX](03_dax/README.md) | 46 medidas: volumen, presupuesto, controles, Benford, alertas, cartera, titulares | U2, U4 | L2, T2, T4, AV2 |
| 04 | [Dashboards y storytelling](04_dashboards/README.md) | Estructura de 4 páginas, lista de verificación de visualización, clínica del mal tablero, guion | U3 | L2, T3, AV2 |
| 05 | [Python y R en Power BI](05_python_r/README.md) | Isolation Forest y regresión logística; precálculo vs. script en Power Query | U4 | L3, PC |
| 06 | [Fuentes organizacionales](06_fuentes_organizacionales/README.md) | PostgreSQL en la nube, plegado de consultas, Excel con hojas ocultas, carpeta de extractos con dos formatos, XML, API web | U2 | AV1 (rama `fuentes-organizacionales`) |
| 07 | [Seguridad por filas](07_seguridad_filas/README.md) | Roles estáticos y dinámicos, `USERPRINCIPALNAME`, *Ver como*, publicación | U3 | AV2, EF (rama `fuentes-organizacionales`) |

**Orden de trabajo:** 01 → 02 → 03 → 04 → 05. En la rama `fuentes-organizacionales`: 01 → 06 → 02 → 03 → 04 → 07 → 05. Los datos están en [`../datos/`](../datos/README.md).
