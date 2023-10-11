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
