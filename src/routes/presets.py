from fastapi import APIRouter, HTTPException

from src.models import Preset
from src.db import database

router = APIRouter()


@router.get("/")
async def get_all_presets():
    collection = ["presets"]
    return {"presets": collection}


@router.post("/")
async def create_preset(preset: Preset):
    collection = database["presets"]
    result = await collection.insert_one(preset.dict())
    return {"message": "Item inséré avec succès", "inserted_id": str(result.inserted_id)}


@router.get("/{preset_uuid}")
async def get_preset(preset_uuid: str):
    collection = database["presets"]
    result = await collection.find_one({"uuid": preset_uuid})
    if result:
        return Preset(**result)
    else:
        raise HTTPException(status_code=404, detail="preset not found")
