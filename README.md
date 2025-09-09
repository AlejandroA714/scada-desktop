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

### 📊 **Monitoreo en tiempo real**  
Visualización de variables analógicas y digitales con actualización en vivo.
<p align="center">
  <img src="./docs/sensors.gif" width="480" alt="Abrir app">
</p>
  
- 🔔 **Notificaciones de eventos**  
  Integración con [**pyqt5-notificator**](https://github.com/AlejandroA714/pyqt5-notificator), un paquete propio que permite mostrar alertas de escritorio cuando se cumplen condiciones críticas.

- 🎨 **Colores personalizados**  
  Asignación de colores a cada variable para facilitar la identificación en paneles.

- 🧮 **Expresiones evaluables**  
  Uso de [py-expression-eval](https://pypi.org/project/py-expression-eval/) para definir fórmulas personalizadas sobre los valores monitoreados.

- 📑 **Gestión de reportes en Excel**  
  Exportación de registros y tendencias en formato **.xlsx** mediante [openpyxl](https://pypi.org/project/openpyxl/).

- ☁️ **Conexión a MongoDB**  
  Almacenamiento y consulta de datos históricos usando [pymongo](https://pypi.org/project/pymongo/).

- ⚡ **Interfaz amigable**  
  Construida sobre **PyQt5**, con soporte para temas claros/oscuro y estilos personalizables.

---