from fastapi import FastAPI
from app.api.scrapper.scrapper import router as scrapper_router

app = FastAPI()

app.include_router(scrapper_router)
