from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.schemas.contact_schema import ContactCreate, User
from src.repositories import contact_repository


def create_contact(db: Session, contact: ContactCreate) -> User:
    found_contact = contact_repository.get_contact_by_document(
        db, contact.document
    )
    if found_contact:
        raise HTTPException(
            status_code=400, detail='Contact already registered'
        )
    return contact_repository.create_contact(db, contact)
