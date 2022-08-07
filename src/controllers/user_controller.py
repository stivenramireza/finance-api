from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from src.config.database import Base, SessionLocal, engine
from src.schemas.contact_schema import ContactCreate
from src.services import user_service

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix='/users', tags=['Users'])

# Dependency
def get_db() -> SessionLocal:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    path='/',
    status_code=status.HTTP_201_CREATED,
    summary='Register a user',
)
def create_user(
    user: ContactCreate, db: Session = Depends(get_db)
) -> dict[str, any]:
    return {'success': user_service.create_user(db, user)}
