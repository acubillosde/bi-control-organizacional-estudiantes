// =====================================================================================
// Práctica 01 · Power Query (M) · COAGUA (entidad ficticia, datos sintéticos)
// Cómo usar: en Power BI Desktop > Transformar datos > Nueva consulta > Consulta en blanco >
//            Editor avanzado. Pegue CADA bloque en una consulta con el nombre indicado.
// Requisito: parámetro de texto RutaDatos = ruta de la carpeta datos\ terminada en "\"
//            Ej.: "C:\Cursos\bi-control-organizacional\datos\"
// =====================================================================================


// ---- Consulta: fnLeerCsv  (función auxiliar) ----------------------------------------
(rutaRelativa as text) as table =>
let
    Origen = Csv.Document(
        File.Contents(RutaDatos & rutaRelativa),
        [Delimiter = ",", Encoding = 65001, QuoteStyle = QuoteStyle.Csv]
    ),
    Encabezados = Table.PromoteHeaders(Origen, [PromoteAllScalars = true])
in
    Encabezados


// ---- Consulta: dFestivos ------------------------------------------------------------
let
    Origen = fnLeerCsv("integrador\festivos.csv"),
    Tipos = Table.TransformColumnTypes(Origen, {{"fecha", type date}, {"festivo", type text}})
in
    Tipos


// ---- Consulta: dCalendario ----------------------------------------------------------
// Cubre 2022-2026: la cartera tiene desembolsos desde 2022 y algunos pagos de diciembre se ejecutan en enero de 2026.
let
    Inicio = #date(2022, 1, 1),
    Fin = #date(2026, 12, 31),
    Fechas = List.Dates(Inicio, Duration.Days(Fin - Inicio) + 1, #duration(1, 0, 0, 0)),
    Tabla = Table.FromList(Fechas, Splitter.SplitByNothing(), {"fecha"}),
    Tipo = Table.TransformColumnTypes(Tabla, {{"fecha", type date}}),
    Anio = Table.AddColumn(Tipo, "anio", each Date.Year([fecha]), Int64.Type),
    Mes = Table.AddColumn(Anio, "mes", each Date.Month([fecha]), Int64.Type),
    NombreMes = Table.AddColumn(Mes, "nombre_mes",
        each Date.ToText([fecha], [Format = "MMM", Culture = "es-CO"]), type text),
    AnioMes = Table.AddColumn(NombreMes, "anio_mes", each Date.ToText([fecha], [Format = "yyyy-MM"]), type text),
    DiaSemana = Table.AddColumn(AnioMes, "dia_semana", each Date.DayOfWeek([fecha], Day.Monday) + 1, Int64.Type),
    Festivo = Table.AddColumn(DiaSemana, "es_festivo", each List.Contains(dFestivos[fecha], [fecha]), type logical),
    Habil = Table.AddColumn(Festivo, "es_habil", each [dia_semana] <= 5 and not [es_festivo], type logical)
in
    Habil


// ---- Consulta: dEmpleados -----------------------------------------------------------
let
    Origen = fnLeerCsv("integrador\empleados.csv"),
    Tipos = Table.TransformColumnTypes(Origen, {
        {"id_empleado", type text}, {"nombre", type text}, {"cargo", type text}, {"area", type text},
        {"usuario_sistema", type text}, {"banco", type text}, {"cuenta_bancaria", type text},
        {"fecha_ingreso", type date}}),
    Limites = fnLeerCsv("integrador\limites_aprobacion.csv"),
    LimitesTipos = Table.TransformColumnTypes(Limites, {{"cargo", type text}, {"limite_aprobacion", Int64.Type}}),
    ConLimite = Table.NestedJoin(Tipos, {"cargo"}, LimitesTipos, {"cargo"}, "lim", JoinKind.LeftOuter),
    Expandida = Table.ExpandTableColumn(ConLimite, "lim", {"limite_aprobacion"})
in
    Expandida


// ---- Consulta: dProveedores ---------------------------------------------------------
let
    Origen = fnLeerCsv("integrador\proveedores.csv"),
    Tipos = Table.TransformColumnTypes(Origen, {
        {"id_proveedor", type text}, {"nit", type text}, {"dv", Int64.Type}, {"razon_social", type text},
        {"categoria", type text}, {"ciudad", type text}, {"departamento", type text}, {"banco", type text},
        {"cuenta_bancaria", type text}, {"fecha_creacion", type date}, {"creado_por", type text},
        {"estado", type text}}),
    // Control: ¿la cuenta bancaria del proveedor pertenece a un empleado?
    CuentasEmpleados = List.Buffer(dEmpleados[cuenta_bancaria]),
    CuentaEmpleado = Table.AddColumn(Tipos, "cuenta_de_empleado",
        each List.Contains(CuentasEmpleados, [cuenta_bancaria]), type logical)
in
    CuentaEmpleado


// ---- Consulta: dCentrosCosto --------------------------------------------------------
let
    Origen = fnLeerCsv("integrador\centros_costo.csv"),
    Tipos = Table.TransformColumnTypes(Origen, {
        {"id_centro_costo", type text}, {"centro_costo", type text}, {"regional", type text}})
in
    Tipos


// ---- Consulta: fPagos ---------------------------------------------------------------
let
    Origen = fnLeerCsv("integrador\pagos.csv"),
    Tipos = Table.TransformColumnTypes(Origen, {
        {"id_pago", type text}, {"id_proveedor", type text}, {"numero_factura", type text},
        {"fecha_factura", type date}, {"fecha_registro", type date}, {"fecha_aprobacion", type date},
        {"fecha_pago", type date}, {"id_centro_costo", type text}, {"valor", Int64.Type},
        {"medio_pago", type text}, {"usuario_registra", type text}, {"usuario_aprueba", type text}}),
    // Normaliza el número de factura para detectar duplicados aproximados (FV-0123 = FV123 = fv 123)
    FacturaNorm = Table.AddColumn(Tipos, "factura_normalizada",
        each Text.TrimStart(Text.Select([numero_factura], {"0".."9"}), "0"), type text),
    PrimerDigito = Table.AddColumn(FacturaNorm, "primer_digito",
        each Number.FromText(Text.Start(Text.From([valor]), 1)), Int64.Type),
    MismoUsuario = Table.AddColumn(PrimerDigito, "mismo_usuario",
        each [usuario_registra] = [usuario_aprueba], type logical),
    DiasAprobPago = Table.AddColumn(MismoUsuario, "dias_aprobacion_a_pago",
        each Duration.Days([fecha_pago] - [fecha_aprobacion]), Int64.Type),
    // Límite de aprobación del aprobador (para la regla "aprobación sobre el límite")
    ConLimite = Table.NestedJoin(DiasAprobPago, {"usuario_aprueba"},
        Table.SelectColumns(dEmpleados, {"usuario_sistema", "limite_aprobacion"}), {"usuario_sistema"},
        "apr", JoinKind.LeftOuter),
    Expandida = Table.ExpandTableColumn(ConLimite, "apr", {"limite_aprobacion"}, {"limite_aprobador"}),
    SobreLimite = Table.AddColumn(Expandida, "sobre_limite",
        each [valor] > [limite_aprobador], type logical),
    MontoRedondo = Table.AddColumn(SobreLimite, "monto_redondo",
        each Number.Mod([valor], 1000000) = 0, type logical)
in
    MontoRedondo


// ---- Consulta: fPresupuesto ---------------------------------------------------------
let
    Origen = fnLeerCsv("integrador\presupuesto.csv"),
    Tipos = Table.TransformColumnTypes(Origen, {
        {"id_centro_costo", type text}, {"fecha", type date}, {"presupuesto", type number}}, "en-US")
in
    Tipos


// ---- Consulta: fCreditos ------------------------------------------------------------
let
    Origen = fnLeerCsv("integrador\creditos.csv"),
    Tipos = Table.TransformColumnTypes(Origen, {
        {"id_credito", type text}, {"id_cliente", type text}, {"municipio", type text},
        {"departamento", type text}, {"linea", type text}, {"fecha_desembolso", type date},
        {"monto_desembolsado", Int64.Type}, {"saldo_capital", Int64.Type},
        {"tasa_ea", type number}, {"plazo_meses", Int64.Type}, {"garantia", type text},
        {"score_buro", Int64.Type}, {"antiguedad_cliente_anios", Int64.Type}, {"id_asesor", type text},
        {"dias_mora", Int64.Type}, {"calificacion", type text}, {"incumplimiento_12m", Int64.Type}},
        "en-US"),  // "en-US" para leer el punto decimal de tasa_ea
    // Política interna FICTICIA: A 0-30, B 31-60, C 61-90, D 91-180, E > 180 días
    CalifEsperada = Table.AddColumn(Tipos, "calificacion_esperada", each
        if [dias_mora] <= 30 then "A" else if [dias_mora] <= 60 then "B"
        else if [dias_mora] <= 90 then "C" else if [dias_mora] <= 180 then "D" else "E", type text),
    Politica = Table.TransformColumnTypes(fnLeerCsv("integrador\politica_lineas_credito.csv"),
        {{"linea", type text}, {"monto_maximo", type number}, {"tasa_min_ea", type number},
         {"tasa_max_ea", type number}}, "en-US"),
    ConPolitica = Table.NestedJoin(CalifEsperada, {"linea"}, Politica, {"linea"}, "pol", JoinKind.LeftOuter),
    Expandida = Table.ExpandTableColumn(ConPolitica, "pol", {"monto_maximo", "tasa_min_ea", "tasa_max_ea"}),
    FueraPolitica = Table.AddColumn(Expandida, "fuera_de_politica", each
        [monto_desembolsado] > [monto_maximo] or [tasa_ea] < [tasa_min_ea] or [tasa_ea] > [tasa_max_ea],
        type logical)
in
    FueraPolitica


// ---- Consulta: fAlertas  (salida de scripts/deteccion_anomalias.py) -------------------
let
    Origen = fnLeerCsv("resultados\alertas_pagos.csv"),
    Tipos = Table.TransformColumnTypes(Origen, {
        {"id_pago", type text}, {"prueba", type text}, {"detalle", type text}})
in
    Tipos


// ---- Consulta: fPuntajePagos  (salida de scripts/deteccion_anomalias.py) --------------
let
    Origen = fnLeerCsv("resultados\puntaje_pagos.csv"),
    Tipos = Table.TransformColumnTypes(Origen, {
        {"id_pago", type text}, {"if_puntaje", type number}, {"if_anomalo", Int64.Type},
        {"n_alertas_reglas", Int64.Type}}, "en-US")
in
    Tipos


// ---- Consulta: fCreditosPuntaje  (salida de scripts/modelo_credito.py) ----------------
// Relación 1:1 con fCreditos por id_credito.
let
    Origen = fnLeerCsv("resultados\creditos_puntaje.csv"),
    Tipos = Table.TransformColumnTypes(Origen, {
        {"id_credito", type text}, {"prob_incumplimiento", type number},
        {"perdida_esperada_simple", type number}, {"accion_recomendada", type text}}, "en-US")
in
    Tipos


// ---- Consulta: tExcepcionesCalidad  (Laboratorio L1, parte 2) ------------------------
// Tabla de excepciones: una fila por registro que incumple una regla de calidad.
let
    P = fPagos,
    R1 = Table.AddColumn(Table.SelectRows(P, each [fecha_pago] < [fecha_aprobacion]),
        "regla", each "Pago anterior a la aprobación", type text),
    R2 = Table.AddColumn(Table.SelectRows(P, each [fecha_factura] > [fecha_registro]),
        "regla", each "Factura posterior al registro", type text),
    R3 = Table.AddColumn(Table.SelectRows(P, each [valor] <= 0 or [valor] = null),
        "regla", each "Valor no positivo o vacío", type text),
    R4 = Table.AddColumn(Table.SelectRows(P, each [limite_aprobador] = null),
        "regla", each "Aprobador sin cargo/límite registrado", type text),
    Union = Table.Combine({R1, R2, R3, R4}),
    Columnas = Table.SelectColumns(Union, {"id_pago", "regla", "valor", "fecha_aprobacion", "fecha_pago"})
in
    Columnas
