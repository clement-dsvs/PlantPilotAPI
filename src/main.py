from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.db import client

from src.routes import presets_router, user_router, message_router, topic_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

@app.on_event("startup")
async def startup_db_client():
    await client.start_session()


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()


@app.get("/")
def hello_world():
    return {"Hello": "World"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(presets_router, prefix="/preset")
app.include_router(user_router, prefix="/user")
app.include_router(message_router, prefix="/message")
app.include_router(topic_router, prefix="/topic")
