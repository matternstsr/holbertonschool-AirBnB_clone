#!/usr/bin/python3
"""Test User"""
import unittest
from models.user import User
from models.base_model import BaseModel


class Testuser(unittest.TestCase):
    """unittests for the user class."""

    def test_class(self):
        """Tests for the correct class."""
        user1 = User()
        self.assertEqual(user1.__class__.__name__, "User")

    def test_inheritance(self):
        """Tests if the class inherits from BaseModel"""
        user1 = User()
        self.assertEqual(user1.__class__.__name__, "User")

    def test_module_doc(self):
        """Check for module documentation"""
        self.assertTrue(len(User.__doc__) > 0)

    def test_class_doc(self):
        """Check for documentation"""
        self.assertTrue(len(User.__doc__) > 0)

    def test_method_docs(self):
        """Check for method documentation"""
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)

    def test_is_instance(self):
        """Test if user is an instance of BaseModel"""
        my_user = User()
        self.assertTrue(isinstance(my_user, BaseModel))

    def test_field_types(self):
        """Test field attributes of user"""
        my_user = User()
        self.assertTrue(type(my_user.email) is str)
        self.assertTrue(type(my_user.password) is str)
        self.assertTrue(type(my_user.first_name) is str)
        self.assertTrue(type(my_user.last_name) is str)

    def test_user(self):
        """Test 'User' exists"""
        inst_1 = User()
        self.assertTrue(inst_1)

    def test_user_instance_del(self):
        """Test 'User' deletes"""
        inst_1_1 = User()
        del inst_1_1

    def test_user_instance(self):
        """Test 'User' instance"""
        inst_2 = User()
        self.assertIsInstance(inst_2, User)

    def test_user_save(self):
        """Test 'User' saves"""
        inst_3 = User()
        updated_user = inst_3.updated_at
        inst_3.save()
        new_inst_3 = inst_3.updated_at
        self.assertNotEqual(updated_user, new_inst_3)

    def test_email_str(self):
        """Test 'User' type"""
        inst_4 = User()
        self.assertIsInstance(inst_4.email, str)

    def test_password_str(self):
        """Test 'User' type"""
        inst_5 = User()
        self.assertIsInstance(inst_5.password, str)

    def test_first_name_str(self):
        """Test 'User' type"""
        inst_6 = User()
        self.assertIsInstance(inst_6.first_name, str)

    def test_last_name_str(self):
        """Test 'User' type"""
        inst_7 = User()
        self.assertIsInstance(inst_7.last_name, str)


if __name__ == '__main__':
    unittest.main()
