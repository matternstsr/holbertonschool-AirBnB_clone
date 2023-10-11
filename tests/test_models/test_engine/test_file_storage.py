#!/usr/bin/python3
"""FileStorage unittests"""
import os
import unittest
import uuid
import json
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


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

    @classmethod
    def tearDown(cls):
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

    def test_file_storage_type(self):
        """Test that the storage instance is of the correct type"""
        storage_instance = FileStorage()
        self.assertIsInstance(storage_instance, FileStorage)

    def test_save_method_type_error(self):
        """Test that save method raises TypeError with incorrect arguments"""
        storage_instance = FileStorage()
        """Attempt to call save with an argument that is not a BaseModel instance"""
        with self.assertRaises(TypeError):
            storage_instance.save("not_a_base_model_instance")

    def test_all_with_None(self):
        """Test if the all method raises TypeError with None argument"""
        with self.assertRaises(TypeError):
            self.storage.all(None)

    def test_new_with_None(self):
        """Test if the new method raises TypeError with None argument"""
        with self.assertRaises(TypeError):
            self.storage.new(None, None)

    def test_save_with_None(self):
        """Test if the save method raises TypeError with None argument"""
        with self.assertRaises(TypeError):
            self.storage.save(None)

    def test_file_path_type(self):
        """Test if the file path attribute is a string"""
        self.assertIsInstance(self.storage._FileStorage__file_path, str)

    def test_objects_type(self):
        """Test if the objects attribute is a dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_file_path_private(self):
        """Test if the file path attribute is private (starts with an underscore)"""
        self.assertTrue(hasattr(self.storage, '_FileStorage__file_path'))

    def test_objects_private(self):
        """Test if the objects attribute is private (starts with an underscore)"""
        self.assertTrue(hasattr(self.storage, '_FileStorage__objects'))

    def test_objects_types(self):
        """Test if the objects attribute is of type dict"""
        self.assertEqual(type(self.storage._FileStorage__objects), dict)

    def test_base_model_id_is_string(self):
        """UUID format testing."""
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_base_model_uuid_good_format(self):
        """Tests if UUID is in the correct format."""
        bm = BaseModel()
        self.assertIsInstance(uuid.UUID(bm.id), uuid.UUID)

    def test_base_model_created_at_is_datetime(self):
        """Datetime test."""
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)

    def test_base_model_updated_at_is_datetime(self):
        """Datetime test."""
        bm = BaseModel()
        self.assertIsInstance(bm.updated_at, datetime)

    def test_all(self):
        """tests if all works in File Storage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_new(self):
        """test when new is created"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = "123455"
        user.name = "Kevin"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload_filestorage(self):
        """
        tests reload
        """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, self.path)
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except Exception:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except Exception:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == '__main__':
    unittest.main()
