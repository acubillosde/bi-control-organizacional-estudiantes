# Expediente de COAGUA para el diagnóstico de madurez de BI (Ruta B)

**Se usa en:** [Actividad de diagnóstico de madurez de BI con evidencia](../../unidad-1/actividad_madurez_bi/README.md), Ruta B (semana 2). Lea primero el [catálogo de fuentes](coagua_fuentes.md), que dice a qué pregunta puede aportar cada documento.

> **Todo es ficticio.** COAGUA, las personas, las fechas y los documentos son inventados para el curso. Son los documentos que un consultor encontraría en su primera semana pidiendo información. **No contienen datos del caso integrador ni dicen nada sobre su contenido.**

> **Cómo leerlo.** Un documento prueba una capacidad solo si muestra lo que la pregunta del instrumento pide, y solo si está vigente. Fíjese en las fechas, en quién firma y en la diferencia entre lo que alguien **dice** y lo que un documento **muestra**. Si falta una pieza, anótela como NV y diga qué pediría.

Son ocho documentos, de media página cada uno (E1 a E8).

---

## E1 · Glosario de indicadores de Finanzas

*Hoja de cálculo de la Gerencia Financiera · Versión 3 · marzo de 2022*

| Indicador | Definición | Responsable |
|---|---|---|
| Ejecución presupuestal | Valor ejecutado sobre valor aprobado, por centro de costo, acumulado del año | Contador general (cargo vacante desde 2024) |
| Pagos a proveedores del mes | Suma de los pagos **por fecha de aprobación** | Contador general (cargo vacante desde 2024) |
| Cartera vencida | Saldo con más de 30 días de mora sobre cartera total | Contador general (cargo vacante desde 2024) |
| Costo de operación por oficina | Gastos directos de la oficina sobre colocación del periodo | Contador general (cargo vacante desde 2024) |

Se listan nueve indicadores en total; aquí se muestran cuatro. *Nota al pie:* «Este glosario lo elaboró Finanzas. Tesorería y Riesgos usan sus propias definiciones».

---

## E2 · Mapa de sistemas de COAGUA

*Dirección de Tecnología (Mauricio Rendón) · junio de 2024, última revisión*

| Sistema | Qué contiene | Quién lo mantiene | Cómo llega la información a los informes |
|---|---|---|---|
| ERP | Pagos, proveedores, comprobantes | Tecnología | Extracción mensual a archivo plano, hecha por una persona |
| Sistema de cartera | Créditos, saldos y mora | Tecnología y Riesgos | Extracción mensual a archivo plano |
| Hojas de cálculo de Finanzas | Consolidación mensual y reportes | Finanzas | Se alimentan a mano con las extracciones |
| Portal del banco | Extractos | Tesorería | Descarga manual |
| Correo | Reportes en PDF o Excel a gerentes y comité | Cada área | Envío manual |

*Nota:* «Los reportes de Tesorería y de Finanzas parten de un mismo archivo de consolidación». «El almacenamiento y las copias de seguridad están a cargo de Tecnología. No hay dueños de datos designados».

---

## E3 · Bitácora del cierre mensual de informes (últimos tres meses)

*Finanzas · Pablo Mejía, analista*

| Mes | Fecha de extracción | Quién | Pasos | Informe publicado |
|---|---|---|---|---|
| Septiembre | 3 de octubre | P. Mejía | Extraer del ERP y de cartera; pegar en el archivo de consolidación; actualizar tablas; revisar los totales a ojo; enviar por correo | 19 de octubre |
| Octubre | 4 de noviembre | P. Mejía | Igual | 24 de noviembre |
| Noviembre | 3 de diciembre | P. Mejía | Igual | 21 de diciembre |

*Notas del analista:* «Mi instructivo de una página (2023) está en mi carpeta personal. Si no estoy, el cierre se atrasa». «No hay un paso de validación escrito: reviso que los totales se vean razonables».

---

## E4 · Fichas de indicadores

*Tres fichas, Finanzas, Tesorería y Riesgos · 2023 a 2025*

| Indicador | Fórmula | Meta | Umbral | Responsable |
|---|---|---|---|---|
| Pagos a tiempo (Tesorería) | Pagos realizados en la fecha comprometida sobre pagos comprometidos | 98% | No definido | Tesorera (Nubia Cárdenas) |
| Ejecución presupuestal (Finanzas) | Ejecutado sobre aprobado | Entre 95% y 100% | No definido | Gerencia Financiera |
| Mora a 30 días (Riesgos) | Saldo con más de 30 días sobre cartera total | 5% | No definido | Gerente de Riesgos (Julián Barrera) |

No hay fichas para otros indicadores. *Nota:* «Los umbrales de alerta no están definidos; se discuten en el comité cuando el valor "se ve mal"».

---

## E5 · Extracto del acta del comité de auditoría

*Sesión de diciembre de 2026 · preside Elvira Montoya*

1. La revisoría fiscal y la gerencia de riesgos presentan sus informes. **El comité toma nota.**
2. «Se solicita a la Gerencia General un tablero de control interno que permita monitorear pagos y cartera».
3. «El proyecto se aprueba en principio. **El presupuesto se definirá cuando se conozca el alcance.**»
4. Responsable del seguimiento: Gerencia General. Fecha de la próxima revisión: no se fija.

---

## E6 · Registro de solicitudes de información (hoja compartida)

*Gerencia General · primer semestre de 2026*

| Fecha | Solicitante | Qué pidió | Canal | Entregado | Quién lo atendió |
|---|---|---|---|---|---|
| 12 de febrero | Gerente regional (Huila) | Mora de su regional | Correo | 26 de febrero | Finanzas |
| 3 de marzo | Control Interno | Pagos del trimestre | Correo | 20 de marzo | Finanzas |
| 18 de abril | Gerencia General | Ejecución por oficina | Correo | 2 de mayo | Finanzas |
| 6 de mayo | Comité | Mora por línea | Correo | 25 de mayo | Riesgos |

No hay prioridad, estado ni plazo comprometido. *Mensaje del gerente regional del Huila a Finanzas:* «¿Me explican de dónde sale este número? Mi equipo me pregunta y no sé qué contestarles».

---

## E7 · Política de tratamiento de datos personales (extracto)

*Gestión Humana · Yaneth Roa · 2021*

- «Los datos personales de asociados y empleados se almacenan en los sistemas de la cooperativa, bajo la custodia de Tecnología».
- «Se informará al titular la finalidad del tratamiento y se solicitará su autorización».
- La política **no designa dueños de los datos** y **no menciona el uso de los datos para análisis o informes.**

---

## E8 · Correo de la Gerencia General al comité

*Andrés Poveda · enero de 2027*

> «Estimados miembros: quiero tranquilizarlos. **Nuestros reportes están automatizados** y llegan puntuales cada mes. El tablero que piden será una extensión natural de lo que ya tenemos».
