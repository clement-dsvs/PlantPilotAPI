from pydantic import BaseModel
from .User import User


class Preset(BaseModel):
    uuid: str
    name: str
    created_by: User
