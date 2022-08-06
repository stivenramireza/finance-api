from uuid import uuid4

from src.models.user_model import UserRegister, User

from src.repositories import user_repository


def register_user(user: UserRegister) -> User:
    user = user.dict()
    user_id = str(uuid4())
    user.update({'id': user_id})

    return user_repository.register_user(user)
