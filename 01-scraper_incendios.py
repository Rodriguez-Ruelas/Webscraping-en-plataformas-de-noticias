import csv
import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

# Ruta al ChromeDriver
CHROMEDRIVER_PATH = "C:/Users/raulr/Desktop/PROFEPA/Webscraping/chromedriver-win64/chromedriver.exe"

#  Palabras clave relacionadas con incendios forestales
palabras_clave_incendio = [
    "incendio", "quema", "fuego", "llamas", "brasa", "ceniza", "humo", "carbonización",
    "ardiendo", "propagación", "chispa", "ignición", "bosque", "forestal", "pinos",
    "matorral", "sotobosque", "arbolado", "maleza", "pastizal", "vegetación seca",
    "zona boscosa", "sierra", "ladera", "cerro", "bomberos", "brigadistas", "controlado",
    "sofocado", "combate", "helicóptero", "retardante", "evacuación", "alerta",
    "contingencia", "peritaje", "hectáreas afectadas", "pérdida forestal", "afectación",
    "daño ambiental", "fauna desplazada", "riesgo ecológico", "quemas agrícolas",
    "fogata", "corto circuito", "pirotecnia", "actividad humana", "vandalismo", "negligencia"
]

# Municipios comunes para detección automática
lugares_ejemplo = [
    "Valle de Bravo", "Ocuilan", "Toluca", "Ixtapan de la Sal", "Zinacantepec", "Temascaltepec",
    "Tenancingo", "Lerma", "Tlalmanalco", "Coatepec Harinas", "Amanalco", "Villa Victoria"
]

# Portales a revisar
portales = {
    "El Sol de Toluca": "https://oem.com.mx/elsoldetoluca/",
    "La Jornada Edomex": "https://estadodemexico.jornada.com.mx/",
    "Quadratín Edomex": "https://edomex.quadratin.com.mx/",
    "AD Noticias": "https://adnoticias.mx/",
    "Milenio Edomex": "https://www.milenio.com/estado-de-mexico",
    "CONAFOR": "https://www.gob.mx/conafor/prensa",
    "CONANP": "https://www.conanp.gob.mx/",
    "Protección Civil Edomex": "https://proteccioncivil.edomex.gob.mx/"
}

# Configurar navegador
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")
service = Service(CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

# Función para extraer fecha
def buscar_fecha(driver):
    tags = ["time", "span", "p", "div", "header"]
    for tag in tags:
        try:
            elems = driver.find_elements(By.TAG_NAME, tag)
            for el in elems:
                texto = el.text.strip()
                if re.search(r"\d{1,2} de \w+ de \d{4}", texto.lower()):
                    return texto
        except:
            continue
    return "Fecha no encontrada"

# Función para detectar municipio en oración
def detectar_lugar(oracion):
    for lugar in lugares_ejemplo:
        if isinstance(oracion, str) and lugar.lower() in oracion.lower():
            return f"{lugar}, Estado de México"
    return None

# Geolocalización
geolocator = Nominatim(user_agent="incendios-app")
coordenadas = {}

# Archivo final
filename = "oraciones_incendios_geolocalizado.csv"
with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Fuente", "Título", "Fecha", "Link", "Palabra clave", "Oración", "Lugar detectado", "Latitud", "Longitud"])

    for fuente, url in portales.items():
        print(f"\n🌐 Visitando {fuente}")
        try:
            driver.get(url)
            time.sleep(4)
            articles = driver.find_elements(By.TAG_NAME, "article")
            article_links = []

            for article in articles:
                try:
                    link_tag = article.find_element(By.TAG_NAME, "a")
                    title = link_tag.text.strip()
                    link = link_tag.get_attribute("href")
                    if title and link and link.startswith("http"):
                        article_links.append((title, link))
                except:
                    continue

            print(f"🔎 {len(article_links)} artículos encontrados.")

            for title, link in article_links:
                try:
                    driver.execute_script("window.open(arguments[0]);", link)
                    driver.switch_to.window(driver.window_handles[1])
                    time.sleep(2)

                    date = buscar_fecha(driver)
                    body_text = ""
                    for p in driver.find_elements(By.TAG_NAME, "p"):
                        body_text += p.text.strip() + " "

                    oraciones = re.split(r'(?<=[.?!])\s+', body_text)

                    for palabra in palabras_clave_incendio:
                        for oracion in oraciones:
                            if palabra.lower() in oracion.lower():
                                lugar = detectar_lugar(oracion)
                                lat, lon = None, None
                                if lugar:
                                    if lugar in coordenadas:
                                        lat, lon = coordenadas[lugar]
                                    else:
                                        try:
                                            location = geolocator.geocode(lugar, timeout=10)
                                            if location:
                                                lat, lon = location.latitude, location.longitude
                                                coordenadas[lugar] = (lat, lon)
                                            time.sleep(1)
                                        except GeocoderTimedOut:
                                            pass

                                writer.writerow([fuente, title, date, link, palabra, oracion.strip(), lugar, lat, lon])
                                print(f"✅ '{palabra}' detectado en {fuente}: {oracion.strip()[:100]}...")

                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                except Exception as e:
                    print(f"❌ Error procesando artículo: {e}")
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    continue

        except Exception as e:
            print(f"⚠️ No se pudo acceder a {fuente}: {e}")
            continue

driver.quit()
print(f"\n📁 ¡Archivo '{filename}' generado con éxito!")
