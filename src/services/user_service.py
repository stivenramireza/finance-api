from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.schemas.contact_schema import ContactCreate
from src.repositories import user_repository
from src.services import contact_service
from src.middlewares import password_middleware


def create_user(db: Session, contact: ContactCreate) -> bool:
    created_contact = contact_service.create_contact(db, contact)
    if not created_contact:
        raise HTTPException(
            status_code=409, detail='Contact could not be registered'
        )

    hashed_password = password_middleware.get_password_hash(
        contact.credential.password
    )
    return user_repository.create_user(db, created_contact.id, hashed_password)
