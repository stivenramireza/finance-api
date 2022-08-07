from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from src.config.database import db_session
from src.schemas.user_schema import UserCreate, User
from src.services import user_service, auth_service


router = APIRouter(prefix='/users', tags=['Users'])


@router.post(
    path='/',
    status_code=status.HTTP_201_CREATED,
    response_model=User,
    summary='Create a user',
    tags=['Users'],
)
def create_user(user: UserCreate, db: Session = Depends(db_session)) -> User:
    return user_service.create_user(db, user)


# @router.get(
#     path='/',
#     status_code=status.HTTP_200_OK,
#     response_model=User,
#     summary='Get user',
#     tags=['Users'],
# )
# def get_user(
#     db: Session = Depends(db),
#     uid: Contact = Depends(auth_service.get_current_uid),
# ) -> Contact:
#     return user_service.get_user_by_id(db, uid)
