from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from src.config.postgres_db import db_session
from src.schemas.transaction_schema import TransactionSchema
from src.services import user_service, transaction_service
from src.middlewares.jwt_middleware import JWTBearer


router = APIRouter(prefix='/transactions', tags=['transaction-service'])


@router.get(
    path='',
    status_code=status.HTTP_200_OK,
    response_model=list[TransactionSchema],
    summary='Get user transactions',
)
def get_user_transactions(
    db: Session = Depends(db_session),
    jwt_auth: JWTBearer = Depends(JWTBearer()),
) -> list[TransactionSchema]:
    user = user_service.get_current_user(db, jwt_auth.get('sub'))
    return transaction_service.get_transactions_by_user(user)
