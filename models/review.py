#!/usr/bin/python3
"""Defines a new class, Review, that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines a class, Review"""

    place_id = ""
    user_id = ""
    text = ""
