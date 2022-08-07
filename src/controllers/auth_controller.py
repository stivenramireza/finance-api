from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from src.config.database import Base, SessionLocal, engine
from src.schemas.auth_schema import Credential
from src.services import user_service

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix='/auth', tags=['Auth'])

# Dependency
def get_db() -> SessionLocal:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    path='/',
    status_code=status.HTTP_200_OK,
    summary='User login',
)
def login(
    credential: Credential, db: Session = Depends(get_db)
) -> dict[str, any]:
    return {'success': user_service.create_user(db, None)}
