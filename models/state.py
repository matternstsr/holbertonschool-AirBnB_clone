#!/usr/bin/python3
"""Defines a new class, State, that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """ Class 'State' inherits from Class 'BaseModel' """
    name = ""
    
    def __init__(self, *args, **kwargs):
        """ Initialization method """
        super().__init__(*args, **kwargs)