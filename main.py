from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Private Doc QnA Assistant")
app.include_router(router)