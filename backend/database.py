import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    """
    Estabelece uma conexão com o banco de dados PostgreSQL usando as credenciais e configurações
    fornecidas através de variáveis de ambiente.

    Retorna:
        connection (psycopg2.extensions.connection): Objeto de conexão com o banco de dados.
    """
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        cursor_factory=RealDictCursor
    )
    return connection
