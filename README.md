# 🔥 Sistema de Web Scraping para Monitoreo de Noticias Ambientales

## 🧪 Contexto

Este proyecto plantea una **solución práctica de monitoreo de noticias basada en web scraping**, diseñada para apoyar a instituciones como **PROFEPA**, **Protección Civil** u otras dependencias interesadas en el análisis automatizado de medios digitales para la **detección temprana de eventos ambientales**, como incendios forestales.

El sistema se enfoca en capturar y analizar oraciones clave desde noticias en línea, relacionadas con palabras como “bosque”, “incendio”, “humo”, etc., con el objetivo de construir una base de datos que pueda alimentar futuros modelos de análisis o visualización.

## 🎯 Propósito del proyecto

Detectar noticias relevantes sobre eventos forestales o ambientales mediante palabras clave, extraer fragmentos de texto representativos, y permitir su inspección y análisis a través de una interfaz gráfica amigable.

## 🛠️ Componentes principales

Este proyecto implementa un **sistema de scraping local con interfaz gráfica (GUI)** desarrollado en Python utilizando el patrón Modelo-Vista-Controlador (MVC).

### 🔧 Funcionalidades:

- **Interfaz gráfica (GUI)** con PyQt5 (diseñada en Qt Designer)
- **Carga de URLs y palabras clave** desde la GUI
- **Scraping de texto** con `requests` + `BeautifulSoup`
- **Limpieza y separación de oraciones** con `nltk` entrenado en español
- **Identificación de oraciones que contienen palabras clave**
- **Visualización en tiempo real** dentro de la GUI con barra de progreso
- **Exportación a Excel** (`.xlsx`) estructurado con `pandas`
- **Compilación en ejecutable (.exe)** usando PyInstaller

## 🧩 Cómo funciona la aplicación

La aplicación cuenta con una **interfaz gráfica intuitiva** que permite:

1. Ingresar múltiples **URLs de noticias** desde el campo superior izquierdo.  
2. Agregar **palabras clave** desde el campo superior derecho (por ejemplo: “incendio”, “bosque”, “humo”, “choix”, etc.).  
3. Presionar el botón “Iniciar” para comenzar el scraping.

Durante la ejecución, la aplicación:

- Accede a cada URL proporcionada y descarga el texto de la página.
- Limpia el contenido y lo divide en oraciones usando `nltk`.
- Identifica aquellas oraciones que contienen las palabras clave seleccionadas.
- Muestra los resultados en tiempo real dentro del panel inferior, incluyendo errores de acceso o coincidencias encontradas.
- Al finalizar, **exporta los datos** en un archivo Excel (`resultados_scraping.xlsx`) con las columnas:
  - URL
  - Palabra clave
  - Número de coincidencia
  - Contexto de la oración

También se incluye una barra de progreso y un botón para guardar manualmente los datos si lo deseas.

### 🖼️ Vista de la aplicación

<p align="center">
  <img src="https://github.com/Rodriguez-Ruelas/Webscraping-en-plataformas-de-noticias/blob/main/Image/01_app.PNG" width="500">
</p>
<p align="center"><em>Figura 1. Interfaz principal al iniciar la aplicación.</em></p>

<p align="center">
  <img src="https://github.com/Rodriguez-Ruelas/Webscraping-en-plataformas-de-noticias/blob/main/Image/02_app.PNG" width="500">
</p>
<p align="center"><em>Figura 2. Resultados mostrados tras ejecutar el scraping con varias URLs y palabras clave.</em></p>

---

## 👤 Autor

**Raúl Alfonso Rodríguez Ruelas**  
[GitHub](https://github.com/Rodriguez-Ruelas)  
[LinkedIn](https://www.linkedin.com/in/raul-rodriguez-ruelas-20634a171/)

---

> *Rodríguez Ruelas, R. A. (2025). Sistema de Web Scraping para Monitoreo de Noticias Ambientales. GitHub Repository. https://github.com/Rodriguez-Ruelas*
