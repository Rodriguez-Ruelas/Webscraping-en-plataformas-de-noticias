# main.py - Lanzador

from PyQt5.QtWidgets import QApplication
from MVC_Controlador import Controlador
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Controlador()
    ventana.show()
    sys.exit(app.exec_())