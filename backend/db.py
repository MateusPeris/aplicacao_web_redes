import sqlite3
import os

def init_db():
    # Caminho absoluto da pasta database, relativo ao local do script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_dir = os.path.join(base_dir, '..', 'database')
    db_path = os.path.join(db_dir, 'dispositivos.db')

    # Garante que a pasta existe
    os.makedirs(db_dir, exist_ok=True)

    # Conecta ao banco
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS dispositivos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT NOT NULL,
            nome TEXT NOT NULL,
            taxa REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()