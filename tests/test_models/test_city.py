#!/usr/bin/python3
"""Test City"""
import unittest
from models.base_model import BaseModel
from models.city import City


class Testcity(unittest.TestCase):
    """Unittests for the City class."""

    def test_class(self):
        """Tests if the correct class."""
        city1 = City()
        self.assertEqual(city1.__class__.__name__, "City")

    def test_inheritance(self):
        """Tests if Class inherits from BaseModel."""
        city1 = City()
        self.assertTrue(issubclass(city1.__class__, BaseModel))

    def setUp(self):
        """Return to "" class attributes"""
        City.name = ""
        City.state_id = ""

    def test_module_doc(self):
        """Check for module documentation"""
        self.assertTrue(len(City.__doc__) > 0)

    def test_class_doc(self):
        """Check for class documentation"""
        self.assertTrue(len(City.__doc__) > 0)

    def test_method_docs(self):
        """Check for method documentation"""
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)

    def test_is_instance(self):
        """Test if City is an instance of BaseModel"""
        my_city = City()
        self.assertTrue(isinstance(my_city, BaseModel))

    def test_field_types(self):
        """Test field attributes of City"""
        my_city = City()
        self.assertTrue(type(my_city.name) is str)
        self.assertTrue(type(my_city.state_id) is str)

    def test_city(self):
        '''Test if 'City' exists'''
        inst_1 = City()
        self.assertTrue(inst_1)

    def test_city_instance_del(self):
        '''Test if 'City' deletes'''
        inst_1_1 = City()
        del inst_1_1

    def test_city_instance(self):
        '''Test if 'City' is an instance of City'''
        inst_2 = City()
        self.assertIsInstance(inst_2, City)

    def test_city_save(self):
        '''Test if 'City' saves'''
        inst_3 = City()
        updated_city = inst_3.updated_at
        inst_3.save()
        new_inst_3 = inst_3.updated_at
        self.assertNotEqual(updated_city, new_inst_3)

    def test_name_str(self):
        '''Test if 'City' name is a string'''
        inst_4 = City()
        self.assertIsInstance(inst_4.name, str)

    def test_state_id_str(self):
        '''Test if 'City' state_id is a string'''
        inst_5 = City()
        self.assertIsInstance(inst_5.state_id, str)


if __name__ == '__main__':
    unittest.main()
