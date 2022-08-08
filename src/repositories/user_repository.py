from uuid import uuid4

from sqlalchemy.orm import Session

from src.models.user_model import User


def get_user_by_id(db: Session, user_id: str) -> User:
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_uid(db: Session, uid: str) -> User:
    return db.query(User).filter(User.uid == uid).first()


def get_user_by_username(db: Session, username: str) -> User:
    return db.query(User).filter(User.username == username).first()


def get_user_by_contact_id(db: Session, contact_id: str) -> User:
    return db.query(User).filter(User.contact_id == contact_id).first()


def create_user(
    db: Session, username: str, password: str, contact_id: int
) -> User:
    created_user = User(
        uid=str(uuid4()),
        username=username,
        password=password,
        contact_id=contact_id,
    )
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    return created_user
