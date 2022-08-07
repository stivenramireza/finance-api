from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.schemas.contact_schema import ContactCreate, Contact
from src.repositories import contact_repository


def get_contact_by_id(db: Session, contact_id: str) -> Contact:
    return contact_repository.get_contact_by_id(db, contact_id)


def get_contact_by_email(db: Session, email: str) -> Contact:
    return contact_repository.get_contact_by_email(db, email)


def create_contact(db: Session, contact: ContactCreate) -> Contact:
    found_contact = contact_repository.get_contact_by_document(
        db, contact.document
    )
    if found_contact:
        raise HTTPException(
            status_code=400, detail='Contact already registered'
        )
    return contact_repository.create_contact(db, contact)
