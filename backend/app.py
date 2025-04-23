from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from db import init_db
import os

app = Flask(__name__)
CORS(app)
init_db()

@app.route('/dispositivos', methods=['GET'])
def listar():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, '..', 'database', 'dispositivos.db')

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM dispositivos")
    dispositivos = c.fetchall()
    conn.close()
    return jsonify(dispositivos)

@app.route('/dispositivos', methods=['POST'])
def adicionar():
    data = request.json
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, '..', 'database', 'dispositivos.db')

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO dispositivos (ip, nome, taxa) VALUES (?, ?, ?)", 
              (data['ip'], data['nome'], data['taxa']))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Dispositivo adicionado com sucesso'}), 201

@app.route('/dispositivos/<int:id>', methods=['DELETE'])
def remover(id):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DB_PATH = os.path.join(BASE_DIR, '..', 'database', 'dispositivos.db')

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM dispositivos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': 'Dispositivo removido com sucesso'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
