from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import get_db_connection
from fastapi.middleware.cors import CORSMiddleware
import logging

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

@app.post("/query")
def execute_query(request: QueryRequest):
    """
    Execute an SQL query based on the provided QueryRequest object.

    Args:
        request (QueryRequest): Object containing the SQL query to be executed.

    Returns:
        dict: A dictionary containing the query results or a success message.

    Raises:
        HTTPException: Exception raised in case of query execution error, with status code 400 and error details.
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
