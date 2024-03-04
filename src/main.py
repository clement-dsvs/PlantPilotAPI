from fastapi import FastAPI
from src.db import client

from src.routes import presets_router

app = FastAPI()


@app.on_event("startup")
async def startup_db_client():
    await client.start_session()


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()


@app.get("/")
def hello_world():
    return {"Hello": "World"}


app.include_router(presets_router, prefix="/presets")
