from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    created_at: datetime = Field(default=datetime.utcnow())
    updated_at: datetime = Field(default=datetime.utcnow())


class UserCreate(BaseModel):
    password: str = Field(min_length=8, example='stivenramireza')


class User(UserBase):
    id: UUID
    contact_id: int

    class Config:
        orm_mode = True
