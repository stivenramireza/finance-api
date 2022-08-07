from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src.services import contact_service, user_service
from src.middlewares import password_middleware, jwt_middleware

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Invalid credentials',
    headers={'WWW-Authenticate': 'Bearer'},
)


def get_current_uid(token: str = Depends(oauth2_scheme)) -> str:
    uid = None

    try:
        payload = jwt_middleware.get_payload(token)
        uid = payload.get('sub')
        if not uid:
            raise credentials_exception
    except Exception:
        raise credentials_exception

    return uid


def authenticate_user(db: Session, email: str, password: str) -> bool:
    contact = contact_service.get_contact_by_email(db, email)
    if not contact:
        return False

    user = user_service.get_user_by_contact_id(db, contact.id)

    is_correct_password = password_middleware.verify_password(
        password, user.password
    )
    if not is_correct_password:
        return False

    return True
