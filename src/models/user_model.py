from datetime import datetime

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from src.config.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    contact_id = Column(Integer, ForeignKey('contacts.id'))
    password = Column(String)
    created_at = Column(Date, default=datetime.utcnow())
    updated_at = Column(Date, default=datetime.utcnow())

    contact = relationship('Contact', back_populates='users')
