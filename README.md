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

## 👤 Autor

**Raúl Alfonso Rodríguez Ruelas**

[GitHub](https://github.com/Rodriguez-Ruelas)  
[LinkedIn](https://www.linkedin.com/in/raul-rodriguez-ruelas-20634a171/)

---

> *Rodríguez Ruelas, R. A. (2025). Sistema de Web Scraping para Monitoreo de Noticias Ambientales. GitHub Repository. https://github.com/Rodriguez-Ruelas*

