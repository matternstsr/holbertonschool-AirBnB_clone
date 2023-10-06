#!/usr/bin/python3
"""BaseModel Air BnB unittests"""
import unittest
from models.base_model import BaseModel
import datetime
import time


class TestBaseModel(unittest.TestCase):
    """class TestBaseModel"""

    def test_base_model_attrib_and_class(self):
        """Tests that BaseModel has correct attrs within the right class"""
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIsNotNone(base.id)
        self.assertIsNotNone(base.created_at)
        self.assertIsNotNone(base.updated_at)

    def test_base_model_attrib_type(self):
        """Tests that BaseModel attributes are of correct type"""
        base = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertEqual(len(base.id), 36)
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertIsInstance(base.updated_at, datetime.datetime)

    def test_base_model_checking_created_updated(self):
        """Tests that BaseModel updated_at is same as create_at"""
        base = BaseModel()
        self.assertEqual(base.updated_at, base.created_at)

    def test_base_model_str_method(self):
        """Tests that BaseModel str method"""
        base = BaseModel()
        base_str = base.__str__()
        self.assertIsInstance(base_str, str)
        self.assertEqual(base_str[:11], '[BaseModel]')
        self.assertEqual(base_str[12:50], '({})'.format(base.id))
        self.assertDictEqual(eval(base_str[51:]), base.__dict__)

    def test_base_model_save_method(self):
        """Tests that BaseModel save"""
        base = BaseModel()
        time.sleep(0.0001)
        base.save()
        self.assertNotEqual(base.updated_at, base.created_at)

    def test_base_model_to_dict_method(self):
        """Tests that BaseModel to_dict method creates a dict"""
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertIsInstance(base_dict, dict)
        self.assertEqual(base_dict['id'], base.id)
        self.assertEqual(base_dict['__class__'], type(base).__name__)
        self.assertEqual(base_dict['created_at'], base.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'], base.updated_at.isoformat())
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertIsInstance(base.updated_at, datetime.datetime)

    def test_base_model_dict_to_instance_with_kwargs(self):
        """Tests that BaseModel makes new obj with dict"""
        base = BaseModel()
        base.name = "Betty"
        base.number = 972
        base_dict = base.to_dict()
        new_base = BaseModel(**base_dict)
        new_base_dict = new_base.to_dict()
        self.assertFalse(new_base is base)
        self.assertDictEqual(new_base_dict, base_dict)

    def test_base_model_dict_to_instance_with_empty_kwargs(self):
        """Tests that BaseModel makes new obj with dict that has nothing"""
        base_dict = {}
        new_base = BaseModel(**base_dict)
        new_base_dict = new_base.to_dict()
        self.assertIsInstance(new_base, BaseModel)
        self.assertIsNotNone(new_base.id)
        self.assertIsNotNone(new_base.created_at)
        self.assertIsNotNone(new_base.updated_at)

if __name__ == '__main__':
    unittest.main()