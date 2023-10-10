#!/usr/bin/python3
"""Test State"""
import unittest
from models.state import State
"""from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel"""


class Teststate(unittest.TestCase):
    """Unittests for the State Class"""

    def test_class(self):
        """Tests for correct class"""
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def test_inheritance(self):
        """Tests if class inherits from BaseModel"""
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")
