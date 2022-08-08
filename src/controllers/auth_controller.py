from fastapi import APIRouter, Depends, Body, status

from sqlalchemy.orm import Session

from src.config.database import db_session
from src.schemas.auth_schema import LoginSchema, AccessTokenSchema
from src.services import auth_service


router = APIRouter(prefix='/auth', tags=['auth-service'])


@router.post(
    path='/login', status_code=status.HTTP_200_OK, summary='User login'
)
def login(
    login: LoginSchema = Body(), db: Session = Depends(db_session)
) -> AccessTokenSchema:
    return auth_service.authenticate_user(db, login)
