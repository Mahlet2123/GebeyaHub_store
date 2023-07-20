#!/usr/bin/python3
""" the categories module """
from models import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship


class Category(BaseModel, Base):
    """ A category class """
    __tablename__ = categories

    name = Column(String(60), nullable=False)
    discription =Column(String(1024), nullable=True)

    products = relationship(
            'Product',
            backref='category',
            cascade = "all, delete, delete-orphan"
            )
