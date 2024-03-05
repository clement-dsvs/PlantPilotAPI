from fastapi import APIRouter, HTTPException, Request
from src.db import database
import datetime

router = APIRouter()


@router.get("/")
async def get_all():
    collection = database["C_FORUM_TOPICS"]
    result = []
    async for item in collection.find({}, {'_id': 0}):
        result.append(item)
    collection = database["C_FORUM_MESSAGES"]
    async for item in collection.find({}, {'_id': 0}):
        result.append(item)
    return {"objects": result}


@router.post("/")
async def create_topic(request: Request):
    form = await request.form()
    form = dict(form.items())
    form["created_at"] = datetime.datetime.now()
    form["last_message_by"] = None
    form["last_message_at"] = datetime.datetime.now()
    form["total_messages"] = 0
    collection = database["C_FORUM_TOPICS"]
    topic = await collection.insert_one(form)
    result = await collection.find_one(form, {'_id': 0})
    if result is not None:
        return result.items()
    else:
        return {"error": "Forum topic already exist"}