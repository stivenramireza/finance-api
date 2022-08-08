from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.utils.secrets import secrets

postgres_secrets = secrets.get('POSTGRES')

SQLALCHEMY_DATABASE_URL = (
    'postgresql://{user}:{password}@{host}:{port}/{schema}'.format(
        user=postgres_secrets.get('user'),
        password=postgres_secrets.get('password'),
        host=postgres_secrets.get('host'),
        port=postgres_secrets.get('port'),
        schema=postgres_secrets.get('schema'),
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
