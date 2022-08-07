from pydantic import BaseModel, Field


class Login(BaseModel):
    username: str = Field(example='stivenramireza@gmail.com')
    password: str = Field(min_length=8, example='stivenramireza')
