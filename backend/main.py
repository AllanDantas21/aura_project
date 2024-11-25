from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_db_connection
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def execute_query(request: QueryRequest):
    """
    Executa uma consulta SQL com base no objeto QueryRequest fornecido.

    Args:
        request (QueryRequest): Objeto contendo a consulta SQL a ser executada.

    Returns:
        dict: Um dicionário contendo os resultados da consulta ou uma mensagem de sucesso.

    Raises:
        HTTPException: Exceção levantada em caso de erro na execução da consulta, com status code 400 e detalhe do erro.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(request.query)
        if cursor.description:
            results = cursor.fetchall()
        else:
            results = {"message": "Query executada com sucesso"}
        conn.commit()
        return {"results": results}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        conn.close()
