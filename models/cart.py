#!/usr/bin/python3
""" the carts module """
from models import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Cart(BaseModel, Base):
    """ A Cart class """
    __tablename__ = carts

    user_id = Column(
            String(60),
            ForeignKey('users.id', ondelete='CASCADE'),
            nullable=False
            )

    cart_items = relationship(
            'CartItem',
            backref='cart',
            cascade='all, delete, delete-orphan'
            )
