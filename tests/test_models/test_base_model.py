#!/usr/bin/python3
"""BaseModel Air BnB unittests"""
import unittest
from models.base_model import BaseModel
import datetime
import time


class TestBaseModel(unittest.TestCase):
    """class TestBaseModel"""

    def setUp(self):
        """Set up a BaseModel instance for testing with custom values"""
        self.base = BaseModel()
        self.base.custom_attribute = 42

    def test_instance_and_attributes(self):
        """Test that BaseModel has the correct attributes"""
        self.assertIsInstance(self.base, BaseModel)
        self.assertIsNotNone(self.base.id)
        self.assertIsNotNone(self.base.created_at)
        self.assertIsNotNone(self.base.updated_at)

        self.assertEqual(self.base.custom_attribute, 42)

    def test_attribute_types(self):
        """Test that BaseModel attributes have the correct types"""
        self.assertIsInstance(self.base.id, str)
        self.assertEqual(len(self.base.id), 36)
        self.assertIsInstance(self.base.created_at, datetime.datetime)
        self.assertIsInstance(self.base.updated_at, datetime.datetime)

    def test_updated_at_same_as_created_at(self):
        """Test that BaseModel updated_at is
        the same as created_at initially"""
        self.assertEqual(self.base.updated_at, self.base.created_at)

    def test_str_representation(self):
        """Test the __str__ method of BaseModel"""
        base_str = str(self.base)
        self.assertIsInstance(base_str, str)
        self.assertTrue(base_str.startswith('[BaseModel]'))

    def test_save_method(self):
        """Test the save method of BaseModel"""
        initial_updated_at = self.base.updated_at
        time.sleep(0.0001)
        self.base.save()
        self.assertNotEqual(self.base.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method of BaseModel"""
        base_dict = self.base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertIn('__class__', base_dict)
        self.assertIn('created_at', base_dict)
        self.assertIn('updated_at', base_dict)
        self.assertIn('id', base_dict)


if __name__ == '__main__':
    unittest.main()
