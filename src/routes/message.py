from fastapi import APIRouter
from src.db import database

router = APIRouter()


@router.post("/")
async def create_messages():
    collection = database["C_FORUM_MESSAGES"]
