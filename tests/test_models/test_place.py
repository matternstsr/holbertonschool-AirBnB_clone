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

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(Place.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Place.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Place):
            self.assertTrue(len(func.__doc__) > 0)

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_place = Place()
        self.assertTrue(isinstance(my_place, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        self.assertTrue(type(Place.city_id) == str)
        self.assertTrue(type(Place.user_id) == str)
        self.assertTrue(type(Place.name) == str)
        self.assertTrue(type(Place.description) == str)
        self.assertTrue(type(Place.number_rooms) == int)
        self.assertTrue(type(Place.number_bathrooms) == int)
        self.assertTrue(type(Place.max_guest) == int)
        self.assertTrue(type(Place.price_by_night) == int)
        self.assertTrue(type(Place.latitude) == float)
        self.assertTrue(type(Place.longitude) == float)
        self.assertTrue(type(Place.amenity_ids) == list)
