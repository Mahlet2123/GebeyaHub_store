#!/usr/bin/python3
""" the cart_item module """
from models import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class CartItem(BaseModel, Base):
    """ A CartItem class """
    __tablename__ = cart_items

    quantity = Column(Integer, nullable=False)
    cart_id = Column(
            String(60),
            ForeignKey('carts.id', ondelete='CASCADE'),
            nullable=False
            )
    product_id = Column(
            String(60),
            ForeignKey('products.id', ondelete='CASCADE'),
            nullable=False
            )
