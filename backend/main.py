from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_db_connection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # URL do seu frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
def execute_query(request: QueryRequest):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(request.query)
        if cursor.description:  # Verifica se a consulta retorna algo (ex: SELECT)
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
