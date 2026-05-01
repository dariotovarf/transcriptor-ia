from fastapi import FastAPI
from app.routes.transcription import router

app = FastAPI()

app.include_router(router)