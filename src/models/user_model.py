from uuid import UUID

from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    name: str = Field(
        ..., min_length=1, max_length=50, example='Stiven Ramírez Arango'
    )
    email: EmailStr = Field(..., example='stivenramireza@gmail.com')


class UserPassword(BaseModel):
    password: str = Field(..., min_length=8, example='stivenramireza')


class UserLogin(User, UserPassword):
    pass


class UserRegister(User, UserPassword):
    def __str__(self) -> str:
        return self.dict()
