# MVC_Vista.py - Vista (View)

from PyQt5.QtWidgets import QWidget
from Interfaz_UI import Ui_Form

class VistaPrincipal(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Personalización visual (puedes mover esto a gusto)
        self.setWindowTitle("Scraper")
        self.textEditScraping.setReadOnly(True)
        self.progressBarScraping.setValue(0)

        # Opcional: placeholders o estilos iniciales
        self.lineEditURL.setPlaceholderText("https://ejemplo.com")
        self.lineEditKeyWords.setPlaceholderText("Palabra clave")

