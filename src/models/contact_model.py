from datetime import datetime

from sqlalchemy import Column, Integer, Boolean, String, Date
from sqlalchemy.orm import relationship

from src.config.postgres_db import Base


class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    active = Column(Boolean, default=True)
    name = Column(String)
    document_type = Column(String)
    document = Column(String)
    email = Column(String)
    created_at = Column(Date, default=datetime.utcnow())
    updated_at = Column(Date, default=datetime.utcnow())

    users = relationship('User', back_populates='contact')
