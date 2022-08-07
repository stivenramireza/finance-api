from pydantic import BaseModel, Field, EmailStr

from src.schemas.user_schema import User, UserCreate


class ContactBase(BaseModel):
    name: str = Field(
        min_length=10, max_length=100, example='Stiven Ramírez Arango'
    )
    document_type: str = Field(example='CC')
    document: str = Field(min_length=5, max_length=20, example='10401254578')
    email: EmailStr = Field(example='stivenramireza@gmail.com')


class ContactCreate(ContactBase):
    credential: UserCreate = Field()


class Contact(ContactBase):
    id: int
    users: list[User] = []

    class Config:
        orm_mode = True
