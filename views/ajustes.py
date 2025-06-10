from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QMessageBox
import sqlite3

class AjustesWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        
        # Layout
        layout = QVBoxLayout()
        
        # Campos del formulario
        self.codigo = QLineEdit()
        self.codigo.setPlaceholderText("Código del Producto (ej: PROD-001)")
        
        self.stock_fisico = QLineEdit()
        self.stock_fisico.setPlaceholderText("Cantidad Física")
        
        self.tipo_ajuste = QComboBox()
        self.tipo_ajuste.addItems(["Diferencia", "Daño", "Pérdida", "Donación"])
        
        self.motivo = QLineEdit()
        self.motivo.setPlaceholderText("Motivo del ajuste")
        
        btn_guardar = QPushButton("💾 Guardar Ajuste")
        btn_guardar.clicked.connect(self.guardar_ajuste)
        
        # Agregar widgets al layout
        layout.addWidget(QLabel("Registrar Ajuste"))
        layout.addWidget(self.codigo)
        layout.addWidget(self.stock_fisico)
        layout.addWidget(self.tipo_ajuste)
        layout.addWidget(self.motivo)
        layout.addWidget(btn_guardar)
        self.setLayout(layout)
    
    def guardar_ajuste(self):
        conn = sqlite3.connect("inventario.db")
        cursor = conn.cursor()
        
        try:
            cursor.execute(
                "INSERT INTO ajustes (producto_id, cantidad_anterior, cantidad_nueva, tipo, motivo, usuario) VALUES (?, ?, ?, ?, ?, ?)",
                (self.codigo.text(), 100, float(self.stock_fisico.text()), self.tipo_ajuste.currentText(), self.motivo.text(), "Admin")
            )
            conn.commit()
            QMessageBox.information(self, "Éxito", "¡Ajuste registrado correctamente!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al guardar: {str(e)}")
        finally:
            conn.close()