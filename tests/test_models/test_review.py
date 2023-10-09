#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.review import Review
"""from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place"""


class Testreview(unittest.TestCase):
    """Unittests for the Review Class"""

    def test_class(self):
        """Tests for the Review Class"""
        rev1 = Review()
        self.assertEqual(rev1.__class__.__name__, "Review")

    def test_inheritance(self):
        """Tests if class inherits from BaseModel"""
        rev1 = Review()
        self.assertTrue(issubclass(rev1.__class__, BaseModel))
