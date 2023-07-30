#!/usr/bin/python3
""" the users module """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin


class User(BaseModel, Base, UserMixin):
    """ A user class """
    __tablename__ = 'users'

    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)

    user_profile = relationship(
            'UserProfile',
            backref='user',
            cascade='all, delete, delete-orphan'
            )

    carts = relationship(
            'Cart',
            backref='user',
            cascade='all, delete, delete-orphan'
            )

    orders = relationship(
            'Order',
            backref='user',
            cascade='all, delete, delete-orphan'
            )

    reviews = relationship(
            'Review',
            backref='user',
            cascade='all, delete, delete-orphan'
            )
