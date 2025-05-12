import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.corpus import udhr

# Descargar recursos necesarios
nltk.download('punkt')
nltk.download('udhr')

def scrapear_real(url, palabra):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return {
            "mensaje": f"❌ Error al acceder a {url}: {e}",
            "conteo": 0,
            "contextos": []
        }

    soup = BeautifulSoup(response.text, "html.parser")
    texto_crudo = soup.get_text(separator=" ").lower()

    # 🔍 Limpieza más agresiva
    texto_limpio = re.sub(r"\s+", " ", texto_crudo)  # Quitar múltiples espacios
    lineas = [line.strip() for line in texto_limpio.split(".") if len(line.strip()) > 40]  # Ignorar líneas cortas

    # Reunimos texto para tokenizar
    texto = ". ".join(lineas)

    palabra = palabra.lower()

    try:
        trainer_text = udhr.raw('Spanish_Espanol-Latin1')
        tokenizer = PunktSentenceTokenizer(trainer_text)
        oraciones = tokenizer.tokenize(texto)
    except Exception as e:
        return {
            "mensaje": f"⚠️ Error al tokenizar texto: {e}",
            "conteo": 0,
            "contextos": []
        }

    contextos = [o.strip() for o in oraciones if palabra in o]
    resaltadas = [o.replace(palabra, f"**{palabra.upper()}**") for o in contextos]

    return {
        "mensaje": f"🔍 '{palabra}' en {url}: {len(contextos)} coincidencia(s)",
        "conteo": len(contextos),
        "contextos": resaltadas[:20]
    }