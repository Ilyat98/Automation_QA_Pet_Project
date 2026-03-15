from pydantic import BaseModel
from typing import List


class User(BaseModel):

    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class UsersResponse(BaseModel):

    page: int
    per_page: int
    total: int
    data: List[User]