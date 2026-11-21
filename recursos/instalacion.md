# Instalación y entorno de trabajo

Todo el curso puede hacerse **sin licencias de pago**.

## 1. Windows (recomendado)

1. Instalar **Power BI Desktop**, que es gratuito, desde Microsoft Store o desde el Centro de descargas de Microsoft. Guía oficial: https://learn.microsoft.com/es-es/power-bi/fundamentals/desktop-get-the-desktop
2. Descargar este repositorio: *Code → Download ZIP* en GitHub, o `git clone`.
3. En Power BI, crear el parámetro `RutaDatos` con la ruta local de la carpeta `datos\` terminada en `\`. Ver [práctica 01](../practicas-powerbi/01_power_query/README.md).
4. *Para el T0 y la profundización C:* usar **Google Colab** (sin instalar nada, con una cuenta de Google) o instalar Python 3.10 o superior y ejecutar `pip install -r scripts/requirements.txt`. En Power BI, ir a *Archivo → Opciones → Scripts de Python* y seleccionar el directorio de Python. Guía: https://learn.microsoft.com/es-es/power-bi/connect-data/desktop-python-scripts

## 2. Mac

Power BI Desktop **no tiene versión para macOS**. Hay cuatro alternativas, de mayor a menor recomendación:

| Opción | Cómo | Ventajas | Limitaciones |
|---|---|---|---|
| A. Sala de cómputo de la Universidad | Reservar sala según la disponibilidad que indica el syllabus oficial | Sin costo ni instalación | Depende del horario de la sala |
| B. Máquina virtual con Windows 11 | Parallels Desktop (de pago, con prueba gratuita), VMware Fusion o UTM en Mac con Apple Silicon, con Windows 11 para ARM | Experiencia completa de Power BI Desktop | Licencias de virtualización y de Windows. Requiere 8 GB de RAM o más. En ARM, Power BI funciona por emulación. **Pendiente de verificación:** requisitos y soporte oficial de Microsoft para Windows en ARM y en entornos virtualizados en Mac (las fuentes consultadas difieren) |
| C. Escritorio remoto a un PC con Windows | Microsoft Remote Desktop / Windows App hacia un equipo propio o de la Universidad | Sin instalación local pesada | Requiere un PC con Windows disponible y buena conexión |
| D. Power BI Service (web) | app.powerbi.com con cuenta institucional | Funciona en el navegador | Editar Power Query y el modelo en la web tiene limitaciones frente a Desktop. Las capacidades exactas dependen de la licencia de la cuenta institucional (**pendiente de verificación** con TI de la Universidad). Compartir requiere licencia Pro |

**Plan mínimo para Mac sin ninguna de las anteriores:** el T0 puede hacerse en **Google Colab** y los talleres T1–T2 con **Power Query en Excel para Mac**, con funciones de edición más limitadas que en Windows, y los scripts de Python de `scripts/` corren en macOS sin cambios. En ese caso, el estudiante entrega capturas y el archivo de Excel en lugar del `.pbix`, y debe coordinar con su equipo que un integrante con Windows consolide el tablero del caso integrador.

## 3. Conexión a la base de datos del caso integrador (rama `fuentes-organizacionales`)

Cuando el docente entregue los datos de conexión de su equipo, siga la [guía de conexión a la base de datos](conexion_base_datos.md).

## 4. Verificación del entorno (Taller T0)

- [ ] Power BI Desktop abre y muestra la versión en *Ayuda → Acerca de*.
- [ ] Se cargó `datos/integrador/pagos.csv` y la vista previa muestra 12 columnas.
- [ ] El cuaderno `unidad-1/t0_exploracion_pagos.ipynb` abre (en Colab o en su computador) y `pd.read_csv` carga `pagos.csv` con 12 columnas.
- [ ] *(Opcional)* `python scripts/deteccion_anomalias.py` se ejecuta sin errores.
