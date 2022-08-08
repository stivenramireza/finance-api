from fastapi import HTTPException

from src.schemas.user_schema import UserSchema
from src.schemas.transaction_schema import TransactionSchema


def get_transactions_by_user(user: UserSchema) -> list[TransactionSchema]:
    transactions = user.source_transactions
    if not transactions:
        raise HTTPException(status_code=404, detail='Transactions not found')

    return transactions
