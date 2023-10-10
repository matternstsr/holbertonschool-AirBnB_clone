#!/usr/bin/python3
"""Test City"""
import unittest
from models.base_model import BaseModel
from models.city import City
"""from models.place import Place
from models.user import User
from models.review import Review
from models.state import State
from models.amenity import Amenity"""


class Testcity(unittest.TestCase):
    """Unittests for the City class."""

    def test_class(self):
        """Tests if correct class."""
        city1 = City()
        self.assertEqual(city1.__class__.__name__, "City")

    def test_inheritance(self):
        """Tests if Class inherits from BaseModel."""
        city1 = City()
        self.assertTrue(issubclass(city1.__class__, BaseModel))
    def setUp(self):
        """Return to "" class attributes"""
        City.name = ""
        City.state_id = ""

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(city.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(City.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_city = City()
        self.assertTrue(isinstance(my_city, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        my_city = City()
        self.assertTrue(type(my_city.name) == str)
        self.assertTrue(type(my_city.state_id) == str)
