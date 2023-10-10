#!/usr/bin/python3
"""Test User"""
import unittest
from models.user import User
from models.base_model import BaseModel
"""from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity"""


class Testuser(unittest.TestCase):
    """unittests for the user class."""

    def test_class(self):
        """Tests for correct class."""
        user1 = User()
        self.assertEqual(user1.__class__.__name__, "User")

    def test_inheritance(self):
        """Tests if class inherits from BaseModel"""
        user1 = User()
        self.assertEqual(user1.__class__.__name__, "User")

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(User.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(User.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_user = User()
        self.assertTrue(isinstance(my_user, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        my_user = User()
        self.assertTrue(type(my_user.email) == str)
        self.assertTrue(type(my_user.password) == str)
        self.assertTrue(type(my_user.first_name) == str)
        self.assertTrue(type(my_user.last_name) == str)
