# Práctica 04 · Dashboard de control interno y storytelling

**Unidad:** U3 (y U2) · **RA:** RA2, RA3 · **Se usa en:** L2 parte 2, T3, Avance 2, entrega final

## Estructura recomendada del informe (4 páginas)

| Página | Pregunta que responde | Audiencia | Visuales sugeridos |
|---|---|---|---|
| 1. Resumen ejecutivo | ¿Estamos dentro del apetito de riesgo este mes? | Comité de auditoría / junta | Tarjetas KPI con semáforo (`% pagos con alerta`, `Ejecución presupuestal %`, `Indicador de cartera vencida`), titular dinámico, tendencia mensual |
| 2. Pagos y controles | ¿Dónde fallan los controles de pago? | Auditoría interna, Tesorería | Matriz prueba × centro de costo, barras por aprobador, línea de pagos por día con días no hábiles resaltados |
| 3. Analítica forense | ¿Qué patrones sugieren fraude o error? | Auditoría interna | Columnas Benford (observado vs. esperado), dispersión valor vs. puntaje de Isolation Forest, tabla de los 20 pagos de prioridad alta |
| 4. Cartera y riesgo de crédito | ¿Cumple la cartera la política? | Gerencia de riesgos | Cartera vencida por línea y municipio, créditos fuera de política, concentración, tasa de incumplimiento por asesor |

Cada página tiene: **un titular que afirma una conclusión** (no "Gráfico de pagos" sino "El 62% de los pagos alertados se concentra en dos centros de costo"), un segmentador de fecha y una nota de fuente.

## Principios que se evalúan (lista de verificación)

- [ ] **Un mensaje por visual.** Si un visual necesita leyenda para entenderse, probablemente sobra información.
- [ ] **Elección del gráfico según la tarea:** comparar → barras; tendencia → líneas; composición → barras apiladas al 100% (evitar los anillos de más de 3 categorías); relación → dispersión; detalle → tabla con formato condicional.
- [ ] **Color con significado.** Gris para el contexto y un color de acento para lo que requiere atención. Rojo y verde solo para semáforos y siempre acompañados de texto o ícono, para personas con daltonismo.
- [ ] **Ejes que empiezan en cero** en las barras. Escalas consistentes entre visuales comparables.
- [ ] **Sin efectos 3D, sombras ni decoración.** Alta proporción de dato frente a tinta.
- [ ] **Orden de lectura en Z:** lo más importante arriba a la izquierda.
- [ ] **Formato de números:** millones con separador ("$ 1.234 M"), porcentajes con un decimal.
- [ ] **Interacción útil:** información sobre herramientas (*tooltips*) con el detalle del pago, obtención de detalles (*drillthrough*) del proveedor a sus pagos.
- [ ] **Accesibilidad:** texto alternativo en los visuales clave y contraste suficiente.

## Clínica del mal tablero (L2, parte 2)

El docente proyecta una página con estos 6 defectos. Los equipos deben identificarlos y corregirlos en 30 minutos:
1. Gráfico circular con 12 proveedores.
2. Barras con el eje truncado en 80 millones.
3. Arcoíris de colores sin significado.
4. Título "Visual 3".
5. Tarjeta de "Total pagado" sin contexto (sin meta ni periodo anterior).
6. Tabla de 6.000 filas sin filtro ni formato condicional.

## Guion de storytelling (T3 y Avance 2)

Plantilla de una página:

1. **Contexto:** qué se revisó, el periodo y la población (por ejemplo, "6.288 pagos de 2025 por $ X").
2. **Conflicto o hallazgo:** la evidencia principal, cuantificada.
3. **Implicación:** el riesgo, a quién afecta y cuánto cuesta.
4. **Resolución:** recomendación accionable con responsable y plazo.
5. **Siguiente paso:** qué se monitoreará, con qué frecuencia y qué umbral.

Use la medida `Titular alertas` como punto de partida y reescríbala con sus propias palabras.
