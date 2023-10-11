#!/usr/bin/python3
"""Test State"""
import unittest
from models.state import State
from models.base_model import BaseModel


class Teststate(unittest.TestCase):
    """Unittests for the State Class"""

    def test_class(self):
        """Tests for the correct class"""
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def test_inheritance(self):
        """Tests if the class inherits from BaseModel"""
        state1 = State()
        self.assertEqual(state1.__class__.__name__, "State")

    def setUp(self):
        """Return the 'name' class attribute to its default value"""
        State.name = ""

    def test_module_doc(self):
        """Check for module documentation"""
        self.assertTrue(len(State.__doc__) > 0)

    def test_class_doc(self):
        """Check for class documentation"""
        self.assertTrue(len(State.__doc__) > 0)

    def test_method_docs(self):
        """Check for method documentation"""
        for func in dir(State):
            self.assertTrue(len(func.__doc__) > 0)

    def test_is_instance(self):
        """Test if a state is an instance of BaseModel"""
        my_state = State()
        self.assertTrue(isinstance(my_state, BaseModel))

    def test_field_types(self):
        """Test field attributes of the state"""
        my_state = State()
        self.assertTrue(type(my_state.name) is str)


if __name__ == '__main__':
    unittest.main()
