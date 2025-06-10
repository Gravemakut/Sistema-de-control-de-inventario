import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from views.dashboard import Dashboard
from views.ajustes import AjustesWindow
from views.reportes import ReportesWindow
from views.busqueda import BusquedaWindow
from views.entradas import EntradasWindow
from views.salidas import SalidasWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventario+ v2.0")
        self.resize(800, 500)  # Tamaño más adecuado
        
        # Stacked Widget para navegar
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        # Pantallas
        self.pantallas = {
            "dashboard": Dashboard(self),
            "ajustes": AjustesWindow(self),
            "reportes": ReportesWindow(self),
            "busqueda": BusquedaWindow(self),
            "entradas": EntradasWindow(self),
            "salidas": SalidasWindow(self)
        }
        
        # Agregar pantallas
        for pantalla in self.pantallas.values():
            self.stacked_widget.addWidget(pantalla)
        
        # Mostrar dashboard inicial
        self.ir_a("dashboard")

    def ir_a(self, nombre_pantalla):
        self.stacked_widget.setCurrentWidget(self.pantallas[nombre_pantalla])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())