#!/usr/bin/python3
"""Defines a new class, City, that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Class 'City' inherits from Class 'BaseModel' """
    state_id = ""
    name = ""
