# Avance 2 · Dashboard de control con KPIs y storytelling

**Peso:** 7.5% · **RA:** RA2, RA3 · **Horas estimadas:** 6 h de equipo (semana 4) · **Fecha límite:** sábado de la semana 4, 23:59

## Enunciado
A partir del modelo del Avance 1 y de la matriz de indicadores trabajada en el S2, construya un tablero de control para el comité de auditoría de COAGUA que muestre si los procesos de pagos y de cartera están dentro del apetito de riesgo y dónde enfocar la atención.

## Entregables
1. **Archivo `.pbix`** con al menos 3 páginas:
   - **Resumen ejecutivo:** de 4 a 6 KPI/KRI con semáforo, tendencia y un titular dinámico;
   - **Pagos y controles:** indicadores de segregación, día no hábil, límites de aprobación, duplicados y ejecución presupuestal;
   - **Cartera:** cartera vencida, créditos fuera de política, calificación inconsistente y concentración.
   - Debe incluir al menos: 8 medidas DAX documentadas, una relación inactiva usada con `USERELATIONSHIP` y una información sobre herramientas (*tooltip*) o una obtención de detalles (*drillthrough*).
2. **Nota ejecutiva** (PDF, máximo 2 páginas) con la estructura contexto → hallazgos (máximo 3, cuantificados) → implicación → recomendación preliminar.
3. **Anexo:** matriz de indicadores (indicador, fórmula, umbral, responsable, frecuencia).

## Distribución sugerida del tiempo (6 h)
| Tarea | Horas |
|---|---:|
| Medidas DAX y umbrales | 1.5 |
| Diseño de las 3 páginas | 2.5 |
| Revisión con la lista de verificación de la práctica 04 | 0.5 |
| Nota ejecutiva | 1.5 |

## Rúbrica

| Criterio | Peso | Excelente (4.6–5.0) | Bueno (4.0–4.5) | Básico (3.0–3.9) | Insuficiente (< 3.0) |
|---|---:|---|---|---|---|
| Pertinencia de los indicadores | 25% | KPIs y KRIs vinculados a riesgos del caso, con umbral justificado y responsable | Indicadores pertinentes con umbrales poco justificados | Métricas sin umbral ni dueño | Indicadores irrelevantes o erróneos |
| Corrección técnica (DAX) | 20% | Medidas correctas, responden a los filtros y están documentadas; uso adecuado de `CALCULATE` y `USERELATIONSHIP` | Correctas con fallas menores | Algunas medidas incorrectas | Medidas erróneas que llevan a conclusiones falsas |
| Diseño visual | 20% | Cumple la lista de verificación: gráficos adecuados, color con significado, jerarquía clara y accesible | 1 o 2 incumplimientos menores | Varios incumplimientos | Tablero confuso |
| Storytelling | 20% | Titulares conclusivos y hallazgos cuantificados que llevan a una recomendación | Hallazgos claros con titulares descriptivos | Descripción sin conclusión | Ausente |
| Nota ejecutiva | 15% | Se lee en 3 minutos; pensada para el comité; sin jerga técnica | Clara con exceso de detalle técnico | Desordenada | Ausente |
