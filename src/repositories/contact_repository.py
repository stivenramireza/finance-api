from sqlalchemy.orm import Session

from src.schemas.contact_schema import ContactCreate
from src.models.contact_model import Contact


def get_contact_by_document(db: Session, document: str) -> int:
    return db.query(Contact).filter(Contact.document == document).first()


def create_contact(db: Session, contact: ContactCreate) -> Contact:
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
