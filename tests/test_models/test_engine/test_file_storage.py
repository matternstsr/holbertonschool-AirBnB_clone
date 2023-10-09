#!/usr/bin/python3
"""FileStorage unittests"""
import unittest
import time
import os
from os import remove
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """class TestFileStorage"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = BaseModel()
        cls.user.name = "Kev"
        cls.user.my_number = 42
        cls.storage = FileStorage()
        cls.path = "file.json"

    @classmethod
    def tearDownClass(cls):
        """at the end of the test this will tear it down"""
        del cls.user
        """ if delete the file """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_file_storage_all_method(self):
        """FileStorage all method contains dict of BaseModel objs"""
        storage_instance = FileStorage()
        storage_dict = storage_instance.all()
        self.assertIsInstance(storage_dict, dict)
        for obj_instance in storage_dict.values():
            self.assertIsInstance(obj_instance, BaseModel)

    def test_file_storage_new_method(self):
        """FileStorage new method adds object"""
        base_instance = BaseModel()
        storage_instance = FileStorage()
        storage_dict = storage_instance.all()
        key = '{}.{}'.format(type(base_instance).__name__, base_instance.id)
        self.assertTrue(key in storage_dict.keys())

    def test_file_storage_save_method(self):
        """FileStorage save method updates __objects"""
        base_instance = BaseModel()
        key = '{}.{}'.format(type(base_instance).__name__, base_instance.id)
        base_updated_0 = base_instance.updated_at
        storage_instance = FileStorage()
        objs_0 = storage_instance.all()
        dt_0 = objs_0[key].updated_at

        time.sleep(0.0001)
        base_instance.save()

        base_updated_1 = base_instance.updated_at
        objs_1 = storage_instance.all()
        dt_1 = objs_1[key].updated_at

        self.assertNotEqual(base_updated_1, base_updated_0)
        self.assertNotEqual(dt_1, dt_0)

        try:
            with open('file.json', 'r'):
                remove('file.json')
        except FileNotFoundError:
            self.assertEqual(1, 2)

    def test_docstring(self):
        """Test docstring"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_documentation(self):
        """Test documentation, created and not empty"""
        self.assertTrue(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertTrue(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertTrue(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertTrue(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)


if __name__ == '__main__':
    unittest.main()
