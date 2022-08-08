from pydantic import BaseModel, Field, EmailStr

from src.schemas.transaction_schema import TransactionSchema


class UserBaseSchema(BaseModel):
    name: str = Field(
        min_length=10,
        max_length=100,
        example='Stiven Ramírez Arango',
    )
    document_type: str = Field(example='CC')
    document: str = Field(min_length=5, max_length=20, example='10401254578')
    email: EmailStr = Field(example='stivenramireza@gmail.com')


class UserCreateSchema(UserBaseSchema):
    username: str = Field(
        min_length=10,
        max_length=50,
        example='stivenramireza',
    )
    password: str = Field(min_length=8, example='stivenramireza')


class UserSchema(UserBaseSchema):
    id: int
    active: bool
    contact_id: int
    source_transactions: list[TransactionSchema] = []

    class Config:
        orm_mode = True
