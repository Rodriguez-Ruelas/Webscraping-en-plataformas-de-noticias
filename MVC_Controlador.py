# MVC_Controlador.py - Controlador (Controller)

from PyQt5.QtWidgets import QMessageBox
from MVC_Vista import VistaPrincipal
from MVC_Modelo import scrapear_real
import pandas as pd

class Controlador(VistaPrincipal):
    def __init__(self):
        super().__init__()

        # Conectar señales
        self.BtnAddURL.clicked.connect(self.agregar_url)
        self.BtnAddKeyWords.clicked.connect(self.agregar_palabra)
        self.BtnScrapingON.clicked.connect(self.iniciar_scraping)
        self.BtnDeleteURL.clicked.connect(self.eliminar_url_seleccionada)
        self.BtnDeleteKeyWords.clicked.connect(self.eliminar_keyword_seleccionada)
        self.BtnGuardarExcel.clicked.connect(self.guardar_scraping)
       

        # Lista interna
        self.urls = []
        self.palabras = []

        self.resultados = []

    def agregar_url(self):
        texto = self.lineEditURL.text().strip()
        if texto:
            self.urls.append(texto)
            self.listWidgetUrls.addItem(texto)
            self.lineEditURL.clear()

    def eliminar_url_seleccionada(self):
        fila = self.listWidgetUrls.currentRow()
        if fila >= 0:
            texto = self.listWidgetUrls.item(fila).text()
            self.listWidgetUrls.takeItem(fila)
            if texto in self.urls:
                self.urls.remove(texto)
            self.textEditScraping.append(f"❌ URL eliminada: {texto}")
        else:
            self.textEditScraping.append("⚠️ No se ha seleccionado ninguna URL.")

    def agregar_palabra(self):
        texto = self.lineEditKeyWords.text().strip()
        if texto:
            self.palabras.append(texto)
            self.listWidgetKeyWords.addItem(texto)
            self.lineEditKeyWords.clear()
    
    def eliminar_keyword_seleccionada(self):
        fila = self.listWidgetKeyWords.currentRow()
        if fila >= 0:
            texto = self.listWidgetKeyWords.item(fila).text()
            self.listWidgetKeyWords.takeItem(fila)
            if texto in self.urls:
                self.urls.remove(texto)
            self.textEditScraping.append(f"❌ URL eliminada: {texto}")
        else:
            self.textEditScraping.append("⚠️ No se ha seleccionado ninguna URL.")            
    
    def Imprimir_Lista(self):
        self.textEditScraping.append("📄 Lista de URLs:")
        for i, url in enumerate(self.urls, 1):
            self.textEditScraping.append(f"  {i}. {url}")

    def iniciar_scraping(self):
        if not self.urls or not self.palabras:
            QMessageBox.warning(self, "Faltan datos", "Agrega al menos una URL y una palabra clave.")
            return

        self.textEditScraping.append("🧪 Iniciando scraping...")
        total = len(self.urls) * len(self.palabras)
        self.progressBarScraping.setMaximum(total)
        progreso = 0

        self.resultados = []

        for url in self.urls:
            for palabra in self.palabras:
                resultado = scrapear_real(url, palabra)
                self.textEditScraping.append(resultado["mensaje"])

                for i, frase in enumerate(resultado["contextos"], 1):
                    self.resultados.append({
                        "URL": url,
                        "Palabra": palabra,
                        "Coincidencia #": i,
                        "Contexto": frase
                    })

                progreso += 1
                self.progressBarScraping.setValue(progreso)

    def guardar_scraping(self):
        try:
            df = pd.DataFrame(self.resultados)
            df.to_excel("resultados_scraping.xlsx", index=False)
            self.textEditScraping.append("📁 Resultados guardados en 'resultados_scraping.xlsx'")
        except Exception as e:
            self.textEditScraping.append(f"❌ Error al guardar archivo: {e}")
