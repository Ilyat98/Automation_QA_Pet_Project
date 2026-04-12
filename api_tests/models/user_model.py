from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str


class CreateUserResponse(BaseModel):
    name: str
    job: str
    id: int


class UpdateUserResponse(BaseModel):
    name: str
    job: str