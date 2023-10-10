#!/usr/bin/python3
"""Test Place"""
import unittest
from models.base_model import BaseModel
from models.place import Place
"""from models.review import Review
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity"""


class Testplace(unittest.TestCase):
    """Unittests for the class Place"""

    def test_class(self):
        """Tests if correct class"""
        place1 = Place()
        self.assertEqual(place1.__class__.__name__, "Place")

    def inheritance(self):
        """Tests if class inherits from BaseModel"""
        place1 = Place()
        self.assertTrue(issubclass(place1.__class__, BaseModel))
