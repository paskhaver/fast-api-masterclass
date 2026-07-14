from contextlib import asynccontextmanager

from database import create_db_and_tables
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "Auth demo is running"}
