from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.schemas.user_schema import UserSchema, UserCreateSchema
from src.schemas.contact_schema import ContactSchema
from src.repositories import user_repository
from src.services import contact_service
from src.middlewares.password_middleware import Password


def get_user_by_id(db: Session, user_id: str) -> UserSchema:
    user = user_repository.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found'
        )

    contact = contact_service.get_contact_by_id(db, user.contact_id)
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Contact not found'
        )

    return contact


def get_user_by_username(db: Session, username: str) -> UserSchema:
    user = user_repository.get_user_by_username(db, username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found'
        )

    return user


def get_user_by_contact_id(db: Session, contact_id: str) -> UserSchema:
    user = user_repository.get_user_by_contact_id(db, contact_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found'
        )

    return user


def create_user(db: Session, user: UserCreateSchema) -> ContactSchema:
    created_contact = contact_service.create_contact(db, user)
    if not created_contact:
        raise HTTPException(
            status_code=409, detail='Contact could not be registered'
        )

    hashed_password = Password.get_hashed_password(user.password)
    created_user = user_repository.create_user(
        db, user.username, hashed_password, created_contact.id
    )
    if not created_user:
        raise HTTPException(
            status_code=409, detail='User could not be registered'
        )

    return created_contact


def get_current_user(db: Session, uid: str) -> UserSchema:
    user = user_repository.get_user_by_uid(db, uid)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    return user
