#!/usr/bin/python3
"""Defines a Class User, that Inherits from Base_model"""
from base_model.py import Basemodel


class User(Basemodel):
    """Defines a class User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
