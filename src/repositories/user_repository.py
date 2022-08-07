from uuid import uuid4

from sqlalchemy.orm import Session

from src.models.user_model import User


def create_user(db: Session, contact_id: int, password: str) -> bool:
    created_user = User(
        id=str(uuid4()), contact_id=contact_id, password=password
    )
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    return True
