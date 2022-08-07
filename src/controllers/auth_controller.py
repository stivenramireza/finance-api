from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from src.config.database import db_session
from src.schemas.auth_schema import Login
from src.services import user_service


router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post(
    path='/',
    status_code=status.HTTP_200_OK,
    summary='User login',
)
def login(login: Login, db: Session = Depends(db_session)) -> dict[str, any]:
    return {'success': user_service.create_user(db, None)}
