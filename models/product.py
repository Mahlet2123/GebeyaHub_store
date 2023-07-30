#!/usr/bin/python3
""" the products module """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Float
from sqlalchemy.orm import relationship


class Product(BaseModel, Base):
    """ A product class """
    __tablename__ = 'products'

    name = Column(String(60), nullable=False)
    price = Column(Float, nullable=False)
    description =Column(String(1024))
    category_id = Column(
            String(60),
            ForeignKey("categories.id", ondelete="CASCADE"),
            nullable=False
            )

    product_images = relationship(
            'ProductImage',
            backref='product',
            cascade='all, delete, delete-orphan'
            )

    cart_items = relationship(
            'CartItem',
            backref='product',
            cascade='all, delete, delete-orphan'
            )

    order_items = relationship(
            'OrderItem',
            backref='product',
            cascade='all, delete, delete-orphan'
            )

    reviews = relationship(
            'Review',
            backref='product',
            cascade='all, delete, delete-orphan'
            )
