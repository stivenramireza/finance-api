from datetime import datetime

from sqlalchemy import Column, Integer, Boolean, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from src.config.postgres_db import Base
from src.models.transaction_model import Transaction


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    active = Column(Boolean, default=True)
    uid = Column(String)
    username = Column(String)
    password = Column(String)
    contact_id = Column(Integer, ForeignKey('contacts.id'))
    created_at = Column(Date, default=datetime.utcnow())
    updated_at = Column(Date, default=datetime.utcnow())

    contact = relationship('Contact', back_populates='users')
    source_transactions = relationship(
        'Transaction',
        foreign_keys=[Transaction.source_user_id],
        back_populates='source_user',
    )
    destination_transactions = relationship(
        'Transaction',
        foreign_keys=[Transaction.destination_user_id],
        back_populates='destination_user',
    )
