from pydantic import BaseModel, EmailStr


class ContactBase(BaseModel):
    name: str
    document_type: str
    document: str
    email: EmailStr


class ContactCreate(ContactBase):
    pass


class Contact(ContactBase):
    pass
