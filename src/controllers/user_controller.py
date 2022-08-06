from fastapi import APIRouter
from fastapi import status

from src.models.user_model import UserRegister
from src.services import user_service

router = APIRouter(prefix='/users', tags=['Users'])


@router.post(
    path='/',
    status_code=status.HTTP_201_CREATED,
    summary='Register a user',
)
def post_user(user: UserRegister) -> dict[str, any]:
    return user_service.register_user(user)
