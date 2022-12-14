from sqlalchemy.orm import Session

from src.schemas.user_schema import UserCreateSchema
from src.models.contact_model import Contact


def get_contact_by_id(db: Session, contact_id: str) -> Contact:
    return db.query(Contact).filter(Contact.id == contact_id).first()


def get_contact_by_document(db: Session, document: str) -> Contact:
    return db.query(Contact).filter(Contact.document == document).first()


def get_contact_by_email(db: Session, email: str) -> Contact:
    return db.query(Contact).filter(Contact.email == email).first()


def create_contact(db: Session, contact: UserCreateSchema) -> Contact:
    created_contact = Contact(
        name=contact.name,
        document_type=contact.document_type,
        document=contact.document,
        email=contact.email,
    )
    db.add(created_contact)
    db.commit()
    db.refresh(created_contact)
    return created_contact
