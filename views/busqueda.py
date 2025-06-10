from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem
import sqlite3

class BusquedaWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        
        layout = QVBoxLayout()
        
        self.busqueda_input = QLineEdit()
        self.busqueda_input.setPlaceholderText("Buscar por código o nombre...")
        
        btn_buscar = QPushButton("🔍 Buscar")
        btn_buscar.clicked.connect(self.buscar_producto)
        
        self.tabla_resultados = QTableWidget()
        self.tabla_resultados.setColumnCount(3)
        self.tabla_resultados.setHorizontalHeaderLabels(["Código", "Nombre", "Stock Físico"])
        
        layout.addWidget(self.busqueda_input)
        layout.addWidget(btn_buscar)
        layout.addWidget(self.tabla_resultados)
        self.setLayout(layout)
    
    def buscar_producto(self):
        conn = sqlite3.connect("inventario.db")
        cursor = conn.cursor()
        query = f"SELECT codigo, nombre, stock_fisico FROM productos WHERE codigo LIKE '%{self.busqueda_input.text()}%' OR nombre LIKE '%{self.busqueda_input.text()}%'"
        cursor.execute(query)
        resultados = cursor.fetchall()
        conn.close()
        
        self.tabla_resultados.setRowCount(len(resultados))
        for i, row in enumerate(resultados):
            self.tabla_resultados.setItem(i, 0, QTableWidgetItem(row[0]))
            self.tabla_resultados.setItem(i, 1, QTableWidgetItem(row[1]))
            self.tabla_resultados.setItem(i, 2, QTableWidgetItem(str(row[2])))