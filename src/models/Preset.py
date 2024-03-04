from pydantic import BaseModel


class Preset(BaseModel):
    uuid: str
    name: str
