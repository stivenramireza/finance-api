from pydantic import BaseModel, Field, EmailStr


class Credential(BaseModel):
    email: EmailStr = Field(example='stivenramireza@gmail.com')
    password: str = Field(min_length=8, example='stivenramireza')
