from uuid import uuid4

from sqlalchemy.orm import Session

from src.models.user_model import User


def get_user_by_id(db: Session, user_id: str) -> User:
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_contact_id(db: Session, contact_id: str) -> User:
    return db.query(User).filter(User.contact_id == contact_id).first()


def create_user(db: Session, contact_id: int, password: str) -> bool:
    created_user = User(
        id=str(uuid4()), contact_id=contact_id, password=password
    )
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    return True
