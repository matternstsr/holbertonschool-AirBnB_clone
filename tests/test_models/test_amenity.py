#!/usr/bin/python3
"""Test Amenity"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
import os

"""from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State"""


class Testamenity(unittest.TestCase):
    """unit test for amenity class"""

    def test_class(self):
        """Tests if correct class"""
        amenity1 = Amenity()
        self.assertEqual(amenity1.__class__.__name__, "Amenity")

    def test_inheritance(self):
        """ Tests if class inherits from BaseModel."""
        amenity1 = Amenity()
        self.assertTrue(issubclass(amenity1.__class__, BaseModel))

    def tearDown(self):
        """ destroys created file """
        storage._FileStorage__file_path = "file.json"
        try:
            os.remove("test.json")
        except FileNotFoundError:
            pass

    def setUp(self):
        """Return to "" class attributes"""
        with open("test.json", 'w'):
            storage._FileStorage__file_path = "test.json"
            storage._FileStorage__objects = {}
        Amenity.name = ""

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 0)

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_Amenity = Amenity()
        self.assertTrue(isinstance(my_Amenity, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        my_Amenity = Amenity()
        self.assertTrue(type(my_Amenity.name) == str)
