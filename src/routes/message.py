from fastapi import APIRouter
from src.db import database
from src.models import Message

router = APIRouter()


@router.post("/")
async def create_messages(message: Message):
    collection = database["C_FORUM_MESSAGES"]
    result = await collection.insert_one(message.dict())
    return result.inserted_id


@router.get("/")
async def get_messages():
    collection = database["C_FORUM_MESSAGES"]
    result = []
    async for item in collection.find({}, {'_id': 0}):
        result.append(item)
    return result
