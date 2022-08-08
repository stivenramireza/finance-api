from fastapi import APIRouter, Depends, Body, status
from sqlalchemy.orm import Session
from redis import Redis

from src.config.postgres_db import db_session
from src.config.redis_db import redis_conn
from src.schemas.auth_schema import LoginSchema, AccessTokenSchema
from src.services import auth_service
from src.middlewares.jwt_middleware import JWTBearer


router = APIRouter(prefix='/auth', tags=['auth-service'])


@router.post(
    path='/login', status_code=status.HTTP_200_OK, summary='User login'
)
def login(
    login: LoginSchema = Body(), db: Session = Depends(db_session)
) -> AccessTokenSchema:
    return auth_service.authenticate_user(db, login)


@router.post(
    path='/logout', status_code=status.HTTP_200_OK, summary='User logout'
)
def logout(
    jwt_auth: JWTBearer = Depends(JWTBearer()),
) -> dict[str, any]:
    success_logout = auth_service.logout(redis_conn, jwt_auth.get('token'))
    return {'success': success_logout}
