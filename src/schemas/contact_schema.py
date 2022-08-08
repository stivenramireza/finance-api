from pydantic import BaseModel


class ContactBaseSchema(BaseModel):
    name: str
    document_type: str
    document: str
    email: str


class ContactSchema(ContactBaseSchema):
    class Config:
        orm_mode = True
