# 🔥 Monitoreo de Noticias sobre Incendios Forestales en el Estado de México

## 📅 Periodo de análisis

2025 (actualización en tiempo real)

## 📚 Resumen

Los incendios forestales representan una amenaza constante para los ecosistemas del Estado de México. Este proyecto propone un sistema automatizado para **recopilar, analizar y visualizar noticias** relacionadas con incendios forestales mediante técnicas de web scraping, procesamiento de lenguaje natural y geolocalización.

Se integran herramientas de Python para obtener titulares y oraciones clave desde portales de noticias locales, detectar menciones a incendios, identificar posibles ubicaciones y mostrar los resultados en una **aplicación web interactiva con mapas y gráficas**.

El sistema está pensado como un módulo base para alimentar futuros modelos predictivos o clasificadores de impacto ambiental.

---

## 🔍 Tecnologías y herramientas

* Python 3.13
* Selenium + ChromeDriver
* geopy (Nominatim)
* pandas, re, csv
* Streamlit
* folium + streamlit-folium
* plotly

---

## 💡 Objetivos

* Automatizar la detección de noticias relevantes sobre incendios forestales
* Extraer oraciones que contengan palabras clave y asociarlas a ubicaciones geográficas
* Visualizar los eventos en un visor interactivo con filtros, gráficas y mapas

---

## 📂 Estructura del proyecto

/
├── 01-scraper_incendios.py # Extrae oraciones clave de portales noticiosos y geolocaliza si detecta un municipio
├── 02-app.py # Visor interactivo con filtros, mapa y gráficas
├── oraciones_incendios_geolocalizado.csv # Archivo generado automáticamente con los resultados

yaml
Copiar
Editar

---
