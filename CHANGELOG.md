# CHANGELOG


## 2026-11-26 · Tiendas Aurora es el eje de las clases

- El [cronograma](cronograma/sabado_1.md) de los tres sábados indica en qué actividades Aurora es el ejemplo que se resuelve antes de aplicar el método a COAGUA.


## 2026-11-26 · Las verificaciones de Aurora en Python pasan a un cuaderno y se corrigen 14 pagos

- **Cuaderno [`casos/verificacion_aurora.ipynb`](casos/verificacion_aurora.ipynb)** en lugar del script `verificacion_aurora.py`: una celda de Python por cada verificación (V01 a V17), con espacio para la predicción y la conclusión. Se abre en Jupyter, VS Code o Colab; en Colab lee los datos directamente desde GitHub. La guía de verificación, las diapositivas y los README ya apuntan al cuaderno.
- **Fechas corregidas en 14 pagos de Aurora** (`datos/demo_aurora/pagos.csv`): los aprobados en fin de semana tenían la factura posterior al registro (9 casos) y el pago lejos de la aprobación. Solo cambian esas 14 filas; las cifras del caso (marzo, hallazgos, V01 a V17) quedan iguales y el promedio de días de factura a pago pasa de 16,218 a 16,240.


## 2026-11-25 · Aurora en una base de datos PostgreSQL (rama `fuentes-organizacionales`)

- Tiendas Aurora pasa de seis CSV a la misma base PostgreSQL de COAGUA, en dos esquemas: `aurora_crudo` (los CSV tal cual, el «antes») y `aurora` (modelo limpio con llaves, restricciones, vistas y roles, el «después»). Los hallazgos del caso quedan anotados en `aurora.bitacora_calidad` y nada se borra.
- Nueva guía para estudiantes [`casos/aurora_base_de_datos.md`](casos/aurora_base_de_datos.md): consultas SQL que reproducen los hallazgos de las verificaciones, con los valores esperados.


## 2026-11-25 · Las verificaciones de Aurora también se contrastan en Python

- Nuevo [`casos/verificacion_aurora.ipynb`](casos/verificacion_aurora.ipynb): ejecuta en pandas las 17 verificaciones (V01 a V17) sobre `datos/demo_aurora/`, una celda por verificación (antes era un script `.py`; ver la entrada del 26 de noviembre). Power BI y Python son herramientas independientes: si coinciden, la cifra es confiable; si no, el estudiante busca cuál tiene el error.
- La guía [`verificacion_aurora.md`](casos/verificacion_aurora.md) agrega el paso «Contraste con Python» y un bloque de código por verificación. Los README de las unidades 1 a 4 y `caso_tiendas_aurora.md` lo mencionan.


## 2026-11-25 · Verificación en Power BI de los hechos de Aurora

- Nueva guía [`casos/verificacion_aurora.md`](casos/verificacion_aurora.md): 17 verificaciones (V01 a V17) para que el estudiante compruebe en su Power BI cada hecho de Aurora, con ciclo prediga → construya → compare → concluya. Trae pasos, Power Query (M), medidas DAX, una pista si no coincide y, al final, los valores esperados. Los valores salen de los datos.
- `caso_aurora.md` y los README de las unidades 1 a 4 enlazan la guía.


## 2026-11-25 · Tiendas Aurora pasa a su propia presentación


## 2026-11-25 · L1: el diagnóstico y el plan se demuestran antes de hacerlos


## 2026-11-25 · Caso de demostración: Tiendas Aurora

<!-- REPO:ESTUDIANTES -->
Nuevo caso ficticio de demostración, [Tiendas Aurora](casos/caso_tiendas_aurora.md) (cadena de 12 tiendas de barrio), con sus datos en `datos/demo_aurora/`. El docente lo usa para mostrar cada concepto aplicado; el caso integrador sigue siendo COAGUA, que cada equipo trabaja por su cuenta.
<!-- /REPO:ESTUDIANTES -->


## 2026-11-25 · Se elimina el caso SYSCO

<!-- REPO:ESTUDIANTES -->
La sesión de casos del S1 usa la Distribuidora Andina (ficticio) y la DIARI. Se retira la guía del caso SYSCO y sus referencias.
<!-- /REPO:ESTUDIANTES -->


## [rama fuentes-organizacionales] · 2026-11-19 · Caso integrador con los sistemas de una organización

<!-- REPO:ESTUDIANTES -->
El caso integrador se trabaja con las fuentes de los sistemas de COAGUA: un ERP en PostgreSQL, el Excel de Finanzas, los extractos bancarios, las facturas XML y la API de TRM. Se agregan una entrevista de requerimientos, una solicitud formal de acceso a datos y la seguridad por filas. Nuevas prácticas 06 y 07; el Avance 1 y el Avance 2 se actualizaron.
<!-- /REPO:ESTUDIANTES -->


## [1.0.0] · 2026-10-27 · Primera versión del curso rediseñado

### Fuente
- Se transcribió el syllabus institucional (PDF de 7 páginas con capa de texto; no requirió OCR) a `fuentes/syllabus_original.md`, que es la fuente de verdad. Se eliminaron el código de formato institucional de cada página y los saltos de línea que partían palabras y URL, y se reconstruyeron las tablas.
- `fuentes/` está excluida de ambos repositorios (`.gitignore`) porque contiene el PDF institucional.
- **No existía `fuentes/contexto_chat.md`**, por lo que no fue posible contrastar la extracción con ese archivo.

### Diferencias con el syllabus oficial y con el encargo de diseño

| # | Tema | Encargo de diseño | Syllabus oficial | Decisión |
|---|---|---|---|---|
| 1 | **Sistema de evaluación** | Talleres 20% · Avances 20% · Tablero final 25% · Sustentación 25% · Quices y participación 10% | Quices 15% · Informe de lectura previa 10% · Talleres y trabajos en clase 20% · Exposiciones 25% · Caso de estudio 30% | **Prevalece el oficial.** Se desagregó así: los avances y el tablero final van dentro de "Caso de estudio"; la sustentación va dentro de "Exposiciones" (15%) junto con la exposición de caso (10%); los talleres autónomos y la profundización van dentro de "Talleres" (20%). La "participación" no tiene peso propio porque el sistema oficial no la contempla |
| 2 | Nombre del curso | "Inteligencia de Negocios para el Control Organizacional" | "Seminario de Interacción 7 – Inteligencia de Negocios" | Se usa el nombre oficial como título y el propuesto como subtítulo |
| 3 | Programa | "Posgrado en analítica aplicada a contabilidad, auditoría y aseguramiento" | "Maestría en Control Organizacional" | Se usa el oficial |
| 4 | Código, prerrequisitos | Extraer del PDF | No figuran | Se registran como "no indicados". Requisitos de entrada: Excel (tablas dinámicas), PowerPoint y portátil |
| 5 | Horario de los sábados | 09:00–17:00 con 1 h de almuerzo = 7 h efectivas (3 × 7 = 21 ≠ 24) | 24 h presenciales | **08:00–17:00** con almuerzo de 12:00 a 13:00 = 8 h efectivas. Las pausas activas de 10' van dentro de los bloques de 2 h. *Debe validarse con la coordinación* |
| 6 | Unidad 4 | Agregar | No existe | Agregada, con la justificación de cubrir RA2 (anomalías) y RA3 (descriptiva, predictiva y prescriptiva) |
| 7 | Herramienta de visualización | Solo Power BI | El material de apoyo incluye el enlace de otra herramienta de visualización | Ese enlace y cualquier mención a esa herramienta fueron **excluidos** de todo el material |
| 8 | Lectura previa Gimenez (2024) | — | Aparece en Metodología, no en la bibliografía | Complementaria, *pendiente de verificación* (sin registro bibliográfico confirmable) |
| 9 | Davenport y Patil | — | Año 2013 | Se corrige a **2012** (HBR, octubre, 90(10), 70–76), verificado |
| 10 | Lluís (2007), páginas | — | "Capítulo 1 pp. 20 a 4…" (truncado en el PDF) | Según el índice del libro, el cap. 1 ocupa las pp. 19–56. Se asignan las pp. 20–45 (estimado) para respetar el tope de lectura previo al S1 |
| 11 | Material de apoyo comercial y antiguo | Marcar | — | Marcado como *contexto histórico* o *complementaria opcional (comercial)* (ver `lecturas/lecturas.md`) |
| 12 | "El lado oscuro de la analítica" | Marcar como "por verificar" | Davenport y Harris (2007) | Marcado **por verificar**. Se halló un posible registro de catálogo, que no se confirma |

### Decisiones de diseño (para validar)
1. **Ventana de 7 semanas**, con S1, S2 y S3 separados por 14 días. Fechas de ejemplo: 20 feb, 6 mar y 20 mar de 2027; entrega final el 3 abr de 2027.
2. **Distribución presencial:** U1 6 h · U2 6 h (2 en el S1 y 4 en el S2) · U3 4 h · U4 5 h · Integrador 3 h.
3. **T4 en aula invertida:** la mecánica de Benford y duplicados se practica antes del S3 para que el sábado se dedique a interpretar y sustentar.
4. **Sustentación en el S3 e informe final después:** el comité retroalimenta en vivo y la versión final incorpora esa retroalimentación (2 semanas después).
5. **Equipos de 4–5 integrantes**, 6 equipos de referencia. Cada caso se trabaja con un equipo expositor y uno de réplica.
6. **Coevaluación** con un factor individual entre 0.8 y 1.0 sobre los componentes grupales.
7. **Organización ficticia:** Cooperativa Agrofinanciera Los Guaduales (COAGUA). Segunda industria (profundización B): retail ("Almacenes Mirador", también ficticia).
8. **Caso colombiano actual** que complementa a SYSCO: la DIARI de la Contraloría General de la República, documentada por la OCDE (2021).
9. **Políticas del caso ficticias:** límites de aprobación, calificación A–E por mora, topes por línea y límite de 300 M por cliente. No se atribuyen a normas reales.
10. **Separación de repositorios:** al de estudiantes no van las guías del docente, las presentaciones, las respuestas, las soluciones, la clave de anomalías, las notas de facilitación, el generador de datos (porque revela la lógica de inyección) ni el script de control de calidad. Los resultados precalculados (`datos/resultados/`) **sí** se publican, para quienes no tienen Python.
11. **Quices** en `evaluacion/quizzes/` (y no dentro de cada unidad) para tener un solo banco. Cada unidad enlaza al suyo.
12. **Docente:** no se incluyó el nombre ni el correo del profesor que registra el PDF. Queda un campo por completar.
13. **Tiempo real (RA2):** cubierto parcialmente, con actualización programada y diseño de monitoreo continuo. El streaming queda fuera de alcance porque requiere licencias.

### Pendientes de verificación
Ver la lista consolidada en [`recursos/enlaces_verificados.md`](recursos/enlaces_verificados.md) (secciones B y C) y en [`lecturas/lecturas.md`](lecturas/lecturas.md). Resumen:
- Número de caso y autoría en el catálogo de HBP: SYSCO, Watson, Ritz-Carlton (autores, año y páginas).
- Autoría de la guía CRISP-DM de IBM atribuida a "Jensen (2016)".
- Gimenez (2024); los dos artículos "buscar en Biblioteca UEC"; editorial de Moreno y Gómez (2021); año, edición y editorial de Hair (2018).
- Davenport y Harris (2007): **por verificar**.
- Páginas estimadas (est.): Ritz-Carlton, Watson, COSO (resumen ejecutivo), Royal Society (resumen ejecutivo), Auditool, CILIP (caps. 4–5), Lluís (rango asignado).
- Umbrales MAD de Benford (Nigrini, 2012): las fuentes secundarias difieren entre 0.004 y 0.006 para "conformidad cercana".
- Algoritmo del dígito de verificación del NIT: se usa la versión de uso común; contrastar con una fuente de la DIAN.
- Normativa: enlace y numeración vigente del anexo de normas de aseguramiento (Decreto 2420 de 2015), Decreto 1499 de 2017 (MIPG), circular SARLAFT aplicable (Supersolidaria o SFC), Acto Legislativo 04 de 2019, Decreto Ley 403 de 2020, Decreto 2037 de 2019 y alcance del art. 34-7 de la Ley 1474 de 2011 (adicionado por la Ley 2195 de 2022).
- Power BI en Mac: soporte oficial en Windows para ARM y en máquinas virtuales; capacidades de Power BI Service según la licencia institucional; *gateway* para scripts de Python y R.
- Estructura y denominación vigentes de la DIARI en el sitio de la Contraloría.

### Control de calidad
`python scripts/control_calidad.py --estudiantes` verifica:
- horas: 24 + 72 = 96, por tramo y por unidad frente a la ruta semanal;
- tope de lectura del 30% por tramo;
- producto y criterio en cada actividad;
- matriz de alineación (evidencia presencial e independiente por RA);
- pesos = 100%;
- cero menciones de la herramienta excluida;
- enlaces relativos;
- ejecución y reproducibilidad de los scripts;
- ausencia de material docente en el repositorio de estudiantes.
