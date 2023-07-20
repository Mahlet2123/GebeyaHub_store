#!/usr/bin/python3
""" the review module """
from models import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey


class Review(BaseModel, Base):
    """ A Review class """
    __tablename__ = review

    rating = Column(float, nullable=False)
    review_text =Column(String(1024), nullable=False)
    user_id = Column(
            String(60),
            ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False)
    product_id = Column(
            String(60),
            ForeignKey("products.id", ondelete="CASCADE"),
            nullable=False
            )
