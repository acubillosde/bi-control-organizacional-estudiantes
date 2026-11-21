# Caso integrador · Tablero de control interno de COAGUA

**Componente oficial:** caso de estudio con aplicación de minería y analítica, que incluye la generación del informe de resultados (visualización) y las estrategias de mejora (30% de la nota). La sustentación ante el comité cuenta además dentro del componente "Exposiciones" (15%).
**RA:** RA1, RA2, RA3 · **Trabajo en equipo** (4–5 integrantes) · **Horas:** 21 h independientes + 3 h presenciales

## La organización (ficticia)

La **Cooperativa Agrofinanciera Los Guaduales (COAGUA)** ofrece ahorro y crédito a productores de café, arroz, cacao, aguacate, maíz, palma y ganadería en siete departamentos de Colombia. Tiene 60 empleados, alrededor de 180 proveedores y una cartera de 3.200 créditos.

Durante 2025 creció rápido: abrió oficinas, contrató proveedores nuevos de servicios profesionales y tecnología, y su sistema de pagos pasó de aprobaciones en papel a un flujo digital. El **comité de auditoría** del consejo de administración recibió dos comunicaciones:
1. Un informe de la revisoría fiscal que menciona "debilidades en la segregación de funciones del proceso de pagos y en la actualización del maestro de terceros".
2. Una denuncia anónima, sin detalles, sobre "proveedores relacionados con funcionarios".

La gerencia de riesgos, por su parte, está preocupada por el aumento de la mora en algunas líneas y regiones.

El comité contrató a su equipo (consultores de analítica para el control) para:
> **Diseñar e implementar en Power BI un tablero de control interno que permita monitorear los riesgos del proceso de pagos y de la cartera, detectar anomalías y presentar recomendaciones al comité.**

> **La historia completa**, con los personajes, las tensiones entre áreas, el RACI y el plan de siete semanas, está en el [caso narrativo de COAGUA](caso_coagua.md). Léalo antes del lanzamiento del caso (S1): este enunciado sigue siendo el que fija las entregas, los pesos y las rúbricas.

## Datos
**Rama `fuentes-organizacionales`:** los datos están en los sistemas de COAGUA. Hay un ERP en PostgreSQL en la nube, el Excel de Finanzas, los extractos del banco, las facturas electrónicas en XML y la API pública de TRM. Vea el [mapa de sistemas](../datos/sistemas/README.md) y el [diccionario de datos del ERP](../datos/sistemas/diccionario_erp.md). Los CSV de [`datos/integrador/`](../datos/README.md) se siguen usando en los laboratorios y talleres, pero el caso integrador se construye sobre las fuentes de los sistemas.

Los datos son sintéticos y contienen irregularidades que el equipo debe descubrir. Algunas solo aparecen al cruzar fuentes. **No se le dirá cuántas ni de qué tipo.**

### Cómo se trabaja en una organización (además de los datos)
- **Entrevista de requerimientos** con control interno en el S1: [guía](entrevista_requerimientos.md).
- **Solicitud formal de acceso** para los datos restringidos (nómina): [formato](solicitud_acceso_datos.md).
- **Cambios de alcance:** el comité puede enviar comunicaciones durante el curso. Incorpórelas en la entrega siguiente.
- **Seguridad por filas:** cada usuario del tablero ve solo lo que le corresponde ([práctica 07](../practicas-powerbi/07_seguridad_filas/README.md)).

## Entregas

| Entrega | Semana | Contenido | Peso | Enunciado |
|---|---|---|---:|---|
| Avance 1 | 3 (miércoles) | Extracción, limpieza y modelo de datos | 7.5% | [avance_1.md](avance_1.md) |
| Avance 2 | 4 (sábado) | Dashboard de control con KPIs y storytelling | 7.5% | [avance_2.md](avance_2.md) |
| Sustentación ante el comité | S3 | Presentación ejecutiva de 12' + 10' de preguntas | 15% (componente Exposiciones) | [entrega_final.md](entrega_final.md#sustentación) |
| Entrega final | 7 (sábado) | Tablero con detección de anomalías + informe ejecutivo | 15% | [entrega_final.md](entrega_final.md) |

## Reglas generales
- Formato de archivos: `Equipo<N>_<Entrega>.pbix` y `Equipo<N>_<Entrega>.pdf`.
- El `.pbix` debe abrir con solo cambiar el parámetro `RutaDatos` (en la rama `fuentes-organizacionales`: `ServidorERP`, `BaseERP` y `RutaSistemas`). Nunca incluya credenciales en las consultas ni en los informes.
- Todo uso de IA generativa debe declararse en el anexo de la entrega.
- Los datos son ficticios: **no** atribuya los hallazgos a entidades reales ni los umbrales del caso a normas reales.
