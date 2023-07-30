#!/usr/bin/python3
""" the order_item module """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class OrderItem(BaseModel, Base):
    """ A OrderItem class """
    __tablename__ = 'order_items'

    quantity = Column(Integer, nullable=False)
    order_id = Column(
            String(60),
            ForeignKey('orders.id', ondelete='CASCADE'),
            nullable=False
            )
    product_id = Column(
            String(60),
            ForeignKey('products.id', ondelete='CASCADE'),
            nullable=False
            )
