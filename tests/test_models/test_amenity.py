#!/usr/bin/python3
"""Test Amenity"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
"""from models.city import City
from models.place import Place
from models.review import Review
from models.state import State"""


class Testamenity(unittest.TestCase):
     """unit test for amenity class"""

     def test_class(self):
         """Tests if correct class"""
         amenity1 = Amenity()
         self.assertEqual(amenity1.__class__name__, "Amenity")

    def test_inheritance(self):
        """ Tests if class inherits from BaseModel."""
        amenity1 = Amenity()
        self.assertTrue(issubclass(amenity1.__class__, BaseModel))
