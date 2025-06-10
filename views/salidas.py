from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QComboBox

class SalidasWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        
        layout = QVBoxLayout()
        
        self.codigo = QLineEdit(placeholderText="Código del producto")
        self.cantidad = QLineEdit(placeholderText="Cantidad despachada")
        self.destino = QComboBox()
        self.destino.addItems(["Sede Central", "Oficina Norte", "Taller"])
        
        btn_guardar = QPushButton("💾 Guardar Salida")
        btn_guardar.clicked.connect(self.guardar_salida)
        
        btn_atras = QPushButton("🔙 Atrás")
        btn_atras.clicked.connect(lambda: self.parent.ir_a("dashboard"))
        
        layout.addWidget(self.codigo)
        layout.addWidget(self.cantidad)
        layout.addWidget(self.destino)
        layout.addWidget(btn_guardar)
        layout.addWidget(btn_atras)
        self.setLayout(layout)
    
    def guardar_salida(self):
        # Lógica para guardar en SQLite
        print(f"Salida registrada: {self.codigo.text()}, {self.destino.currentText()}")