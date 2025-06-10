from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton

class EntradasWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        
        layout = QVBoxLayout()
        
        self.codigo = QLineEdit(placeholderText="Código del producto")
        self.cantidad = QLineEdit(placeholderText="Cantidad recibida")
        
        btn_guardar = QPushButton("💾 Guardar Entrada")
        btn_guardar.clicked.connect(self.guardar_entrada)
        
        btn_atras = QPushButton("🔙 Atrás")
        btn_atras.clicked.connect(lambda: self.parent.ir_a("dashboard"))
        
        layout.addWidget(self.codigo)
        layout.addWidget(self.cantidad)
        layout.addWidget(btn_guardar)
        layout.addWidget(btn_atras)
        self.setLayout(layout)
    
    def guardar_entrada(self):
        # Lógica para guardar en SQLite
        print(f"Entrada registrada: {self.codigo.text()}, {self.cantidad.text()}")