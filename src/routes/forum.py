from fastapi import APIRouter, HTTPException

from src.models import Forum
from src.db import database

router = APIRouter()


@router.get("/login/{username}/{password}")
async def login(username: str, password: str):
    collection = database["C_USERS"]
    result = await collection.find_one({"username": username, "password": password})
    if result:
        return True
    else:
        HTTPException(status_code=404, detail="No user with these credentials")
