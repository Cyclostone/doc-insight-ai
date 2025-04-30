from pydantic import BaseModel

class UploadResponse(BaseModel):
    filename: str
    chunks: int

class QueryRequest(BaseModel):
    query: str 

class QueryResponse(BaseModel):
    answer: str