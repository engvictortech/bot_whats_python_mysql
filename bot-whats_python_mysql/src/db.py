import os
from dotenv import load_dotenv
import mysql.connector

# Carrega o .env da raiz do projeto
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST") or "127.0.0.1",
            port=int(os.getenv("DB_PORT") or 3306),
            user=os.getenv("DB_USER") or "bot_user",
            password=os.getenv("DB_PASSWORD") or "SUA_SENHA",
            database=os.getenv("DB_NAME") or "botdb",
            use_pure=True
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Erro ao conectar: {e}")
        return None

def test_connection():
    conn = get_connection()
    if conn:
        print("Conexão bem-sucedida ✅")
        conn.close()
    else:
        print("Falha na conexão ❌")

def init_db():
    """Cria a tabela messages se não existir"""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INT AUTO_INCREMENT PRIMARY KEY,
                sender VARCHAR(255) NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()

def insert_message(sender, message):
    """Insere uma mensagem na tabela"""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO messages (sender, message) VALUES (%s, %s)",
            (sender, message)
        )
        conn.commit()
        conn.close()

def list_messages():
    """Lista todas as mensagens"""
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, sender, message, created_at FROM messages")
        rows = cursor.fetchall()
        conn.close()
        return rows
    return []

def insert_message(sender, message):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (sender, message) VALUES (%s, %s)", (sender, message))
    conn.commit()
    cursor.close()
    conn.close()

