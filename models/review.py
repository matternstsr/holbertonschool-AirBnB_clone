#!/usr/bin/python3
"""Defines a new class, Review, that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class 'Review' inherits from Class 'BaseModel' """
    place_id = ""
    user_id = ""
    text = ""
