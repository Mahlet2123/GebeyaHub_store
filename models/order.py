#!/usr/bin/python3
""" the orders module """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Order(BaseModel, Base):
    """ A Order class """
    __tablename__ = 'orders'

    user_id = Column(
            String(60),
            ForeignKey('users.id', ondelete='CASCADE'),
            nullable=False
            )

    order_items = relationship(
            'OrderItem',
            backref='order',
            cascade='all, delete, delete-orphan'
            )
