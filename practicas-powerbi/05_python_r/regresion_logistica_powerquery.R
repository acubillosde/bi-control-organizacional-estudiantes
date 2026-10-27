# Script para el paso "Ejecutar script de R" de Power Query (alternativa en R de la profundización C).
# Power BI entrega la tabla actual en `dataset` (data.frame). Partir de la consulta fCreditos.
# Solo usa R base (glm), sin paquetes adicionales.

df <- dataset
df$linea    <- factor(df$linea)
df$garantia <- factor(df$garantia)
df$municipio <- factor(df$municipio)
df$id_asesor <- factor(df$id_asesor)

# Variables disponibles al momento del desembolso (sin dias_mora: evitaría fuga de información)
modelo <- glm(
  incumplimiento_12m ~ monto_desembolsado + tasa_ea + plazo_meses + score_buro +
    antiguedad_cliente_anios + linea + garantia + municipio + id_asesor,
  data = df, family = binomial()
)

df$prob_incumplimiento <- round(predict(modelo, newdata = df, type = "response"), 4)
df$accion_recomendada <- ifelse(df$prob_incumplimiento >= 0.5 & df$saldo_capital >= 50e6,
                                "Visita de campo y revisión de garantía",
                         ifelse(df$prob_incumplimiento >= 0.5, "Gestión de cobro preventiva",
                         ifelse(df$prob_incumplimiento >= 0.25, "Seguimiento mensual", "Monitoreo estándar")))

resultado <- df[, c("id_credito", "prob_incumplimiento", "accion_recomendada")]
