# Práctica 07 · Seguridad por filas: cada quien ve lo que le corresponde

**Unidad:** U3 · **RA:** RA2 · **Se usa en:** Avance 2 y entrega final del caso integrador (rama `fuentes-organizacionales`)

En COAGUA el comité de auditoría y control interno ven todo, y cada gerente regional ve solo su regional. Esta separación es un **control de acceso**, igual a los que el curso analiza con COSO. Si un tablero de control muestra datos a quien no debe verlos, se convierte él mismo en un riesgo.

## Requisitos
- Modelo del Avance 1 con `dCentrosCosto` (o `dCentrosCostoERP`) relacionada con los pagos.
- Tabla `dUsuariosTablero` importada de `gobierno.usuarios_tablero` (PostgreSQL). **No la relacione** con ninguna otra tabla.

## Parte A · Roles estáticos (20 min)
1. *Modelado > Administrar roles > Nuevo*. Cree el rol `Gerencia Huila`.
2. Seleccione la tabla `dCentrosCosto` y escriba el filtro DAX `[regional] = "Huila"`.
3. *Modelado > Ver como > Gerencia Huila*. Revise el total pagado y las tarjetas del resumen ejecutivo.

**Pregunta:** con 8 regionales, ¿cuántos roles estáticos necesita? ¿Qué pasa cuando cambia un gerente o se abre una oficina?

## Parte B · Rol dinámico (40 min)
Un solo rol que lee del sistema quién es el usuario:

1. Cree el rol `Usuarios COAGUA`.
2. En `dCentrosCosto`, escriba este filtro:
   ```DAX
   VAR correo = USERPRINCIPALNAME ()
   VAR alcance = LOOKUPVALUE ( dUsuariosTablero[regional], dUsuariosTablero[correo], correo )
   RETURN alcance = "Todas" || dCentrosCosto[regional] = alcance
   ```
3. Pruebe con *Ver como > Otro usuario*: `gerente.huila@coagua.example` y el rol `Usuarios COAGUA`. Repita con `comite.auditoria@coagua.example` y con un correo que no esté en la tabla.

**Preguntas de control:**
1. ¿Qué ve un usuario que **no** está en `dUsuariosTablero`? ¿Es el comportamiento seguro?
2. El filtro sobre `dCentrosCosto` se propaga a los pagos, pero **no** a las tablas que no se relacionan con ella. ¿Qué ve un gerente regional en la conciliación bancaria (`fBanco`) o en la cartera (`fCreditos`)? Escriba los filtros que faltan. Pista: la cartera tiene `departamento` y el banco no tiene regional; decida si un gerente regional debe verlo.
3. Los créditos de Quindío no pertenecen a ninguna regional de COAGUA. ¿Quién debería verlos?
4. ¿Quién mantiene `gobierno.usuarios_tablero`? ¿Qué control asegura que, cuando un gerente se retira, pierde el acceso? Relaciónelo con el componente *actividades de control* de COSO.

## Parte C · Publicación (opcional, según licencias)
⚠ **Pendiente de verificar:** para publicar en el servicio de Power BI, asignar usuarios a los roles y programar la actualización se necesita una licencia Pro o Premium por usuario, o una capacidad de Fabric. Confirme con el docente si la Universidad la ofrece a los estudiantes. Sin licencia, la Parte B se evalúa con *Ver como* en Power BI Desktop.

Si hay licencia:
1. Publique en un área de trabajo del equipo.
2. En *Seguridad* del modelo semántico, asigne las cuentas reales del equipo al rol.
3. Configure la actualización programada. Es una buena oportunidad para discutir por qué la API de TRM se actualiza sin credenciales y la base de datos necesita credenciales guardadas en el servicio.

## Entregable (dentro del Avance 2)
Capturas de *Ver como* para tres usuarios (comité, un gerente regional y un correo no registrado), con el total pagado que ve cada uno, y la respuesta a las preguntas de control 1 y 2.
