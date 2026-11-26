# Guía de verificación del caso Tiendas Aurora (Power BI)

En las clases de las unidades 1 a 4, el docente muestra los hechos de [Tiendas Aurora](caso_tiendas_aurora.md) y **usted los comprueba en su propio Power BI**. Esta guía trae, para cada verificación, la pregunta, los pasos y las medidas DAX. Al final está el **valor que debe dar**: no lo mire antes de intentarlo.

## Cómo se hace cada verificación (3 a 8 minutos)
1. **Prediga.** Anote en el papel de su equipo lo que cree que va a dar. Equivocarse al predecir enseña más que acertar.
2. **Construya.** Siga los pasos y escriba la medida; no la copie sin leerla.
3. **Contraste con Python.** Abra el cuaderno [`verificacion_aurora.ipynb`](verificacion_aurora.ipynb), ejecute la primera celda de código (prepara los datos) y después la celda de la verificación, por ejemplo la de V07, y compare con lo que dio Power BI. Son dos herramientas independientes: si coinciden, la cifra es confiable.
4. **Compare.** El docente muestra la cifra. Marque ✅ si Power BI, Python y la diapositiva coinciden, o ❌ si no.
5. **Busque el porqué.** Si no coinciden, revise el filtro, la relación, los duplicados, la fecha o el tipo de dato. Si Power BI y Python difieren entre sí, una de las dos tiene el error: no avance hasta saber cuál. Cada verificación trae una pista.
6. **Concluya.** Escriba una frase sobre qué cambia en el control.

**Para Python:** necesita `pandas` (`pip install pandas`) y ejecutar el comando desde la carpeta del repositorio. El script lee `datos/demo_aurora/` y no modifica nada. Sin argumentos, corre las 17 verificaciones.

> Los datos de Aurora son **sintéticos y fijos**: todos los equipos deben obtener el mismo valor. Los hallazgos de Aurora **no se trasladan** a COAGUA: sirven para aprender el método.

## Preparación (una sola vez)

1. Abra Power BI Desktop y use **Obtener datos → Texto o CSV** para cargar las seis tablas de `datos/demo_aurora/`.
2. Renombre las consultas: `pagos` → **fPagos**, `ventas_diarias` → **fVentas**, `proveedores` → **dProveedores**, `tiendas` → **dTiendas**, `empleados` → **dEmpleados**, `limites_aprobacion` → **dLimites**.
3. Verifique los tipos: las columnas `fecha_*` y `fecha` como **Fecha**; `valor`, `ventas`, `tickets` y `devoluciones` como número entero.
4. Las relaciones se crean en cada verificación que las necesita. Si su Power BI usa punto y coma (`;`) como separador de argumentos, cámbielo en las fórmulas de esta guía.

## Tabla de verificaciones

| # | Unidad | Qué se verifica | Tiempo | ✅/❌ |
|---|---|---|---|---|
| V01 | Caso | Cargue las seis tablas y cuente las filas | 4 min | |
| V02 | U1 | Limpie el maestro sin destruir el original | 6 min | |
| V03 | U1 | Construya tres columnas de control sobre pagos | 6 min | |
| V04 | U1 | Cree el calendario y encuentre los días sin ventas | 7 min | |
| V05 | U1 | Arme la estrella de ventas y pida «ventas por cliente» | 5 min | |
| V06 | U1 | Calcule un KPI, un KRI y un KCI | 6 min | |
| V07 | U2 | Reproduzca los tres números de marzo | 8 min | |
| V08 | U2 | Mida la calidad del maestro con reglas en DAX | 6 min | |
| V09 | U2 | Ponga los umbrales de la matriz en un semáforo | 7 min | |
| V10 | U3 | Haga la torta y compárela con barras | 5 min | |
| V11 | U3 | Resalte las devoluciones de T03 frente al resto | 8 min | |
| V12 | U3 | Haga un titular dinámico y póngalo a prueba | 6 min | |
| V13 | U4 | Pruebe Benford sobre el valor de los pagos | 8 min | |
| V14 | U4 | Cuente duplicados exactos y aproximados | 6 min | |
| V15 | U4 | Busque pagos pegados al límite de aprobación | 7 min | |
| V16 | U4 | Mida el valor y la concentración de las dos señales | 6 min | |
| V17 | U4 | Cruce cuentas bancarias de proveedores y de nómina | 7 min | |

## El caso

### V01 · Cargue las seis tablas y cuente las filas

**Prediga:** ¿Cuántas filas cree que tiene pagos? ¿Y ventas_diarias? Anótelo antes de cargar.

**Tablas:** las seis tablas. **Visual:** Transformar datos → Vista → «Perfil de columna basado en todo el conjunto de datos».

**Pasos**

1. Cargue los seis CSV con Obtener datos → Texto o CSV.
2. En el Editor de Power Query, active Vista → Estadísticas de columna y lea «Recuento».
3. Compare con la diapositiva siguiente.

**Python** (celda V01 del cuaderno `verificacion_aurora.ipynb`)

```python
for nombre, df in tablas.items():
    print(f"{nombre}: {len(df)} filas")
```

**Si no coincide:** Revise que el separador y la codificación del CSV sean los correctos (UTF-8, coma). Una fila de más suele ser el encabezado leído como dato.

**Concluya:** Lo primero que se verifica en un dato es el conteo: si no coincide con la fuente, nada de lo demás sirve.


## Unidad 1 · BI y analítica

### V02 · Limpie el maestro sin destruir el original

**Prediga:** ¿Cuántas ciudades distintas cree que hay en proveedores? ¿Y después de estandarizar? ¿Y cuántos NIT distintos?

**Tablas:** proveedores. **Visual:** Editor de Power Query y panel «Perfil de columna».

**Pasos**

1. Cargue `proveedores.csv` y llame a la consulta **proveedores_crudo**; en el menú de la consulta desactive «Habilitar carga».
2. Cree una consulta nueva con **Referencia** a `proveedores_crudo` y llámela **dProveedores**.
3. En `ciudad`: Transformar → Formato → minúsculas; Reemplazar valores «medellin» por «medellín» y «itagui» por «itagüí»; Formato → Poner en mayúscula cada palabra.
4. Agregue la columna `nit_digitos`: Agregar columna → Columna personalizada con la fórmula de abajo.
5. Active Vista → «Distribución de columna» y lea los valores distintos de `ciudad` y de `nit_digitos`.

**Power Query (lenguaje M)**

```
let
  Origen = proveedores_crudo,
  Minuscula = Table.TransformColumns(Origen, {{"ciudad", Text.Lower, type text}}),
  Tilde1 = Table.ReplaceValue(Minuscula, "medellin", "medellín", Replacer.ReplaceText, {"ciudad"}),
  Tilde2 = Table.ReplaceValue(Tilde1, "itagui", "itagüí", Replacer.ReplaceText, {"ciudad"}),
  Propio = Table.TransformColumns(Tilde2, {{"ciudad", Text.Proper, type text}}),
  Nit = Table.AddColumn(Propio, "nit_digitos", each Text.Select([nit], {"0".."9"}), type text)
in
  Nit
```

**Python** (celda V02 del cuaderno `verificacion_aurora.ipynb`)

```python
limpia = prov.ciudad.str.lower().str.replace("medellin", "medellín").str.replace("itagui", "itagüí").str.title()
nit_digitos = prov.nit.str.replace(r"\D", "", regex=True)
print("Filas de proveedores:", len(prov))
print("Ciudades distintas antes:", prov.ciudad.nunique())
print("Ciudades distintas después:", limpia.nunique())
print("NIT distintos (solo dígitos):", nit_digitos.nunique())
```

**Si no coincide:** Si le quedan 6 ciudades, falta uno de los dos reemplazos (con tilde). Si los NIT distintos son 47, no quitó puntos y guiones antes de contar.

**Concluya:** La limpieza queda escrita en pasos que se repiten, y el dato original no se toca. El NIT repetido no se borra: se confirma con compras.

### V03 · Construya tres columnas de control sobre pagos

**Prediga:** De 1.808 pagos, ¿cuántos cree que aprobó la misma persona que los registró? ¿Y cuántos se aprobaron en fin de semana?

**Tablas:** pagos. **Visual:** Columnas nuevas en Power Query y suma en el perfil de la columna.

**Pasos**

1. En Power Query, sobre `pagos`: Agregar columna → Columna personalizada, tres veces, con las fórmulas de abajo.
2. Asigne tipo de dato **Número entero** a `mismo_usuario` y `aprobacion_dia_no_habil`.
3. Use «Transformar → Estadísticas → Suma» sobre cada columna, o cárguelas y súmelas en una tarjeta.

**Power Query (lenguaje M)**

```
mismo_usuario              = each if [usuario_registra] = [usuario_aprueba] then 1 else 0
aprobacion_dia_no_habil    = each if Date.DayOfWeek([fecha_aprobacion], Day.Monday) >= 5 then 1 else 0
factura_normalizada        = each Text.TrimStart(Text.Select([numero_factura], {"0".."9"}), "0")
```

**Python** (celda V03 del cuaderno `verificacion_aurora.ipynb`)

```python
mismo_usuario = (pagos.usuario_registra == pagos.usuario_aprueba).astype(int)
dia_no_habil = (pagos.fecha_aprobacion.dt.dayofweek >= 5).astype(int)   # lunes = 0, sábado = 5
factura_norm = pagos.numero_factura.str.replace(r"\D", "", regex=True).str.lstrip("0")
print("Suma de mismo_usuario:", mismo_usuario.sum())
print("Suma de aprobacion_dia_no_habil:", dia_no_habil.sum())
print("factura_normalizada de FV-2269:", factura_norm[pagos.numero_factura == "FV-2269"].iloc[0])
```

**Si no coincide:** Si la suma de día no hábil da más de 14, revise que `fecha_aprobacion` sea tipo Fecha y que el primer día sea el lunes (`Day.Monday`).

**Concluya:** Sin la columna, la pregunta exige revisar fila por fila; con la columna, es un filtro. Es una señal, no un hallazgo.

### V04 · Cree el calendario y encuentre los días sin ventas

**Prediga:** La tienda T07 debería vender los 30 días de junio. ¿Cuántos días sin ventas cree que tiene?

**Tablas:** ventas_diarias y un calendario nuevo. **Visual:** Tarjeta con dos segmentadores: tienda y mes.

**Pasos**

1. Modelado → Nueva tabla: cree **dCalendario** con `CALENDAR` y renombre la columna `Date` como `fecha`.
2. Agregue la columna `mes = MONTH( dCalendario[fecha] )`.
3. Cree las relaciones: `dCalendario[fecha]` → `fVentas[fecha]` y `dTiendas[id_tienda]` → `fVentas[id_tienda]` (uno a varios).
4. Cree las dos medidas de abajo. Ponga una tarjeta con la medida y segmentadores de `dTiendas[id_tienda]` (T07) y `dCalendario[mes]` (6).

**DAX**

```dax
dCalendario = CALENDAR( DATE( 2025, 1, 1 ), DATE( 2025, 12, 31 ) )
mes = MONTH( dCalendario[fecha] )          -- columna calculada
Filas de ventas = COUNTROWS( fVentas )
Dias sin ventas = COUNTROWS( FILTER( dCalendario, ISBLANK( [Filas de ventas] ) ) )
```

**Python** (celda V04 del cuaderno `verificacion_aurora.ipynb`)

```python
junio = pd.date_range("2025-06-01", "2025-06-30")
vendio = set(ventas[(ventas.id_tienda == "T07") & (ventas.fecha.dt.month == 6)].fecha)
sin_ventas = [d for d in junio if d not in vendio]
print("Días sin ventas de T07 en junio:", len(sin_ventas))
print("Filas esperadas (12 tiendas x 365 días):", 12 * 365, "· filas reales:", len(ventas))
```

**Si no coincide:** Si la tarjeta da 30, el segmentador de tienda no filtra fVentas: revise la relación dTiendas → fVentas. Si da 0, no filtró la tienda T07.

**Concluya:** Los días que faltan no aparecen en la tabla de ventas: solo se ven contra un calendario completo. 4.380 − 4.371 = 9.

### V05 · Arme la estrella de ventas y pida «ventas por cliente»

**Prediga:** ¿Cuánto suman las ventas de 2025? ¿Qué tienda vende más? ¿Puede el modelo decir ventas por cliente?

**Tablas:** fVentas, dTiendas, dCalendario. **Visual:** Matriz con tiendas en las filas y tarjeta con el total.

**Pasos**

1. En la vista Modelo, verifique las relaciones: dTiendas y dCalendario hacia fVentas, uno a varios, filtro en un sentido.
2. Cree la medida `Ventas = SUM( fVentas[ventas] )` y cambie su formato a millones (Formato de medida → Unidades de presentación).
3. Ponga una tarjeta con `Ventas` y una matriz con `dTiendas[nombre_tienda]` y `Ventas`; ordene de mayor a menor.
4. Intente arrastrar una columna «cliente»: no existe en el modelo.

**DAX**

```dax
Ventas = SUM( fVentas[ventas] )
```

**Python** (celda V05 del cuaderno `verificacion_aurora.ipynb`)

```python
por_tienda = ventas.groupby("id_tienda").ventas.sum().sort_values(ascending=False)
nombre = tiendas.set_index("id_tienda").nombre_tienda[por_tienda.index[0]]
print("Ventas totales 2025: $" + n0(ventas.ventas.sum()), "=", n1(ventas.ventas.sum() / 1e6), "millones")
print("Tienda con más ventas:", por_tienda.index[0], nombre, n1(por_tienda.iloc[0] / 1e6), "millones")
print("Filas de ventas:", len(ventas))
```

**Si no coincide:** Si el total es mayor, hay una relación mal creada que duplica filas. Si falta una tienda, revise que id_tienda tenga el mismo tipo de dato en las dos tablas.

**Concluya:** El modelo responde lo que su granularidad permite: una fila por tienda y día. «Por cliente» no se puede, y eso se dice.

### V06 · Calcule un KPI, un KRI y un KCI

**Prediga:** Prediga: ¿cuántos días pasan en promedio entre la factura y el pago? ¿Qué porcentaje de las ventas se devuelve? ¿Qué porcentaje de pagos aprueba quien los registró?

**Tablas:** fPagos y fVentas. **Visual:** Tres tarjetas, una por indicador.

**Pasos**

1. Cree las tres medidas de abajo.
2. Ponga una tarjeta por medida y dé formato: 1 decimal, porcentaje con 2 decimales.
3. Anote cada valor junto a su predicción.

**DAX**

```dax
Dias factura a pago = AVERAGEX( fPagos, DATEDIFF( fPagos[fecha_factura], fPagos[fecha_pago], DAY ) )
Devolucion pct = DIVIDE( SUM( fVentas[devoluciones] ), SUM( fVentas[ventas] ) )
Pct mismo usuario = DIVIDE( SUM( fPagos[mismo_usuario] ), COUNTROWS( fPagos ) )
```

**Python** (celda V06 del cuaderno `verificacion_aurora.ipynb`)

```python
print("KPI · días de factura a pago:", n1((pagos.fecha_pago - pagos.fecha_factura).dt.days.mean()))
print("KRI · devoluciones sobre ventas:", n2(ventas.devoluciones.sum() / ventas.ventas.sum() * 100) + "%")
print("KCI · pagos con el mismo usuario:", n2((pagos.usuario_registra == pagos.usuario_aprueba).mean() * 100) + "%")
```

**Si no coincide:** Si el KCI no da 18 pagos, falta la columna `mismo_usuario` de la verificación V03. Si los días dan otro valor, revise que las dos fechas sean tipo Fecha.

**Concluya:** Un indicador es una medida con nombre, fórmula y dueño. Los tres se calculan igual: con una medida DAX que se pueda auditar.


## Unidad 2 · BI en el control

### V07 · Reproduzca los tres números de marzo

**Prediga:** Marzo de 2025: ¿cuánto sumó «el pago del mes» según la fecha de aprobación? ¿Según la fecha de pago? ¿Y sin duplicados? ¿Por qué no coinciden?

**Tablas:** fPagos y dCalendario. **Visual:** Tres tarjetas con segmentador de mes (3).

**Pasos**

1. Relaciones: `dCalendario[fecha]` → `fPagos[fecha_aprobacion]` (activa) y `dCalendario[fecha]` → `fPagos[fecha_pago]` (se crea inactiva).
2. En fPagos cree las columnas `clave` y `es_duplicado` (necesita `factura_normalizada` de V03).
3. Cree las tres medidas de abajo y póngalas en tarjetas, con segmentador de `dCalendario[mes]` en 3 (la columna `mes` es la de V04).
4. Divida cada resultado por un millón en el formato de la medida.

**DAX**

```dax
clave = fPagos[id_proveedor] & "|" & fPagos[factura_normalizada] & "|" & fPagos[valor]     -- columna calculada
es_duplicado =                                                                    -- columna calculada
  VAR k = fPagos[clave]
  VAR id = fPagos[id_pago]
  RETURN IF( COUNTROWS( FILTER( fPagos, fPagos[clave] = k && fPagos[id_pago] < id ) ) > 0, 1, 0 )
Pagos por aprobacion = SUM( fPagos[valor] )
Pagos por pago = CALCULATE( SUM( fPagos[valor] ), USERELATIONSHIP( fPagos[fecha_pago], dCalendario[fecha] ) )
Pagos sin duplicados = CALCULATE( [Pagos por aprobacion], fPagos[es_duplicado] = 0 )
```

**Python** (celda V07 del cuaderno `verificacion_aurora.ipynb`)

```python
marzo_aprobacion = pagos[pagos.fecha_aprobacion.dt.to_period("M") == "2025-03"]
marzo_pago = pagos[pagos.fecha_pago.dt.to_period("M") == "2025-03"]
sin_duplicados = marzo_aprobacion[marzo_aprobacion.es_duplicado == 0]
print("Por fecha de aprobación:", n1(marzo_aprobacion.valor.sum() / 1e6), "millones")
print("Por fecha de pago:", n1(marzo_pago.valor.sum() / 1e6), "millones")
print("Aprobación sin duplicados:", n1(sin_duplicados.valor.sum() / 1e6), "millones")
print("Duplicados en marzo:", len(marzo_aprobacion) - len(sin_duplicados))
```

**Si no coincide:** Si «por pago» da lo mismo que «por aprobación», la relación con fecha_pago sigue inactiva sin `USERELATIONSHIP`, o la usó en la medida equivocada. Si los duplicados son 0, falta `factura_normalizada`.

**Concluya:** Los tres números son correctos; lo que falta es una definición escrita. La relación inactiva explica una diferencia y los duplicados explican la otra.

### V08 · Mida la calidad del maestro con reglas en DAX

**Prediga:** Sobre el maestro SIN limpiar: ¿cuántos proveedores tienen la ciudad mal escrita? ¿Cuántos NIT están repetidos?

**Tablas:** proveedores_crudo y dProveedores. **Visual:** Dos tarjetas.

**Pasos**

1. Active «Habilitar carga» en `proveedores_crudo` (la consulta sin limpiar de la verificación V02).
2. Cree las dos medidas de abajo. `EXACT` distingue mayúsculas y tildes; el operador `=` de DAX no las distingue.
3. Ponga una tarjeta por medida.

**DAX**

```dax
Ciudades fuera de lista =
  COUNTROWS( FILTER( proveedores_crudo,
    NOT( EXACT( proveedores_crudo[ciudad], "Medellín" ) || EXACT( proveedores_crudo[ciudad], "Envigado" )
      || EXACT( proveedores_crudo[ciudad], "Itagüí" ) || EXACT( proveedores_crudo[ciudad], "Bello" )
      || EXACT( proveedores_crudo[ciudad], "Sabaneta" ) ) ) )
NIT repetidos = COUNTROWS( dProveedores ) - DISTINCTCOUNT( dProveedores[nit_digitos] )
```

**Python** (celda V08 del cuaderno `verificacion_aurora.ipynb`)

```python
lista = ["Medellín", "Envigado", "Itagüí", "Bello", "Sabaneta"]
nit_digitos = prov.nit.str.replace(r"\D", "", regex=True)
print("Ciudades fuera de lista:", (~prov.ciudad.isin(lista)).sum(), "de", len(prov))   # isin distingue mayúsculas y tildes
print("NIT repetidos:", len(prov) - nit_digitos.nunique())
print("Proveedores con el NIT repetido:", list(prov[nit_digitos.duplicated(keep=False)].id_proveedor))
```

**Si no coincide:** Si le da 6 en lugar de 8, usó `=`, que ignora las mayúsculas: «medellín» pasa como válida. Con `EXACT` sí la marca.

**Concluya:** Un error de calidad se corrige o se excluye; una señal de control se investiga. La regla queda como medida y se repite cada mes.

### V09 · Ponga los umbrales de la matriz en un semáforo

**Prediga:** Con los umbrales de la matriz, ¿qué color tendrá cada indicador de Aurora: verde, amarillo o rojo?

**Tablas:** fPagos y fVentas. **Visual:** Una matriz con indicador, valor y estado, con formato condicional.

**Pasos**

1. Reutilice las medidas de V06 y V07; cree `Pagos duplicados` y las cuatro medidas de estado de abajo.
2. Ponga una tarjeta por indicador, con la medida de estado como color de fondo (Formato condicional → Valor de campo).
3. Los umbrales son los de la matriz de la diapositiva anterior (inventados para la clase).

**DAX**

```dax
Pagos duplicados = SUM( fPagos[es_duplicado] )
Estado dias = SWITCH( TRUE(), [Dias factura a pago] > 20, "Rojo", [Dias factura a pago] > 15, "Amarillo", "Verde" )
Estado devoluciones = IF( [Devolucion pct] > 0.02, "Rojo", "Verde" )
Estado mismo usuario = IF( [Pct mismo usuario] > 0, "Rojo", "Verde" )
Estado duplicados = IF( [Pagos duplicados] > 0, "Rojo", "Verde" )
```

**Python** (celda V09 del cuaderno `verificacion_aurora.ipynb`)

```python
dias = (pagos.fecha_pago - pagos.fecha_factura).dt.days.mean()
dev = ventas.devoluciones.sum() / ventas.ventas.sum()
sep = ventas[(ventas.id_tienda == "T03") & (ventas.fecha.dt.month == 9)]
dev_t03 = sep.devoluciones.sum() / sep.ventas.sum()
mismo = (pagos.usuario_registra == pagos.usuario_aprueba).mean()
duplicados = pagos.es_duplicado.sum()
semaforo = lambda rojo: "Rojo" if rojo else "Verde"
print("Días de factura a pago:", n1(dias), "→", "Rojo" if dias > 20 else "Amarillo" if dias > 15 else "Verde")
print("Devoluciones (todas las tiendas):", n2(dev * 100) + "%", "→", semaforo(dev > 0.02))
print("Devoluciones de T03 en septiembre:", n2(dev_t03 * 100) + "%", "→", semaforo(dev_t03 > 0.02))
print("Pagos con el mismo usuario:", n2(mismo * 100) + "%", "→", semaforo(mismo > 0))
print("Pagos duplicados:", duplicados, "→", semaforo(duplicados > 0))
```

**Si no coincide:** Si todo le sale verde, mire el nivel de agregación: el promedio de las 12 tiendas esconde a T03. Pruebe la tarjeta con el filtro de tienda y mes.

**Concluya:** El mismo dato da un color distinto según el nivel y el umbral. Por eso el umbral se justifica y se acuerda con la junta.


## Unidad 3 · Visualización y storytelling

### V10 · Haga la torta y compárela con barras

**Prediga:** Con una torta de ventas por tienda, ¿puede decir cuál vende más y por cuánto? Pruébelo.

**Tablas:** fVentas y dTiendas. **Visual:** Gráfico circular y gráfico de barras, uno al lado del otro.

**Pasos**

1. Con la medida `Ventas`, cree un gráfico circular con `dTiendas[nombre_tienda]` como leyenda.
2. A su lado, un gráfico de barras horizontales con los mismos campos, ordenado de mayor a menor.
3. Active las etiquetas de porcentaje en la torta y el valor en las barras.
4. Compare: ¿cuál responde «cuál vende más y por cuánto»?

**Python** (celda V10 del cuaderno `verificacion_aurora.ipynb`)

```python
por_tienda = ventas.groupby("id_tienda").ventas.sum().sort_values(ascending=False)
parte = por_tienda / por_tienda.sum() * 100
print("Tienda con más ventas:", por_tienda.index[0])
print("Participación de las dos primeras:", n1(parte.iloc[0]) + "% y " + n1(parte.iloc[1]) + "%")
print("Diferencia entre las dos primeras:", n1((por_tienda.iloc[0] - por_tienda.iloc[1]) / 1e6), "millones")
```

**Si no coincide:** Si ve una diferencia clara en la torta, mire las etiquetas: dos porcentajes casi iguales no se distinguen por el área.

**Concluya:** Con doce porciones nadie compara áreas parecidas. Las barras ordenadas responden la pregunta; la torta solo decora.

### V11 · Resalte las devoluciones de T03 frente al resto

**Prediga:** ¿En qué mes devolvió T03 mucho más que el resto de tiendas? ¿Cuánto fue?

**Tablas:** fVentas, dTiendas y dCalendario. **Visual:** Gráfico de líneas por mes con tres líneas: T03, resto y umbral.

**Pasos**

1. Cree las cuatro medidas de abajo (reutilice `Devolucion pct`).
2. Gráfico de líneas: eje `dCalendario[mes]`; valores `T03`, `Resto` y `Umbral`.
3. Dé color coral solo a la línea de T03, gris al resto, y una línea punteada al umbral.
4. Ponga un título que diga el hallazgo, no el contenido.

**DAX**

```dax
Devolucion pct T03 = CALCULATE( [Devolucion pct], dTiendas[id_tienda] = "T03" )
Devolucion pct resto = CALCULATE( [Devolucion pct], dTiendas[id_tienda] <> "T03" )
Umbral = 0.02
```

**Python** (celda V11 del cuaderno `verificacion_aurora.ipynb`)

```python
ventas["mes"] = ventas.fecha.dt.month
def pct(df):
    return df.groupby("mes")[["devoluciones", "ventas"]].sum().pipe(lambda g: g.devoluciones / g.ventas * 100)
t03, resto = pct(ventas[ventas.id_tienda == "T03"]), pct(ventas[ventas.id_tienda != "T03"])
print(pd.DataFrame({"T03 %": t03.round(2), "Resto %": resto.round(2)}))
print("Mes del pico de T03:", t03.idxmax(), "·", n2(t03.max()) + "%", "· resto ese mes:", n2(resto[t03.idxmax()]) + "%")
```

**Si no coincide:** Si la línea de T03 sale plana, el filtro de tienda no aplica: revise la relación dTiendas → fVentas y que `Devolucion pct` esté bien definida (V06).

**Concluya:** Una línea resaltada, el resto en gris y un umbral: el gráfico dice qué mirar. Muestra una señal; la causa se investiga.

### V12 · Haga un titular dinámico y póngalo a prueba

**Prediga:** Si el titular dice «T03 devolvió X% de sus ventas», ¿qué dirá en enero? ¿Sigue siendo un buen titular?

**Tablas:** fVentas, dTiendas y dCalendario. **Visual:** Tarjeta de texto con segmentador de mes.

**Pasos**

1. Cree la medida `Titular` de abajo; ponga una tarjeta y un segmentador de `dCalendario[mes]`.
2. Elija septiembre y luego enero. Lea el texto en cada caso.
3. Cree `Titular mejorado`, que cambia de mensaje cuando no hay alerta, y compare.

**DAX**

```dax
Titular = "T03 devolvió " & FORMAT( [Devolucion pct T03], "0.0%" ) & " de sus ventas; el resto de tiendas, " & FORMAT( [Devolucion pct resto], "0.0%" )
Titular mejorado = IF( [Devolucion pct T03] > [Umbral],
  "Alerta: T03 devolvió " & FORMAT( [Devolucion pct T03], "0.0%" ) & " de sus ventas, " & FORMAT( DIVIDE( [Devolucion pct T03], [Devolucion pct resto] ), "0" ) & " veces el resto",
  "Sin alertas de devoluciones en T03 este mes" )
```

**Python** (celda V12 del cuaderno `verificacion_aurora.ipynb`)

```python
ventas["mes"] = ventas.fecha.dt.month
def pct(df, mes):
    g = df[df.mes == mes]
    return g.devoluciones.sum() / g.ventas.sum() * 100
for mes, nombre in [(9, "septiembre"), (1, "enero")]:
    t03, resto = pct(ventas[ventas.id_tienda == "T03"], mes), pct(ventas[ventas.id_tienda != "T03"], mes)
    print(f"Titular en {nombre}: T03 devolvió {n1(t03)}% de sus ventas; el resto de tiendas, {n1(resto)}%")
    if t03 > 2:
        print(f"Titular mejorado en {nombre}: Alerta: T03 devolvió {n1(t03)}% de sus ventas, {round(t03 / resto)} veces el resto")
```

**Si no coincide:** Si su Power BI muestra «4.2%» con punto, es la configuración regional: el texto es el mismo. Si el titular no cambia con el mes, falta la relación con dCalendario.

**Concluya:** Un titular dinámico no puede cambiar solo el número: tiene que cambiar el mensaje. Si no hay alerta, no debe gritar.


## Unidad 4 · Analítica para el aseguramiento

### V13 · Pruebe Benford sobre el valor de los pagos

**Prediga:** ¿Con qué frecuencia cree que el valor de un pago empieza por 1? Prediga el porcentaje para todos los pagos y para el usuario aur006.

**Tablas:** fPagos. **Visual:** Columnas por primer dígito, con el esperado como línea y un segmentador de usuario.

**Pasos**

1. Cree la columna `primer_digito` en fPagos.
2. Cree las medidas `% pagos` y `Esperado Benford`.
3. Gráfico de columnas con `primer_digito` en el eje, `% pagos` como columnas y `Esperado Benford` como línea.
4. Ponga un segmentador de `usuario_registra`: todos, `aur006` y luego los demás.

**DAX**

```dax
primer_digito = VALUE( LEFT( FORMAT( fPagos[valor], "0" ), 1 ) )          -- columna calculada
% pagos = DIVIDE( COUNTROWS( fPagos ), CALCULATE( COUNTROWS( fPagos ), ALLSELECTED( fPagos[primer_digito] ) ) )
Esperado Benford = LOG10( 1 + 1 / SELECTEDVALUE( fPagos[primer_digito] ) )
```

**Python** (celda V13 del cuaderno `verificacion_aurora.ipynb`)

```python
primer = pagos.valor.astype(str).str[0].astype(int)
uno = lambda mascara: (primer[mascara] == 1).mean() * 100   # % de pagos del grupo cuyo valor empieza por 1
print("Esperado para el dígito 1:", n1(math.log10(2) * 100) + "%")
print("Todos los pagos:", n1((primer == 1).mean() * 100) + "%")
print("Resto de usuarios:", n1(uno(pagos.usuario_registra != "aur006")) + "%")
print("aur006:", n1(uno(pagos.usuario_registra == "aur006")) + "%", "·", (pagos.usuario_registra == "aur006").sum(), "pagos")
```

**Si no coincide:** Si todos los porcentajes dan 11,1%, el denominador no quita el filtro del dígito: revise `ALLSELECTED`. Si el eje sale en orden raro, ordénelo por `primer_digito`.

**Concluya:** En conjunto parece normal; por usuario, uno se sale. Benford orienta dónde mirar y no prueba nada: se pide el soporte.

### V14 · Cuente duplicados exactos y aproximados

**Prediga:** ¿Cuántos pagos están repetidos con mismo proveedor, factura y valor? ¿Y cuántos más aparecen si se normaliza el número de factura?

**Tablas:** fPagos. **Visual:** Tres tarjetas.

**Pasos**

1. Cree la columna `clave_exacta` (con `numero_factura` sin normalizar).
2. Cree las tres medidas de abajo; `es_duplicado` y `clave` vienen de V07.
3. Una tarjeta por medida.

**DAX**

```dax
clave_exacta = fPagos[id_proveedor] & "|" & fPagos[numero_factura] & "|" & fPagos[valor]     -- columna calculada
Duplicados exactos = COUNTROWS( fPagos ) - DISTINCTCOUNT( fPagos[clave_exacta] )
Duplicados con normalizacion = SUM( fPagos[es_duplicado] )
Duplicados aproximados = [Duplicados con normalizacion] - [Duplicados exactos]
```

**Python** (celda V14 del cuaderno `verificacion_aurora.ipynb`)

```python
exactos = pagos.duplicated(["id_proveedor", "numero_factura", "valor"]).sum()
normalizados = pagos.es_duplicado.sum()
print("Duplicados exactos:", exactos)
print("Duplicados con la factura normalizada:", normalizados)
print("Duplicados aproximados:", normalizados - exactos)
```

**Si no coincide:** Si los aproximados dan 0, `clave` está usando `numero_factura` en lugar de `factura_normalizada`. Si los exactos dan 20, contó los dos pagos de cada par.

**Concluya:** Una regla sin normalizar deja pasar parte del problema. Y marca de más si hay entregas parciales legítimas: cada alerta pide su soporte.

### V15 · Busque pagos pegados al límite de aprobación

**Prediga:** El jefe de compras aprueba hasta $8 millones. ¿Cuántos pagos del año caen entre el 95% y el 100% del límite? ¿Y cuántos son del mismo proveedor en agosto?

**Tablas:** fPagos y dCalendario. **Visual:** Tarjeta y matriz por proveedor, con segmentador de mes.

**Pasos**

1. Cree la medida `Pagos cerca del limite`.
2. Matriz con `id_proveedor` en las filas y la medida; ordene de mayor a menor.
3. Ponga un segmentador de `dCalendario[mes]` y elija agosto (8).
4. Mire quién concentra los pagos y en qué días.

**DAX**

```dax
Pagos cerca del limite = CALCULATE( COUNTROWS( fPagos ), fPagos[valor] >= 0.95 * 8000000, fPagos[valor] < 8000000 )
```

**Python** (celda V15 del cuaderno `verificacion_aurora.ipynb`)

```python
cerca = pagos[(pagos.valor >= 0.95 * 8_000_000) & (pagos.valor < 8_000_000)]
print("Pagos entre 95% y 100% del límite (año):", len(cerca))
print(cerca.id_proveedor.value_counts().head(3))
ago = cerca[(cerca.id_proveedor == "P017") & (cerca.fecha_aprobacion.dt.month == 8)]
print("P017 en agosto:", len(ago), "pagos entre", n2(ago.valor.min() / 1e6), "y", n2(ago.valor.max() / 1e6), "millones")
```

**Si no coincide:** Si le da más de 34, usó un umbral menor al 95%. Si P017 no sale primero, la matriz no está ordenada por la medida.

**Concluya:** La regla sola da 34 alertas; el patrón está en un proveedor y en una ventana corta. Una alerta no es un hallazgo.

### V16 · Mida el valor y la concentración de las dos señales

**Prediga:** Los pagos aprobados por quien los registró: ¿de cuántos usuarios son y cuánto valen? Y los de fin de semana: ¿sábado o domingo?

**Tablas:** fPagos. **Visual:** Dos tarjetas y una matriz por día de la semana.

**Pasos**

1. Cree las medidas de abajo.
2. Una tarjeta para cada una de las dos primeras medidas.
3. Matriz con el día de la semana (columna `dia_semana` en `dCalendario`) y los pagos no hábiles.

**DAX**

```dax
Valor mismo usuario = CALCULATE( SUM( fPagos[valor] ), fPagos[mismo_usuario] = 1 )
Usuarios que registran y aprueban = CALCULATE( DISTINCTCOUNT( fPagos[usuario_registra] ), fPagos[mismo_usuario] = 1 )
Pagos en dia no habil = SUM( fPagos[aprobacion_dia_no_habil] )
dia_semana = WEEKDAY( dCalendario[fecha], 2 )          -- columna calculada: 6 = sábado, 7 = domingo
```

**Python** (celda V16 del cuaderno `verificacion_aurora.ipynb`)

```python
mismo = pagos[pagos.usuario_registra == pagos.usuario_aprueba]
finde = pagos[pagos.fecha_aprobacion.dt.dayofweek >= 5]
print("Pagos del mismo usuario:", len(mismo), "·", n1(mismo.valor.sum() / 1e6), "millones · usuarios:", list(mismo.usuario_registra.unique()))
print("Pagos en día no hábil:", len(finde), "· sábados:", (finde.fecha_aprobacion.dt.dayofweek == 5).sum(), "· domingos:", (finde.fecha_aprobacion.dt.dayofweek == 6).sum())
print("Valor de los pagos de fin de semana:", n1(finde.valor.sum() / 1e6), "millones")
```

**Si no coincide:** Si la matriz de día no hábil queda vacía, relacione `fecha_aprobacion` con `dCalendario[fecha]` como relación activa (V07).

**Concluya:** Son controles preventivos que el sistema debería impedir: el hallazgo también es del sistema, no solo de una persona. Se usan identificadores, no nombres.

### V17 · Cruce cuentas bancarias de proveedores y de nómina

**Prediga:** ¿Cuántos proveedores comparten cuenta bancaria con la nómina de un empleado? ¿Qué patrón tienen sus pagos?

**Tablas:** dProveedores, dEmpleados y fPagos. **Visual:** Tarjeta y tabla de pagos del proveedor señalado.

**Pasos**

1. Cree la medida `Proveedores con cuenta de empleado`.
2. Ponga la tarjeta. Si da más de 0, filtre `dProveedores` por esa condición (columna calculada `cuenta_de_empleado`) y mire sus pagos.
3. **Dato personal:** este resultado no se publica en un tablero general. Se entrega solo a quien lo investiga.

**DAX**

```dax
Proveedores con cuenta de empleado =
  CALCULATE( COUNTROWS( dProveedores ),
    FILTER( dProveedores, dProveedores[cuenta_bancaria] IN VALUES( dEmpleados[cuenta_nomina] ) ) )
cuenta_de_empleado = IF( dProveedores[cuenta_bancaria] IN VALUES( dEmpleados[cuenta_nomina] ), 1, 0 )          -- columna calculada
```

**Python** (celda V17 del cuaderno `verificacion_aurora.ipynb`)

```python
coinciden = prov[prov.cuenta_bancaria.isin(emp.cuenta_nomina)]
print("Proveedores con cuenta de nómina:", len(coinciden), list(coinciden.id_proveedor))
pr = pagos[pagos.id_proveedor.isin(coinciden.id_proveedor)]
print("Pagos a ese proveedor:", len(pr), "·", n1(pr.valor.sum() / 1e6), "millones")
print("Proveedor creado:", coinciden.fecha_creacion.iloc[0], "· primer pago aprobado:", pr.fecha_aprobacion.min().date(), "· último:", pr.fecha_aprobacion.max().date())
print("Quién registró los pagos:", list(pr.usuario_registra.unique()), "· valor máximo:", n1(pr.valor.max() / 1e6), "millones")
```

**Si no coincide:** Si le da 0, las dos columnas de cuenta tienen tipos distintos (una texto y otra número): conviértalas al mismo tipo. Si da más de 1, la columna no se está filtrando por el valor exacto.

**Concluya:** Una coincidencia de cuenta es una señal fuerte, y aun así se confirma antes de afirmar un conflicto de interés. Es un dato personal.

## Valores esperados

Compare solo después de intentarlo. Las cifras salen de `datos/demo_aurora/`.

**V01 · Cargue las seis tablas y cuente las filas**

| Qué | Valor |
|---|---|
| tiendas | 12 |
| empleados | 36 |
| limites_aprobacion | 4 |
| proveedores | 47 |
| pagos | 1.808 |
| ventas_diarias | 4.371 |

**V02 · Limpie el maestro sin destruir el original**

| Qué | Valor |
|---|---|
| Filas de dProveedores | 47 |
| Ciudades distintas antes | 8 |
| Ciudades distintas después | 5 |
| NIT distintos (solo dígitos) | 46 de 47 |

**V03 · Construya tres columnas de control sobre pagos**

| Qué | Valor |
|---|---|
| Suma de mismo_usuario | 18 |
| Suma de aprobacion_dia_no_habil | 14 |
| factura_normalizada de FV-2269 | 2269 |

**V04 · Cree el calendario y encuentre los días sin ventas**

| Qué | Valor |
|---|---|
| Días sin ventas de T07 en junio | 9 |
| Filas esperadas de fVentas (12 tiendas × 365 días) | 4.380 |
| Filas reales | 4.371 |
| Si quita el segmentador de tienda | 0 (otras tiendas sí vendieron esos días) |

**V05 · Arme la estrella de ventas y pida «ventas por cliente»**

| Qué | Valor |
|---|---|
| Ventas totales 2025 | $37.646.760.978 (≈ $37.646,8 millones) |
| Tienda con más ventas | T02 · Belén · $3.738,0 millones |
| Filas de fVentas | 4.371 |

**V06 · Calcule un KPI, un KRI y un KCI**

| Qué | Valor |
|---|---|
| KPI · días de factura a pago | 16,2 |
| KRI · devoluciones sobre ventas | 0,82% |
| KCI · pagos con el mismo usuario | 1,00% (18 de 1.808) |

**V07 · Reproduzca los tres números de marzo**

| Qué | Valor |
|---|---|
| Por fecha de aprobación | $958,0 millones |
| Por fecha de pago | $956,8 millones |
| Aprobación sin duplicados | $909,7 millones |
| Pagos duplicados en marzo | 4 pagos · $48,3 millones |

**V08 · Mida la calidad del maestro con reglas en DAX**

| Qué | Valor |
|---|---|
| Ciudades fuera de lista | 8 de 47 |
| NIT repetidos | 1 |
| Proveedor del NIT repetido | P047 repite el NIT de P009 |

**V09 · Ponga los umbrales de la matriz en un semáforo**

| Qué | Valor |
|---|---|
| Días de factura a pago | 16,2 → Amarillo (meta 15, alerta 20) |
| Devoluciones sobre ventas (todas las tiendas) | 0,82% → Verde |
| Devoluciones de T03 en septiembre | 4,17% → Rojo (póngalo con filtro de tienda y mes) |
| Pagos con el mismo usuario | 1,00% → Rojo (umbral 0%) |
| Pagos duplicados | 16 → Rojo (umbral 0 sin explicar) |

**V10 · Haga la torta y compárela con barras**

| Qué | Valor |
|---|---|
| Tienda con más ventas | T02 · Belén |
| Participación de las dos primeras en la torta | 9,9% y 9,9% |
| Diferencia entre las dos primeras | $20,4 millones |

**V11 · Resalte las devoluciones de T03 frente al resto**

| Qué | Valor |
|---|---|
| Mes del pico | Septiembre |
| T03 en septiembre | 4,17% |
| Resto de tiendas en septiembre | 0,80% |
| T03 en los demás meses | entre 0,7% y 0,9% |

**V12 · Haga un titular dinámico y póngalo a prueba**

| Qué | Valor |
|---|---|
| Titular en septiembre | T03 devolvió 4,2% de sus ventas; el resto de tiendas, 0,8% |
| Titular en enero | T03 devolvió 0,8% de sus ventas; el resto de tiendas, 0,8%  (dice lo mismo cuando no pasa nada) |
| Titular mejorado en septiembre | Alerta: T03 devolvió 4,2% de sus ventas, 5 veces el resto |

**V13 · Pruebe Benford sobre el valor de los pagos**

| Qué | Valor |
|---|---|
| Esperado para el dígito 1 | 30,1% |
| Todos los pagos, dígito 1 | 27,7% |
| Resto de usuarios, dígito 1 | 30,6% |
| aur006 (290 pagos), dígito 1 | 12,1% |

**V14 · Cuente duplicados exactos y aproximados**

| Qué | Valor |
|---|---|
| Duplicados exactos | 10 |
| Duplicados con la factura normalizada | 16 |
| Duplicados aproximados | 6 |

**V15 · Busque pagos pegados al límite de aprobación**

| Qué | Valor |
|---|---|
| Pagos entre 95% y 100% del límite (año) | 34  ← alertas de la regla sola |
| Proveedor que más concentra | P017 con 8 pagos |
| P017 en agosto | 7 pagos entre $7,66 y $7,99 millones |
| Aprobador de esos pagos | el jefe de compras |

**V16 · Mida el valor y la concentración de las dos señales**

| Qué | Valor |
|---|---|
| Pagos registrados y aprobados por la misma persona | 18 · $81,9 millones |
| Usuarios que lo hacen | 1 (aur004) |
| Pagos aprobados en día no hábil | 14: 10 sábados y 4 domingos |
| Valor de los pagos de fin de semana | $111,0 millones |

**V17 · Cruce cuentas bancarias de proveedores y de nómina**

| Qué | Valor |
|---|---|
| Proveedores que comparten cuenta con nómina | 1 (P046) |
| Pagos a ese proveedor | 5 · $34,4 millones |
| Proveedor creado | 2025-05-05 |
| Primer pago aprobado | 2025-05-09 |
| Último pago aprobado | 2025-06-16 |
| Quién registró los pagos | un solo usuario (aur003), todos por debajo de $8 millones |
