from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from database import get_db_connection
from fastapi.middleware.cors import CORSMiddleware
import logging
import hashlib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QueryRequest(BaseModel):
    query: str

class AuthRequest(BaseModel):
    nome: str
    senha: str

@app.post("/query")
def execute_query(request: QueryRequest):
    """
    Executa uma consulta SQL com base no objeto QueryRequest fornecido.

    Args:
        request (QueryRequest): Objeto contendo a consulta SQL a ser executada.

    Returns:
        dict: Um dicionário contendo os resultados da consulta ou uma mensagem de sucesso.

    Raises:
        HTTPException: Exceção levantada em caso de erro na execução da consulta, com código de status 400 e detalhes do erro.
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(request.query)
                if cursor.description:
                    results = cursor.fetchall()
                else:
                    results = {"message": "Query executada com sucesso!"}
                conn.commit()
                return {"results": results}
    except Exception as e:
        logger.error(f"Erro ao executar a query {e}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/auth")
def authenticate_user(request: AuthRequest):
    """
    Autentica um usuário com base nas credenciais fornecidas.

    Args:
        request (AuthRequest): Objeto contendo o nome e a senha do usuário.

    Returns:
        dict: Um dicionário contendo o token de autenticação se as credenciais forem válidas.

    Raises:
        HTTPException: Se o nome ou a senha estiverem incorretos, retorna uma exceção HTTP 401.
        HTTPException: Se ocorrer um erro interno do servidor, retorna uma exceção HTTP 500.
    """
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT senha FROM usuarios WHERE nome = %s", (request.nome,))
                user = cursor.fetchone()
                if user and hashlib.sha256(request.senha.encode()).hexdigest() == user["senha"]:
                    return {"token": "authToken"}
                else:
                    raise HTTPException(status_code=401, detail="Nome ou senha incorretos")
    except Exception as e:
        logger.error(f"Erro ao autenticar o usuário {e}")
        raise HTTPException(status_code=500, detail="Erro interno do servidor")