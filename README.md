# 🔥 Sistema de Web Scraping para Monitoreo de Noticias

## 🧪 Contexto

Este proyecto plantea una **solución práctica para el monitoreo automatizado de noticias** mediante web scraping, útil para dependencias gubernamentales, instituciones educativas, investigadores o cualquier usuario que necesite **recabar información de manera rápida y estructurada** desde medios digitales.

El sistema permite extraer oraciones clave desde páginas de noticias en línea, detectando menciones a temas específicos como *“bosques”*, *“incendios”*, *“brigadas”*, *“zonas protegidas”*, o cualquier palabra clave definida por el usuario. Esto facilita la construcción de bases de datos orientadas al análisis temático, seguimiento de eventos o clasificación automática.

## 🎯 Propósito del proyecto

Desarrollar una herramienta que permita **automatizar la detección y extracción de fragmentos relevantes** en noticias digitales, usando palabras clave definidas por el usuario, todo dentro de una interfaz gráfica sencilla. El objetivo es facilitar tareas de monitoreo, recolección de datos o exploración temática para diversos fines analíticos o académicos.

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
