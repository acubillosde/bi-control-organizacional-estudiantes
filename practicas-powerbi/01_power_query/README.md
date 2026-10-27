# Práctica 01 · ETL con Power Query

**Unidad:** U1 (y U2 para calidad de datos) · **RA:** RA1, RA2 · **Se usa en:** Laboratorio L1 (S1), Taller T1, Avance 1
**Tiempo estimado:** 110 minutos en clase + 3 h en el T1

## Objetivo

Construir una canalización ETL reproducible que cargue los datos de COAGUA, les asigne tipos, derive columnas de control y genere una tabla calendario con festivos y una tabla de excepciones de calidad.

## Paso a paso

1. **Parámetro de ruta.** *Inicio → Transformar datos → Administrar parámetros → Nuevo*. Nombre: `RutaDatos`, tipo: Texto, valor: la ruta de la carpeta `datos\` terminada en `\`. Así el archivo funciona en cualquier equipo con solo cambiar el parámetro.
2. **Función auxiliar.** Cree una consulta en blanco llamada `fnLeerCsv` y pegue el primer bloque de [`consultas.m`](consultas.m). Todas las tablas usan esta función. Se escribe una sola vez y se reutiliza (principio DRY).
3. **Dimensiones.** Cree, en este orden, `dFestivos`, `dCalendario`, `dEmpleados`, `dProveedores` y `dCentrosCosto`. El orden importa porque `dCalendario` usa `dFestivos` y `dProveedores` usa `dEmpleados`.
4. **Hechos.** Cree `fPagos`, `fPresupuesto` y `fCreditos`. Revise en la barra de pasos aplicados cada columna derivada y explique **qué control de auditoría habilita**:

   | Columna | Control que habilita |
   |---|---|
   | `factura_normalizada` | Duplicados aproximados |
   | `primer_digito` | Ley de Benford |
   | `mismo_usuario` | Segregación de funciones |
   | `limite_aprobador`, `sobre_limite` | Cumplimiento de la política de atribuciones |
   | `monto_redondo` | Montos redondos (prueba de razonabilidad) |
   | `calificacion_esperada` | Coherencia entre la mora y la calificación de cartera |
   | `fuera_de_politica` | Topes de monto y rangos de tasa por línea |

5. **Perfilado (L1, parte 2).** *Vista → Calidad de columna, Distribución de columnas y Perfil de columna*. Por defecto el perfilado usa las primeras 1.000 filas: cámbielo a "basado en todo el conjunto de datos" en la barra de estado. Anote en una tabla los porcentajes de válidos, errores y vacíos de las columnas clave.
6. **Tabla de excepciones.** Cree `tExcepcionesCalidad` (último bloque). Responda: ¿cuántos registros incumplen cada regla? ¿Cuál es un problema de calidad del dato y cuál es un posible problema de control?
7. **Cargar.** *Cerrar y aplicar*. Desactive la carga de `fnLeerCsv`, que es una función, no una tabla.
8. *(Opcional, después del T4)* Ejecute `python scripts/deteccion_anomalias.py` para generar `datos/resultados/` y cree `fAlertas` y `fPuntajePagos`.

## Entregable del L1
`.pbix` con todas las consultas y una tabla (en una página del informe o en un comentario) con los resultados del perfilado y del paso 6.

## Si algo falla
- **"No se encontró el archivo"**: revise que `RutaDatos` termine en `\` y que no tenga comillas de más.
- **Las fechas aparecen como texto o con error**: las fechas vienen en formato ISO (`aaaa-mm-dd`). Use el paso `Table.TransformColumnTypes` del script, no la detección automática.
- **`tasa_ea` sale multiplicada por 10.000**: falta el argumento de referencia cultural `"en-US"` en el cambio de tipo, que se usa para leer el punto decimal.
