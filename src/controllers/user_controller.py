from fastapi import APIRouter, Depends, status

from sqlalchemy.orm import Session

from src.config.database import Base, SessionLocal, engine
from src.schemas.contact_schema import ContactCreate, Contact
from src.services import user_service, auth_service

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


@router.get(path='/', response_model=Contact, summary='Get user')
def get_user(
    db: Session = Depends(get_db),
    uid: Contact = Depends(auth_service.get_current_uid),
) -> Contact:
    return user_service.get_user_by_id(db, uid)
