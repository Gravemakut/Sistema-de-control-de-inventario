# database.py
import sqlite3
import sys
import os

def get_db_path():
    """Obtiene la ruta correcta para la base de datos, tanto en desarrollo como en .exe"""
    if getattr(sys, 'frozen', False):
        # Si está empaquetado (ejecutándose desde .exe)
        return os.path.join(sys._MEIPASS, "inventario.db")
    else:
        # Si está en desarrollo
        return "inventario.db"

def crear_db():
    db_path = get_db_path()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Tabla de productos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        codigo TEXT PRIMARY KEY,
        nombre TEXT,
        stock_sistema REAL,
        stock_fisico REAL
    )
    ''')
    
    # Tabla de ajustes
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ajustes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        producto_id TEXT,
        cantidad_anterior REAL,
        cantidad_nueva REAL,
        tipo TEXT,
        motivo TEXT,
        usuario TEXT,
        fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (producto_id) REFERENCES productos (codigo)
    )
    ''')
    
    # Datos de ejemplo (opcional)
    cursor.execute("INSERT OR IGNORE INTO productos VALUES ('PROD-001', 'Tornillo 5mm', 100, 100)")
    conn.commit()
    conn.close()

# Ejecutar al importar
crear_db()