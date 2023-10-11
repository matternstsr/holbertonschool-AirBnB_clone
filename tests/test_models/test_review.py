#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
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
        self.assertTrue(len(Review.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Review.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Review):
            self.assertTrue(len(func.__doc__) > 0)

    def test_is_instance(self):
        """ Test if user is an instance of BaseModel """
        my_Review = Review()
        self.assertTrue(isinstance(my_Review, BaseModel))

    def test_field_types(self):
        """ Test field attributes of user """
        my_Review = Review()
        self.assertTrue(type(my_Review.place_id) is str)
        self.assertTrue(type(my_Review.user_id) is str)
        self.assertTrue(type(my_Review.text) is str)

    def test_review(self):
        ''' test 'Review' exists '''
        inst_1 = Review()
        self.assertTrue(inst_1)

    def test_review_instance_del(self):
        ''' test 'Review' deletes '''
        inst_1_1 = Review()
        del inst_1_1

    def test_review_instance(self):
        ''' test 'Review' instance '''
        inst_2 = Review()
        self.assertIsInstance(inst_2, Review)

    def test_review_save(self):
        ''' test 'Review' saves '''
        inst_3 = Review()
        updated_review = inst_3.updated_at
        inst_3.save()
        new_inst_3 = inst_3.updated_at
        self.assertNotEqual(updated_review, new_inst_3)

    def test_place_id_str(self):
        ''' test 'Review' type '''
        inst_4 = Review()
        self.assertIsInstance(inst_4.place_id, str)

    def test_user_id_str(self):
        ''' test 'Review' type '''
        inst_5 = Review()
        self.assertIsInstance(inst_5.user_id, str)

    def test_text_str(self):
        ''' test 'Review' type '''
        inst_6 = Review()
        self.assertIsInstance(inst_6.text, str)


if __name__ == '__main__':
    unittest.main()
