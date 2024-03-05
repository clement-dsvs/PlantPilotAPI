from datetime import datetime

from pydantic import BaseModel

from . import User


class Topic(BaseModel):
    created_by: User = None
    created_at: datetime = None
    title: str = "Topic Title"
    description: str = ""


class Message(BaseModel):
    topic: Topic = None
    created_by: User = None
    created_at: datetime = None
    message: str = ""
    response_to = None
    modified_at: datetime = None
    previous_message = None
