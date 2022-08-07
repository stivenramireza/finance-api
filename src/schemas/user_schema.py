from pydantic import BaseModel, Field, EmailStr


class UserBase(BaseModel):
    name: str = Field(
        min_length=10, max_length=100, example='Stiven Ramírez Arango'
    )
    document_type: str = Field(example='CC')
    document: str = Field(min_length=5, max_length=20, example='10401254578')
    email: EmailStr = Field(example='stivenramireza@gmail.com')


class UserCreate(UserBase):
    username: str = Field(
        min_length=10, max_length=50, example='stivenramireza'
    )
    password: str = Field(min_length=8, example='stivenramireza')


class User(UserBase):
    pass
