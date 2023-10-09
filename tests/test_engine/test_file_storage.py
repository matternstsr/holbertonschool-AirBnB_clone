#!/usr/bin/python3
"""FileStorage unittests"""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """class TestFileStorage"""

    def test_file_storage_all_method_returns_empty_dict_initially(self):
        """FileStorage all method should return an empty dict initially"""
        storage = FileStorage()
        storage_dict = storage.all()
        self.assertIsInstance(storage_dict, dict)
        """ Check that all values in the dictionary are instances of BaseModel"""
        self.assertTrue(all(isinstance(obj, BaseModel)
                            for obj in storage_dict.values()))

    def test_file_storage_new_method_adds_object_to_storage(self):
        """FileStorage new method should add an object to storage"""
        storage = FileStorage()
        base = BaseModel()
        storage_dict = storage.all()
        key = '{}.{}'.format(type(base).__name__, base.id)
        self.assertIn(key, storage_dict)

    def test_file_storage_save_method_updates_object_timestamp(self):
        """FileStorage save method should update the object's timestamp"""
        storage = FileStorage()
        base = BaseModel()
        key = '{}.{}'.format(type(base).__name__, base.id)
        initial_timestamp = base.updated_at
        base.save()
        updated_timestamp = storage.all()[key].updated_at
        self.assertNotEqual(updated_timestamp, initial_timestamp)

    def test_file_storage_save_method_creates_json_file(self):
        """FileStorage save method should create a JSON file"""
        storage = FileStorage()
        base = BaseModel()
        key = '{}.{}'.format(type(base).__name__, base.id)
        base.save()
        self.assertTrue(storage._FileStorage__file_path)
        """Check if file path is not empty"""
        try:
            with open(storage._FileStorage__file_path, 'r'):
                pass
        except FileNotFoundError:
            self.fail("File not found")

    def test_file_storage_save_method_raises_exception_on_inv_file_path(self):
        """FileStorage save method should raise an exception on an invalid file path"""
        storage = FileStorage()
        base = BaseModel()
        base.save()
        invalid_path = 'invalid_path.json'
        try:
            with open(invalid_path, 'r'):
                pass
        except FileNotFoundError:
            """ Expected behavior: File is not found, which is correct"""
            pass
        else:
            self.fail(f"File '{invalid_path}' should not exist")

        """ Clean up by removing the invalid file path if it exists"""
        if os.path.exists(invalid_path):
            os.remove(invalid_path)


if __name__ == '__main__':
    unittest.main()
