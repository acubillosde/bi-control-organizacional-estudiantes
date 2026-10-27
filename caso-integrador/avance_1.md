# Avance 1 · Extracción, limpieza y modelo de datos

**Peso:** 7.5% · **RA:** RA1 · **Horas estimadas:** 6 h de equipo (semana 3) · **Fecha límite:** miércoles de la semana 3, 23:59 (antes del S2)

## Enunciado
Construya la base técnica del tablero de COAGUA: una canalización ETL reproducible y un modelo de datos que permita responder preguntas de control sobre pagos y cartera.

## Entregables
1. **Archivo `.pbix`** con:
   - parámetro `RutaDatos` y consultas de Power Query para las 9 tablas de `datos/integrador/` (pueden partir de la práctica 01);
   - al menos **3 columnas de control** derivadas en Power Query, además de las de la práctica, cada una justificada;
   - modelo estrella con relaciones correctas y `dCalendario` marcada como tabla de fechas;
   - una página "Calidad de datos" con el perfilado y la tabla de excepciones.
2. **Memoria técnica** (PDF, 3–5 páginas):
   - diagrama del modelo (captura de la vista de modelo);
   - tabla de transformaciones: consulta, transformación, motivo y control que habilita;
   - hallazgos de calidad: qué problemas se encontraron y cómo se trataron (corregir, excluir o marcar);
   - **tres preguntas de control** que el modelo permite responder, con su respuesta preliminar.

## Distribución sugerida del tiempo (6 h)
| Tarea | Horas |
|---|---:|
| Completar el ETL a partir de T1 | 1.5 |
| Columnas de control adicionales | 1.0 |
| Modelo y validación de totales | 1.5 |
| Página de calidad | 0.5 |
| Memoria técnica | 1.5 |

## Rúbrica

| Criterio | Peso | Excelente (4.6–5.0) | Bueno (4.0–4.5) | Básico (3.0–3.9) | Insuficiente (< 3.0) |
|---|---:|---|---|---|---|
| ETL reproducible | 25% | Parámetro de ruta, función reutilizable, tipos explícitos; abre en otro equipo sin errores | Reproducible con ajustes menores | Funciona solo en el equipo del autor | No carga o faltan tablas |
| Columnas de control | 20% | 3 o más columnas originales, bien justificadas y vinculadas a riesgos | 3 columnas con justificación general | Columnas copiadas de la práctica | Sin columnas de control |
| Modelo de datos | 25% | Estrella correcta, cardinalidades y direcciones justificadas, relación inactiva usada con criterio | Estrella correcta con detalles menores | Relaciones con errores que no alteran los totales | Modelo que produce totales erróneos |
| Calidad de datos | 15% | Perfilado completo, excepciones clasificadas (calidad vs. control) y tratamiento justificado | Perfilado completo sin clasificación | Perfilado parcial | Ausente |
| Memoria y preguntas de control | 15% | Clara, concisa, con 3 preguntas relevantes y respuestas cuantificadas | Clara, con preguntas genéricas | Incompleta | Ausente |
