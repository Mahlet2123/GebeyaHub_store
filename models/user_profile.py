#!/usr/bin/python3
""" the user_profile module """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey


class UserProfile(BaseModel, Base):
    """ A userProfile class """
    __tablename__ = 'user_profile'

    profile_picture = Column(String(128), nullable=True)
    bio = Column(String(128), nullable=True)
    user_id = Column(
            String(60),
            ForeignKey('users.id', ondelete='CASCADE'),
            nullable=False
            )
