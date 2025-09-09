# SCADA Desktop

Aplicación de escritorio desarrollada en **Python 3.8** con **PyQt5**.  
Incluye integración con MongoDB, manejo de expresiones evaluables, colores web, hojas de cálculo Excel, y notificaciones a través del paquete propio **pyqt5-notificator**.

---

## 🚀 Requisitos

- Python **3.8.x**
- pip actualizado
- MongoDB (si la app se conecta a una base de datos real)

---

## 📦 Instalación

1. Clonar o descargar el proyecto:

   ```bash
   git clone https://github.com/tuusuario/scada-desktop.git
   cd scada-desktop
# 🖥️ SCADA Desktop

**SCADA Desktop** es una aplicación de escritorio desarrollada en **Python 3.8** con **PyQt5**, diseñada para la **supervisión y control de variables** en sistemas industriales y de automatización.  
Ofrece una interfaz moderna, soporte de notificaciones en tiempo real y conectividad con bases de datos, permitiendo a los usuarios gestionar datos, alarmas y reportes de forma sencilla.

---

## ✨ Funcionalidades principales

- 🎛️ **Interfaz gráfica moderna e intuitiva**  
  Desarrollada con PyQt5, incluye menús, paneles y ventanas personalizadas.
<p align="center">
  <img src="./docs/login.png" width="480" alt="Abrir app">
</p>
<p align="center">
  <img src="./docs/main.png" width="480" alt="Abrir app">
</p>

- 📊 **Monitoreo en tiempo real**  
Visualización de variables analógicas y digitales con actualización en vivo.
<p align="center">
  <img src="./docs/sensors.gif" width="480" alt="Abrir app">
</p>
  
- 🔌 **Conexión con dispositivos externos**  
  Soporte para exportar e importar configuraciones rapidamente
  <p align="center">
  <img src="./docs/export.gif" width="480" alt="Abrir app">
</p>
<p align="center">
  <img src="./docs/import.gif" width="480" alt="Abrir app">
</p>

- 🗂️ **Creacion y edicion de RTUs**  
 Guarde y gestione diferentes espacios de trabajo
<p align="center">
  <img src="./docs/open.png" width="480" alt="Abrir app">
</p>

 Trabaje en mas multiples workspaces a la vez
<p align="center">
  <img src="./docs/workspaces.gif" width="480" alt="Abrir app">
</p>

 Arrastre y ubique a su antojo
<p align="center">
  <img src="./docs/grab.gif" width="480" alt="Abrir app">
</p>

 Visualice los dispositivos y cree nuevos
<p align="center">
  <img src="./docs/devices.png" width="480" alt="Abrir app">
</p>

 Cree y edite RTUs
<p align="center">
  <img src="./docs/devices-edit.png" width="480" alt="Abrir app">
</p>

 Cree nuevas variables
<p align="center">
  <img src="./docs/devices-var-add.gif" width="480" alt="Abrir app">
</p>

 Actualice imagen de referencia

<p align="center">
  <img src="./docs/image.gif" width="480" alt="Abrir app">
</p>

- **Gestion de usuarios**
Gestione usuarios administradores y normales

<p align="center">
  <img src="./docs/usuarios.png" width="480" alt="Abrir app">
</p>
Registre uno nuevo
<p align="center">
  <img src="./docs/usuarios-add.gif" width="520" alt="Abrir app">
</p>
Reciba su contrase;a por correo
<p align="center">
  <img src="./docs/usuarios-not.png" width="480" alt="Abrir app">
</p>

- 📑 **Exportación de reportes**  
  Posibilidad de exportar datos a formatos como Excel para análisis externo.
<p align="center">
  <img src="./docs/report.png" width="480" alt="Abrir app">
</p>

[📊 Ver reporte en Excel](./docs/report.xlsx)

---

## 🔧 Requisitos

- Python 3.8
- PyQt5
- Dependencias adicionales en `requirements.txt`

Instalación rápida:

```bash
pip install -r requirements.txt