from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.utils.secrets import secrets

db_secrets = secrets.get('DB')

SQLALCHEMY_DATABASE_URL = (
    'postgresql://{user}:{password}@{host}:{port}/{schema}'.format(
        user=db_secrets.get('user'),
        password=db_secrets.get('password'),
        host=db_secrets.get('host'),
        port=db_secrets.get('port'),
        schema=db_secrets.get('schema'),
    )
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)

# Dependency
def db_session() -> SessionLocal:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
