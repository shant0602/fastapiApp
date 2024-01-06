from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True


class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
