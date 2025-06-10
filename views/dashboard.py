from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QGridLayout

class Dashboard(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        
        layout = QGridLayout()
        
        # Botones principales
        botones = [
            ("📦 Ajustes", "ajustes"),
            ("📥 Entradas", "entradas"),
            ("📤 Salidas", "salidas"),
            ("📊 Reportes", "reportes"),
            ("🔍 Buscar", "busqueda")
        ]
        
        for i, (texto, pantalla) in enumerate(botones):
            btn = QPushButton(texto)
            btn.clicked.connect(lambda _, p=pantalla: self.parent.ir_a(p))
            layout.addWidget(btn, i // 2, i % 2)  # Distribución en grid 2x3
        
        self.setLayout(layout)