#!/usr/bin/python3
"""FileStorage unittests"""
import unittest
import models
import time
import os
from os import remove
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
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

    def test_file_storage_type(self):
        """Test that the storage instance is of the correct type"""
        storage_instance = FileStorage()
        self.assertIsInstance(storage_instance, FileStorage)

    def test_save_method_type_error(self):
        """Test that save method raises TypeError with incorrect arguments"""
        storage_instance = FileStorage()
        """Attempt to call save with an argument is not a BaseModel instance"""
        with self.assertRaises(TypeError):
            storage_instance.save("not_a_base_model_instance")

    def test_all_with_None(self):
        """Test if all method raises TypeError with None argument"""
        with self.assertRaises(TypeError):
            self.storage.all(None)

    def test_new_with_None(self):
        """Test if new method raises TypeError with None argument"""
        with self.assertRaises(TypeError):
            self.storage.new(None, None)

    def test_save_with_None(self):
        """Test if save method raises TypeError with None argument"""
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

    def test_file_path_types(self):
        """Test if the __file_path attribute is of type str"""
        self.assertEqual(type(models.storage._FileStorage__file_path), str)

    def test_objects_types(self):
        """Test if the objects attribute is of type dict"""
        self.assertEqual(type(models.storage._FileStorage__objects), dict)

    """ Tests invalid argument types"""

    def test_save_with_invalid_argument(self):
        with self.assertRaises(TypeError):
            models.storage.save(int())

    def test_reload_with_invalid_argument(self):
        with self.assertRaises(TypeError):
            models.storage.reload(int())

    """ Tests related to invalid argument types:"""

    def test_save_with_arguments(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_with_arguments(self):
        """Test if reload method raises TypeError with invalid arguments."""
        with self.assertRaises(TypeError):
            models.storage.reload([1, 2, 3])

    def test_FileStorage_file_path_private_and_str(self):
        """Check if __file_path attribute is a private string attribute."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_private_and_dict(self):
        """Check if __objects attribute is a private dictionary attribute."""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage(self):
        """Check if models.storage is an instance of FileStorage."""
        self.assertEqual(type(models.storage), FileStorage)

    def test_new_with_arguments(self):
        """Test if new method raises TypeError with invalid arguments."""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 10)

    def test_new(self):
        """Test adding various model instances to storage."""
        base1 = BaseModel()
        usr = User()
        st = State()
        plc = Place()
        cty = City()
        am = Amenity()
        rev = Review()

        models.storage.new(base1)
        models.storage.new(usr)
        models.storage.new(st)
        models.storage.new(plc)
        models.storage.new(cty)
        models.storage.new(am)
        models.storage.new(rev)

        self.assertIn("BaseModel." + base1.id, models.storage.all().keys())
        self.assertIn(base1, models.storage.all().values())
        self.assertIn("User." + usr.id, models.storage.all().keys())
        self.assertIn(usr, models.storage.all().values())
        self.assertIn("State." + st.id, models.storage.all().keys())
        self.assertIn(st, models.storage.all().values())
        self.assertIn("Place." + plc.id, models.storage.all().keys())
        self.assertIn(plc, models.storage.all().values())
        self.assertIn("City." + cty.id, models.storage.all().keys())
        self.assertIn(cty, models.storage.all().values())
        self.assertIn("Amenity." + am.id, models.storage.all().keys())
        self.assertIn(am, models.storage.all().values())
        self.assertIn("Review." + rev.id, models.storage.all().keys())
        self.assertIn(rev, models.storage.all().values())


if __name__ == '__main__':
    unittest.main()
