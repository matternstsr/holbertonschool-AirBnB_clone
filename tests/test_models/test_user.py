#!/usr/bin/python3
"""Test User"""
import unittest
from models.user import User
from models.base_model import BaseModel
"""from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel"""


class Testuser(unittest.TestCase):
    """unittests for the user class."""

    def test_class(self):
        """Tests for correct class."""
        user1= User()
        self.assertEqual(user1.__class__.__name__, "User")

    def test_inheritance(self):
        """Tests if class inherits from BaseModel"""
        user1 = User()
        self.assertEqual(user1.__class_.__name__, "User")
