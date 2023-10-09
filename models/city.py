#!/usr/bin/python3
"""Defines a new class, City, that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Defines a new class, City"""

    state_id = ""
    name = ""
