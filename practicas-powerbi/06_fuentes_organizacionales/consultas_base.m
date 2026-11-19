// =====================================================================================
// Práctica 06 · Consultas base para las fuentes de los sistemas de COAGUA (entidad ficticia)
// Parámetros de texto: ServidorERP, BaseERP, RutaSistemas (carpeta datos\sistemas\ terminada en "\")
// Estas consultas son el punto de partida. Completar lo que falta es parte del Avance 1.
// =====================================================================================


// ---- Consulta: fPagosERP  (PostgreSQL con plegado de consultas) -----------------------
let
    Origen = PostgreSQL.Database(ServidorERP, BaseERP),
    Pagos = Origen{[Schema = "erp", Item = "pagos"]}[Data],
    // ¿Qué estados existen? Revíselo antes de filtrar y compárelo con el diccionario de datos.
    Filtro = Table.SelectRows(Pagos, each [fec_pago] >= #date(2025, 1, 1))
in
    Filtro


// ---- Consulta: dCentrosCostoERP  (PostgreSQL con SQL nativo) --------------------------
// Con SQL nativo, Power BI no puede plegar los pasos que agregue después. Úselo solo cuando aporte algo.
let
    Origen = PostgreSQL.Database(ServidorERP, BaseERP, [Query = "
        SELECT cod_ccosto, nombre AS centro_costo, regional
        FROM erp.centros_costo
        ORDER BY cod_ccosto"])
in
    Origen


// ---- Consulta: dTRM  (API pública de datos.gov.co) -----------------------------------
let
    Respuesta = Json.Document(Web.Contents("https://www.datos.gov.co/resource/32sa-8pi3.json", [
        Query = [
            #"$where" = "vigenciahasta >= '2024-12-01T00:00:00' and vigenciadesde <= '2026-02-28T00:00:00'",
            #"$limit" = "2000"
        ]])),
    Tabla = Table.FromRecords(Respuesta),
    Tipos = Table.TransformColumnTypes(Tabla, {{"valor", type number}, {"vigenciadesde", type datetime},
        {"vigenciahasta", type datetime}}, "en-US")
in
    Tipos


// ---- Consulta: fnHojaPresupuestoBase  (función: lee UNA hoja del Excel de Finanzas) ------
(hoja as table) as table =>
let
    // Filas 1 a 5: título, regional, unidad, vacía y encabezado combinado. La fila 6 trae los encabezados.
    Datos = Table.PromoteHeaders(Table.Skip(hoja, 5), [PromoteAllScalars = true]),
    Centros = Table.SelectRows(Datos, each Text.StartsWith(Text.From([#"Centro de costo"] ?? ""), "CC")),
    Largo = Table.UnpivotOtherColumns(Table.RemoveColumns(Centros, {"Total"}), {"Centro de costo"}, "mes", "valor")
in
    Largo
// Prueba: = fnHojaPresupuestoBase(Excel.Workbook(File.Contents(RutaSistemas & "finanzas\Presupuesto_2025_v3_FINAL.xlsx"), null, true){[Item = "Bogotá", Kind = "Sheet"]}[Data])


// ---- Consulta: fnExtractoA  (función: extractos de enero a junio) ---------------------
(contenido as binary) as table =>
let
    T = Table.PromoteHeaders(Csv.Document(contenido,
        [Delimiter = ",", Encoding = 65001, QuoteStyle = QuoteStyle.Csv]), [PromoteAllScalars = true]),
    Tipos = Table.TransformColumnTypes(T, {{"Fecha", type date}, {"Descripcion", type text}, {"Referencia", type text},
        {"Debito", type number}, {"Credito", type number}, {"Saldo", type number}}, "en-US")
in
    Tipos


// ---- Consulta: fnHijo  (función auxiliar para XML) -------------------------------------
// Devuelve el valor del primer nodo hijo con ese nombre (Xml.Document separa el prefijo cbc:/cac:).
(nodos as table, nombre as text) => Table.SelectRows(nodos, each [Name] = nombre){0}[Value]


// ---- Consulta: fFacturaUna  (lee UNA factura para explorar la estructura) ---------------
let
    Archivos = Folder.Files(RutaSistemas & "facturas_electronicas"),
    Primera = Archivos{0}[Content],
    Raiz = Xml.Document(Primera){0}[Value],
    Numero = fnHijo(Raiz, "ID"),
    Fecha = fnHijo(Raiz, "IssueDate")
in
    [archivo = Archivos{0}[Name], numero = Numero, fecha = Fecha]
