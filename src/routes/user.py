from fastapi import APIRouter, HTTPException

from src.models import User
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


@router.post("/create/{username}/{password}/{email}")
async def create_account(username: str, password: str, email: str):
    collection = database["C_USERS"]
    result = []
    errors = []
    async for item in collection.find({"$or": [{"username": {"$eq": username}}, {"email": {"$eq": email}}]}):
        result.append(item)
        if item["username"] == username and "Username" not in errors:
            errors.append("Username")
        if item["email"] == email and "Email" not in errors:
            errors.append("Email")
    print(result)
    if len(errors) >= 1:
        return HTTPException(status_code=409, detail={"Already exists": errors})
    else:
        collection.insert_one({"username": username, "password": password, "email": email,
                               "is_active": True, "isAdmin": False})
        return {"Ok": "Account created"}
