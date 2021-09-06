from pydantic import BaseModel # helps to auto create JSON shcemas from the model
from typing import Optional


class User(BaseModel):
    user_name: str
    age: int


class UpdateUser(BaseModel):
    user_name: Optional[str]
    age: Optional[int]
