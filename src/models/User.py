from pydantic import BaseModel, EmailStr

SECRET = "75eff79f3492967902d7f8a77a105160cd739d3b8f78fcc8d6cead5ab2ae7911"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class User(BaseModel):
    username: str
    full_name: str
    email: EmailStr
    hashed_password: str
    disabled: bool
