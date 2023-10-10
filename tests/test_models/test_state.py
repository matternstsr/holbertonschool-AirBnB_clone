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

    def setUp(self):
        """Return to "" class attributes"""
        State.name = ""

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(state.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(State.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(State):
            self.assertTrue(len(func.__doc__) > 0)

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_state = State()
        self.assertTrue(isinstance(my_state, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        my_state = State()
        self.assertTrue(type(my_state.name) == str)
