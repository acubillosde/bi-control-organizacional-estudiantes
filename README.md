# Inteligencia de Negocios para el Control Organizacional

**Seminario de Interacción 7 – Inteligencia de Negocios** · Maestría en Control Organizacional
2 créditos · 96 horas (24 presenciales en 3 sábados + 72 de trabajo independiente) · Power BI


## Presentación
Este curso forma a profesionales del control, la auditoría y el aseguramiento para **diseñar, implementar y comunicar soluciones de inteligencia de negocios** que permitan monitorear riesgos, detectar anomalías y apoyar las decisiones de los órganos de control. Se aprende haciendo: a lo largo de siete semanas, cada equipo construye en Power BI un tablero de control interno para una cooperativa agrofinanciera ficticia (COAGUA), con datos sintéticos que contienen irregularidades por descubrir, y lo sustenta ante un comité de auditoría.

## Resultados de aprendizaje
1. **RA1.** Diseñar y aplicar modelos de BI orientados al control organizacional, integrando extracción, transformación y visualización de datos.
2. **RA2.** Implementar dashboards e indicadores clave de control interno para monitorear riesgos, detectar anomalías y evaluar el cumplimiento normativo.
3. **RA3.** Analizar y comunicar hallazgos con analítica descriptiva, predictiva y prescriptiva, con recomendaciones para la auditoría, el aseguramiento y la gestión de riesgos.


## Unidades
| Unidad | Sesión | Tema |
|---|---|---|
| [U1](unidad-1/README.md) | Sábado 1 | BI y Business Analytics: ETL, data warehouse, BI vs. BA, CRISP-DM |
| [U2](unidad-2/README.md) | Sábados 1–2 | BI en el control organizacional: gobierno y calidad de datos, KPIs, cuadro de mando |
| [U3](unidad-3/README.md) | Sábado 2 | Visualización y comunicación: principios, storytelling, órganos de control |
| [U4](unidad-4/README.md) | Sábado 3 | Analítica para el aseguramiento: Benford, duplicados, Isolation Forest, COSO, ISO 31000 |

## Cómo usar este repositorio
1. Lea el [syllabus](syllabus/syllabus.md) y la [ruta semanal](cronograma/trabajo_independiente.md).
2. Instale Power BI según [`recursos/instalacion.md`](recursos/instalacion.md) (incluye alternativas para Mac).
3. Descargue el repositorio. Los datos están en [`datos/`](datos/README.md).
4. Siga las [prácticas de Power BI](practicas-powerbi/README.md) en orden y las actividades de cada unidad.
5. Dudas: abra un *Issue* con la etiqueta adecuada (ver [plan de seguimiento](cronograma/plan_seguimiento.md)).

## Estructura
```
syllabus/              Syllabus, tabla de carga y matriz de alineación
cronograma/            Agenda de cada sábado, ruta semanal, plan de seguimiento
unidad-1/ … unidad-4/  Lecturas y actividades por unidad
lecturas/              Bibliografía por unidad (obligatoria, complementaria, propuesta)
casos/                 Guías de discusión de los casos
caso-integrador/       Enunciado, avances, entrega final y rúbricas
practicas-powerbi/     Power Query (M), modelo, DAX, dashboards, Python/R
datos/                 Datasets sintéticos (CSV) y, en sistemas/, las fuentes de los sistemas de COAGUA
scripts/               Detección de anomalías y modelo de crédito (Python)
evaluacion/            Rúbricas, criterios y quices
recursos/              Instalación y enlaces verificados
```

## Requisitos
- Computador con Windows y **Power BI Desktop** (gratuito) o una de las alternativas para Mac.
- Excel (tablas dinámicas) y PowerPoint, según el syllabus oficial.
- Conexión a internet para la base de datos del ERP y la API de TRM (rama `fuentes-organizacionales`). El docente entrega a cada equipo un usuario de solo lectura.
- *Opcional (profundización C):* Python 3.10 o superior con `pip install -r scripts/requirements.txt`, o R.

Ninguna actividad requiere licencias de pago.

## Datos y derechos
- Todos los datos son **sintéticos**: no corresponden a ninguna entidad ni persona real. La única excepción es la TRM, que es la tasa oficial publicada en datos.gov.co.
- Este repositorio no reproduce textos con derechos de autor. Los artículos y casos se consultan en la Biblioteca de la Universidad.
