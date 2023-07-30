#!/usr/bin/python3
""" the product_images module """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class ProductImage(BaseModel, Base):
    """ A ProductImage class """
    __tablename__ = 'product_images'

    _type = Column(String(60), nullable=True)
    image_urls = Column(String(128), nullable=False)
    product_id = Column(
            String(60),
            ForeignKey('products.id', ondelete='CASCADE'),
            nullable=False
            )
