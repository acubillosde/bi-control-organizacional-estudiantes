# Avance 1 · Integración de fuentes, limpieza y modelo de datos

**Peso:** 7.5% · **RA:** RA1 · **Horas estimadas:** 6 h de equipo (semana 3) · **Fecha límite:** miércoles de la semana 3, 23:59 (antes del S2)

> **Rama `fuentes-organizacionales`.** En esta versión del curso, los datos del caso no son CSV listos. Están en los sistemas de COAGUA, descritos en el [mapa de sistemas](../datos/sistemas/README.md): un ERP en PostgreSQL, el Excel de Finanzas, los extractos del banco, las facturas electrónicas y la API de TRM.

## Enunciado
Construya la base técnica del tablero de COAGUA. Necesita una canalización ETL reproducible que integre las fuentes de la organización y un modelo de datos que permita responder preguntas de control sobre pagos, pagos frente a banco y facturas, y cartera.

## Entregables
1. **Archivo `.pbix`** con:
   - los parámetros `ServidorERP`, `BaseERP` y `RutaSistemas`, **sin credenciales** dentro de las consultas;
   - **todas** las fuentes integradas:
     - ERP (`erp.pagos`, `erp.terceros`, `erp.centros_costo`, `erp.limites_aprobacion`, `erp.festivos`);
     - cartera (`cartera.creditos`, `cartera.politica_lineas`);
     - presupuesto (Excel);
     - extractos (12 archivos);
     - facturas XML;
     - TRM (API);
   - al menos un paso que se **pliegue** al servidor (evidencia: captura de *Ver consulta nativa*);
   - al menos **3 columnas de control** derivadas, cada una justificada; al menos una debe cruzar dos fuentes;
   - modelo estrella con relaciones correctas y `dCalendario` marcada como tabla de fechas;
   - una página **«Calidad e integración»**: perfilado, tabla de excepciones y **cifras de cuadre entre fuentes** (por ejemplo, total pagado en el ERP frente a total debitado en el banco).
2. **Memoria técnica** (PDF, 4–6 páginas):
   - **requerimientos** obtenidos en la [entrevista](entrevista_requerimientos.md) (media página);
   - **inventario de fuentes:** sistema, dueño, conector, formato, problemas encontrados y cómo se resolvieron;
   - **contraste con el [diccionario de datos](../datos/sistemas/diccionario_erp.md):** afirmaciones del diccionario que los datos contradicen, con evidencia;
   - diagrama del modelo (captura de la vista de modelo);
   - tabla de transformaciones: consulta, transformación, motivo y control que habilita;
   - **tres preguntas de control** que el modelo permite responder, con su respuesta preliminar. Al menos una debe requerir dos fuentes.
3. **Solicitud de acceso a datos** (opcional): si su análisis requiere nómina, adjunte la [solicitud formal](solicitud_acceso_datos.md) que envió y la respuesta que recibió.

## Distribución sugerida del tiempo (6 h)
| Tarea | Horas |
|---|---:|
| Conexión al ERP y a la cartera (práctica 06, pasos 1 y 5) | 1.0 |
| Excel, extractos y XML (práctica 06, pasos 2 a 4) | 1.5 |
| Columnas de control y modelo; cuadre entre fuentes | 1.5 |
| Página de calidad e integración | 0.5 |
| Memoria técnica | 1.5 |

## Rúbrica

| Criterio | Peso | Excelente (4.6–5.0) | Bueno (4.0–4.5) | Básico (3.0–3.9) | Insuficiente (< 3.0) |
|---|---:|---|---|---|---|
| Integración de fuentes y ETL reproducible | 25% | Las 6 fuentes integradas con parámetros, sin credenciales en el código; resuelve los cambios de formato, las unidades y las hojas ocultas; evidencia de plegado | Todas las fuentes, con un problema de lectura menor sin resolver | Falta una fuente o hay errores de lectura que alteran los totales | Faltan varias fuentes o el archivo no carga |
| Columnas de control | 15% | 3 o más columnas originales justificadas; al menos una cruza fuentes y está vinculada a un riesgo | 3 columnas con justificación general | Columnas copiadas de la práctica | Sin columnas de control |
| Modelo de datos | 20% | Estrella correcta, cardinalidades y direcciones justificadas, relación inactiva usada con criterio | Estrella correcta con detalles menores | Relaciones con errores que no alteran los totales | Modelo que produce totales erróneos |
| Calidad, cuadre y diccionario | 20% | Cuadre entre fuentes cuantificado; al menos 4 contradicciones del diccionario con evidencia; excepciones clasificadas (calidad frente a control) | Cuadre presente y 2–3 contradicciones | Perfilado sin cuadre entre fuentes | Ausente |
| Requerimientos, gobierno y memoria | 20% | Requerimientos trazados a la entrevista; supuestos explícitos; si hubo solicitud de acceso, aplica el mínimo privilegio; 3 preguntas de control relevantes y cuantificadas | Requerimientos genéricos; memoria clara | Memoria incompleta o sin requerimientos | Ausente |
