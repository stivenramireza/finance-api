from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.schemas.contact_schema import ContactSchema
from src.schemas.user_schema import UserCreateSchema
from src.repositories import contact_repository


def get_contact_by_id(db: Session, contact_id: str) -> ContactSchema:
    return contact_repository.get_contact_by_id(db, contact_id)


def get_contact_by_email(db: Session, email: str) -> ContactSchema:
    return contact_repository.get_contact_by_email(db, email)


def create_contact(db: Session, contact: UserCreateSchema) -> ContactSchema:
    found_contact = contact_repository.get_contact_by_document(
        db, contact.document
    )
    if found_contact:
        raise HTTPException(
            status_code=400, detail='Contact already registered'
        )

    return contact_repository.create_contact(db, contact)
