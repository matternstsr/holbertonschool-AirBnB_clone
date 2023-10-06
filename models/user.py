#!/usr/bin/python3
"""Defines a Class User, that Inherits from Base_model"""
from base_model.py import BaseModel


class User(BaseModel):
    """Defines a class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
