from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem
import sqlite3
import pandas as pd

class ReportesWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        
        layout = QVBoxLayout()
        
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(6)
        self.tabla.setHorizontalHeaderLabels(["Producto", "Stock Sistema", "Stock Físico", "Diferencia", "Fecha", "Usuario"])
        
        btn_actualizar = QPushButton("🔄 Actualizar Datos")
        btn_actualizar.clicked.connect(self.cargar_datos)
        
        btn_exportar = QPushButton("📤 Exportar a Excel")
        btn_exportar.clicked.connect(self.exportar_excel)
        
        layout.addWidget(self.tabla)
        layout.addWidget(btn_actualizar)
        layout.addWidget(btn_exportar)
        self.setLayout(layout)
        self.cargar_datos()
    
    def cargar_datos(self):
        conn = sqlite3.connect("inventario.db")
        df = pd.read_sql_query("SELECT * FROM ajustes", conn)
        conn.close()
        
        self.tabla.setRowCount(len(df))
        for i, row in df.iterrows():
            self.tabla.setItem(i, 0, QTableWidgetItem(row["producto_id"]))
            self.tabla.setItem(i, 1, QTableWidgetItem(str(row["cantidad_anterior"])))
            self.tabla.setItem(i, 2, QTableWidgetItem(str(row["cantidad_nueva"])))
            self.tabla.setItem(i, 3, QTableWidgetItem(str(row["cantidad_nueva"] - row["cantidad_anterior"])))
            self.tabla.setItem(i, 4, QTableWidgetItem(row["fecha"]))
            self.tabla.setItem(i, 5, QTableWidgetItem(row["usuario"]))
    
    def exportar_excel(self):
        conn = sqlite3.connect("inventario.db")
        df = pd.read_sql_query("SELECT * FROM ajustes", conn)
        df.to_excel("reporte_ajustes.xlsx", index=False)
        QMessageBox.information(self, "Éxito", "Reporte exportado a 'reporte_ajustes.xlsx'")