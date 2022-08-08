from datetime import datetime

from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from src.config.postgres_db import Base


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    concept = Column(String)
    amount = Column(Float)
    source_user_id = Column(Integer, ForeignKey('users.id'))
    destination_user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(Date, default=datetime.utcnow())
    updated_at = Column(Date, default=datetime.utcnow())

    source_user = relationship(
        'User',
        foreign_keys=[source_user_id],
        back_populates='source_transactions',
    )
    destination_user = relationship(
        'User',
        foreign_keys=[destination_user_id],
        back_populates='destination_transactions',
    )
