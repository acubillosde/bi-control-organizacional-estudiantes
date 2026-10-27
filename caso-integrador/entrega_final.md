# Entrega final · Detección de anomalías, informe ejecutivo y sustentación

**RA:** RA1, RA2, RA3
**Pesos:** sustentación 15% (componente Exposiciones) · entrega final 15% (componente Caso de estudio)
**Horas:** 2 h de preparación de la sustentación (semana 5) + 8 h de entrega final (semanas 6–7) + 2 h de lectura de cierre

---

## Sustentación

**Cuándo:** Sábado 3, de 14:00 a 16:40 · **Duración:** 12' de presentación + 10' de preguntas del comité
**Formato:** máximo 8 diapositivas o páginas del tablero en modo presentación.

Estructura sugerida:
1. El mensaje en una frase, que es la conclusión principal (1 diapositiva).
2. Alcance: población, periodo y pruebas realizadas (1).
3. Hallazgos priorizados por riesgo, con cantidad y valor en pesos (3).
4. Causa probable y control que falló, según el componente de COSO (1).
5. Recomendaciones con responsable, plazo e indicador de seguimiento (1).
6. Decisión que se solicita al comité (1).

### Rúbrica de sustentación

| Criterio | Peso | Excelente (4.6–5.0) | Bueno (4.0–4.5) | Básico (3.0–3.9) | Insuficiente (< 3.0) |
|---|---:|---|---|---|---|
| Mensaje y estructura | 20% | Abre con la conclusión; la secuencia es lógica; cierra con una decisión solicitada | Estructura clara sin decisión explícita | Estructura de proceso ("primero hicimos…") | Desordenada |
| Hallazgos y evidencia | 25% | Hallazgos priorizados, cuantificados y respaldados en el tablero; distingue señal de conclusión | Cuantificados sin priorización | Hallazgos vagos | Afirma fraude sin evidencia o con errores |
| Recomendaciones | 20% | Accionables, con responsable, plazo e indicador; vinculadas a la causa | Accionables pero genéricas | Vagas | Ausentes |
| Respuesta a preguntas | 20% | Responde con precisión, reconoce límites y usa el tablero en vivo | Responde adecuadamente | Respuestas evasivas | No responde |
| Manejo del tiempo y comunicación | 15% | Dentro del tiempo; lenguaje ejecutivo; participación equilibrada | Desvío menor de tiempo | Se excede o lee las diapositivas | Muy por fuera del tiempo |

### Guía de preguntas del comité
Para el docente y los estudiantes evaluadores. Cada comité elige 3 o 4:
- "¿Cuánto dinero está en riesgo y con qué grado de certeza?"
- "¿Cuál de estos hallazgos llevaría a la próxima reunión del consejo? ¿Por qué?"
- "¿Esto es fraude o error? ¿Qué evidencia adicional necesitaría?"
- "¿Qué control falló: el diseño o la operación?"
- "Si implementamos su tablero, ¿quién lo revisa, cada cuánto y qué pasa cuando un indicador está en rojo?"
- "¿Qué falsos positivos espera y cuánto cuesta revisarlos?"
- "¿Qué datos personales usa el tablero y quién debería tener acceso?"
- "¿Cómo sabemos que su modelo no está sesgado contra alguna región o asesor?"

---

## Entrega final

**Fecha límite:** sábado de la semana 7, 23:59.

### Enunciado
Incorpore la retroalimentación del comité y entregue la versión final del tablero, con detección de anomalías y un informe ejecutivo para el comité de auditoría.

### Entregables
1. **Archivo `.pbix` final**, con:
   - las páginas del Avance 2, corregidas;
   - una página de **analítica forense**: Benford (global y segmentada), duplicados, reglas de control y alertas de `alertas_pagos.csv` o propias;
   - una página de **priorización**: cruce entre reglas e Isolation Forest y tabla de casos de prioridad alta;
   - *(si aplica)* integración del puntaje de riesgo de crédito (`creditos_puntaje.csv` o la profundización C).
2. **Informe ejecutivo** (PDF, máximo 6 páginas más anexos):
   1. Resumen ejecutivo (½ página).
   2. Alcance y metodología: población, pruebas y limitaciones.
   3. Hallazgos priorizados: para cada uno, condición, criterio, causa, efecto (cantidad y valor) y recomendación, con el esquema de hallazgo de auditoría.
   4. **Diseño del monitoreo continuo:** indicador, umbral, frecuencia de actualización, responsable (primera, segunda o tercera línea) y escalamiento.
   5. **Hoja de ruta de madurez analítica** de COAGUA: 3 pasos, citando la lectura de cierre (L10).
   6. Anexo: declaración de uso de IA generativa y diccionario de medidas.

### Distribución sugerida del tiempo (8 h)
| Tarea | Horas |
|---|---:|
| Ajustes por la retroalimentación del comité | 1.5 |
| Página de analítica forense y de priorización | 2.5 |
| Informe ejecutivo | 3.0 |
| Revisión final y verificación de cifras | 1.0 |

### Rúbrica de la entrega final

| Criterio | Peso | Excelente (4.6–5.0) | Bueno (4.0–4.5) | Básico (3.0–3.9) | Insuficiente (< 3.0) |
|---|---:|---|---|---|---|
| Detección de anomalías | 25% | Detecta la mayoría de los tipos de anomalía presentes, incluidas las que requieren segmentar (p. ej., Benford por usuario), y combina reglas con un modelo | Detecta la mayoría de las anomalías evidentes | Detecta pocas, solo con reglas simples | Detección mínima o errónea |
| Rigor analítico | 20% | Distingue señal de evidencia; reconoce falsos positivos y limitaciones; las cifras cuadran | Rigor adecuado con limitaciones no declaradas | Conclusiones que exceden la evidencia | Afirmaciones sin sustento |
| Tablero final | 20% | Integra las retroalimentaciones; navegable; priorización clara | Mejoras parciales | Sin cambios desde el Avance 2 | Incompleto |
| Informe ejecutivo | 20% | Hallazgos en estructura condición–criterio–causa–efecto; recomendaciones accionables; lenguaje para el comité | Completo con detalle técnico excesivo | Incompleto | Ausente |
| Monitoreo y hoja de ruta | 15% | Diseño operable (umbral, frecuencia, responsable, escalamiento); hoja de ruta sustentada en la lectura de cierre | Diseño general | Enunciados vagos | Ausente |
