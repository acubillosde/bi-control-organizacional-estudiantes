# Tiendas Aurora: el caso que el docente resuelve a la vista

*Caso de demostración del curso: las presentaciones lo usan para mostrar cada concepto aplicado, de la unidad 1 a la 4.*

**Tipo:** caso de enseñanza **ficticio**, escrito para este curso. **No es el caso integrador.** Su equipo trabaja con [COAGUA](../caso-integrador/caso_coagua.md); Aurora es el ejemplo resuelto que el docente muestra antes de que usted aplique lo mismo en COAGUA.
**Datos:** [`datos/demo_aurora/`](../datos/README.md) · **Lectura:** unos 8 minutos

> **Todo es inventado.** La empresa, las personas, las cifras y los datos no corresponden a ninguna organización ni persona real; cualquier parecido es coincidencia.

> **Cómo se usa.** En cada unidad pasan tres cosas, en este orden: **(1)** el docente muestra el concepto sobre Aurora, **(2)** el grupo lo hace junto en un ejercicio corto, y **(3)** su equipo lo aplica solo a COAGUA en el laboratorio o en el avance. Por eso aquí **sí se ve** lo que hay en los datos de Aurora; en COAGUA lo averigua su equipo.

---

## Acto I · La promesa

Tiendas Aurora es una cadena de **12 tiendas de barrio** (minimercados) en el Valle de Aburrá: Medellín, Envigado, Itagüí, Bello y Sabaneta. Tiene 160 empleados, unos 45 proveedores de lácteos, panadería, abarrotes, bebidas, frutas, carnes, aseo y servicios, y vendió cerca de **$37.600 millones** en 2025.

Hace dos años, Camila Ríos, la gerente general, le prometió a la junta: *«Cada tienda sabrá cada lunes cuánto vendió, cuánto devolvió y cuánto debe pagar, con la misma cifra que ve la gerencia»*. Hoy esa promesa vive en 12 archivos de Excel y un sistema de compras.

## Acto II · La escena que detona el año

Asunto: **«¿Cuánto pagamos a proveedores en marzo?»**
De: Andrés Mejía, jefe de compras. Para: Laura Zapata, contadora.

> *Laura: la junta pregunta cuánto se pagó en marzo a nuestros proveedores y yo tengo tres números: $958 millones, $957 millones y $910 millones. El sistema de compras dice una cifra; tu archivo de contabilidad, otra; y el gerente de la tienda de Envigado me mostró una tercera. Necesito saber cuál es la buena antes del jueves y cómo explicar la diferencia. Andrés.*

Los tres números eran ciertos para quien los calculó. Uno contaba por **fecha de aprobación** ($958 millones), otro por **fecha de pago** ($957 millones) y el tercero era el de aprobación **sin los cuatro pagos registrados dos veces** ($910 millones). Ninguno decía cuál era «el pago del mes».

## Acto III · Quién mira qué

| Actor | Qué mira | Qué teme |
|---|---|---|
| Camila Ríos, gerencia general | La cifra única | Que la junta pierda confianza |
| Laura Zapata, contabilidad | Que el cierre cuadre | Que le cambien las cifras después del cierre |
| Andrés Mejía, compras | Que los pedidos salgan a tiempo | Que cada control añada pasos |
| Gerentes de tienda | Sus ventas y su margen | Enterarse de sus indicadores por un tablero |
| Tesorería | Pagar a tiempo | Pagos rechazados por un proveedor |

Hay dos que chocan: **compras quiere velocidad y contabilidad quiere control**. Ninguno es el villano.

## Acto IV · Los datos de Aurora tienen memoria

- Cada área cuenta **«el pago»** en una fecha distinta.
- Los proveedores se registraron a lo largo de seis años por personas distintas: la **ciudad** de un mismo proveedor aparece escrita de varias maneras y hay un NIT repetido con otro formato.
- Las ventas de una tienda **no tienen registro durante nueve días de junio**.
- El sistema de compras **permite que quien registra un pago también lo apruebe**.

## Acto V · Qué se hace con Aurora en el curso

Aurora es un caso resuelto, con sus decisiones a la vista. Los datos reales de la cadena están en `datos/demo_aurora/`:

| Tabla | Contenido |
|---|---|
| `tiendas` | 12 tiendas con ciudad y tamaño |
| `empleados` | Usuarios del sistema con cargo |
| `limites_aprobacion` | Cuánto puede aprobar cada cargo |
| `proveedores` | Maestro de proveedores |
| `pagos` | Cerca de 1.800 pagos de 2025 |
| `ventas_diarias` | Ventas, tickets y devoluciones por tienda y día |

## El recorrido: dónde aparece Aurora en cada unidad

| Unidad | Concepto que se muestra sobre Aurora | Lo que su equipo hace luego en COAGUA |
|---|---|---|
| **U1** · BI y analítica | De los datos a la decisión: «tres números para un mismo pago»; arquitectura de fuentes; ETL; columna de control; hechos y dimensiones; KPI y KRI | Diagnóstico de madurez, plan de transformación y clínica de calidad |
| **U2** · BI en el control | Una definición única de «pago del mes»; calidad del maestro de proveedores; modelo estrella; matriz de indicadores | Matriz de indicadores y Avance 1 |
| **U3** · Visualización | Un tablero malo y su versión corregida; un titular con evidencia; el pitch de 3 minutos | Avance 2 y nota ejecutiva |
| **U4** · Analítica para el aseguramiento | Benford, duplicados, fraccionamiento, segregación y modelo, con sus falsos positivos | Entrega final y sustentación |

## Compruébelo usted
En cada unidad, los hechos de Aurora se verifican en Power BI y se contrastan en Python, con el ciclo prediga, construya, contraste, compare y concluya. La [guía de verificación](verificacion_aurora.md) trae los pasos, las medidas DAX, el código Python y, al final, los valores que debe dar. El script [`verificacion_aurora.py`](verificacion_aurora.py) corre las 17 verificaciones: `python casos/verificacion_aurora.py V07`.

