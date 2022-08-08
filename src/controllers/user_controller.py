from fastapi import APIRouter, Depends, Body, status

from sqlalchemy.orm import Session

from src.config.postgres_db import db_session
from src.schemas.user_schema import UserCreateSchema
from src.schemas.contact_schema import ContactSchema
from src.services import user_service
from src.middlewares.jwt_middleware import JWTBearer


router = APIRouter(prefix='/users', tags=['user-service'])


@router.post(
    path='',
    status_code=status.HTTP_201_CREATED,
    response_model=ContactSchema,
    summary='Create a user',
)
def create_user(
    user: UserCreateSchema = Body(), db: Session = Depends(db_session)
) -> ContactSchema:
    return user_service.create_user(db, user)


@router.get(
    path='',
    status_code=status.HTTP_200_OK,
    response_model=ContactSchema,
    summary='Get user',
)
def get_current_user(
    db: Session = Depends(db_session),
    jwt_auth: JWTBearer = Depends(JWTBearer()),
) -> ContactSchema:
    user = user_service.get_current_user(db, jwt_auth.get('sub'))
    return user.contact
