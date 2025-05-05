# 🔥 Monitoreo de Noticias sobre Incendios Forestales en el Estado de México

## 📅 Periodo de análisis

2025 (actualización en tiempo real)

## 📚 Resumen

Los incendios forestales representan una amenaza constante para los ecosistemas del Estado de México. Este proyecto propone un sistema automatizado para **recopilar, analizar y visualizar noticias** relacionadas con incendios forestales mediante técnicas de web scraping, procesamiento de lenguaje natural y geolocalización.

Se integran herramientas de Python para obtener titulares y oraciones clave desde portales de noticias locales, detectar menciones a incendios, identificar posibles ubicaciones y mostrar los resultados en una **aplicación web interactiva con mapas y gráficas**.

El sistema está pensado como un módulo base para alimentar futuros modelos predictivos o clasificadores de impacto ambiental.

## 🔍 Tecnologías y herramientas

- Python 3.13
- Selenium + ChromeDriver
- geopy (Nominatim)
- pandas, re, csv
- Streamlit
- folium + streamlit-folium
- plotly

## 💡 Objetivos

- Automatizar la detección de noticias relevantes sobre incendios forestales
- Extraer oraciones que contengan palabras clave y asociarlas a ubicaciones geográficas
- Visualizar los eventos en un visor interactivo con filtros, gráficas y mapas


## 📃 Datos procesados

- Noticias de portales del Estado de México:
  - El Sol de Toluca
  - La Jornada Edomex
  - Quadratín Edomex
  - AD Noticias
  - Milenio Edomex
  - CONAFOR
  - CONANP
  - Protección Civil Edomex
- Palabras clave: incendio, quema, bosque, brigadistas, humo, etc.
- Ubicaciones detectadas por mención de municipios
- Coordenadas geográficas obtenidas con Nominatim (geopy)

## 📊 Visualización de resultados

- Tabla filtrable por palabra clave y fuente
- Gráfica de barras con frecuencia de ocurrencias
- Mapa interactivo con los puntos geográficos detectados
- Botón de descarga CSV de resultados filtrados

## 🚀 Cómo ejecutar

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
python 01-scraper_incendios.py
streamlit run 02-app.py

🌐 Autor
Raúl Alfonso Rodríguez Ruelas
GitHub
LinkedIn

✍️ Cita sugerida
Rodríguez Ruelas, R. A. (2025). Monitoreo de noticias sobre incendios forestales en el Estado de México. GitHub Repository. https://github.com/Rodriguez-Ruelas
