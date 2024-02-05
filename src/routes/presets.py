from fastapi import APIRouter
from src.models import Preset, User
import uuid

router = APIRouter()


@router.get("/")
def get_all_presets():
    user = User(username='admin', email="admin@eplantcare.com")
    preset = Preset(uuid=uuid.uuid4().__str__(), name="Preset 1", created_by=user)
    return {"presets": [preset]}
