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

    def setUp(self):
        """Return to "" class attributes"""
        Review.place_id = ""
        Review.user_id = ""
        Review.text = ""

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(review.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Review.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Review):
            self.assertTrue(len(func.__doc__) > 0)

    def test_is_instance(self):
        """ Test if user is instance of basemodel """
        my_Review = Review()
        self.assertTrue(isinstance(my_Review, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        my_Review = Review()
        self.assertTrue(type(my_Review.place_id) == str)
        self.assertTrue(type(my_Review.user_id) == str)
        self.assertTrue(type(my_Review.text) == str)
