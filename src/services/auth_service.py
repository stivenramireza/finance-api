from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from redis import Redis

from src.schemas.auth_schema import LoginSchema, AccessTokenSchema
from src.services import user_service
from src.repositories import token_repository
from src.middlewares.password_middleware import Password
from src.middlewares.jwt_middleware import JWTBearer


def authenticate_user(db: Session, login: LoginSchema) -> AccessTokenSchema:
    user = user_service.get_user_by_username(db, login.username)

    is_correct_password = Password.verify_password(
        login.password, user.password
    )
    if not is_correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Invalid credentials',
        )

    payload = JWTBearer.get_jwt_claims(str(user.uid))
    token = JWTBearer.generate_access_token(payload)
    access_token = AccessTokenSchema(access_token=token)

    return access_token


def logout(client: Redis, token: str) -> bool:
    tokens = token_repository.get_tokens(client)
    if token not in tokens:
        return token_repository.save_token(client, token)

    return False
