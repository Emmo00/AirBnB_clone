#!/usr/bin/python3
"""test_user module
test module for user module
"""
from time import sleep
import unittest
import sys
from models.user import User
from datetime import datetime

sys.path.insert(0, '../../')


class TestUserClass(unittest.TestCase):
    """TestUserClass class
    tests the User class
    """
    def test_unique_id(self):
        model1 = User()
        model2 = User()
        self.assertFalse(model1.id == model2.id)

    def test_id_type(self):
        model = User()
        self.assertIsInstance(model.id, str)

    def test_created_updated_type(self):
        model = User()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_representation(self):
        model = User()
        self.assertIsInstance(model.__str__(), str)

    def test_updated_after_save(self):
        model = User()
        update_time = model.updated_at
        sleep(2)
        model.save()
        self.assertNotEqual(update_time, model.updated_at)
        
    def test_default_values(self):
        user = User()
        self.assertTrue(user.email == "")
        self.assertTrue(user.password == "")
        self.assertTrue(user.first_name == "")
        self.assertTrue(user.last_name == "")

    def test_to_dict(self):
        model = User()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], model.__class__.__name__)
        self.assertIsInstance(model_dict['created_at'], str)

    def test_keyword_created_object(self):
        model1 = User()
        model1_dict = model1.to_dict()
        model2 = User(**model1_dict)
        self.assertFalse(model1 is model2)
        self.assertIsInstance(model2.created_at, datetime)


if __name__ == '__main__':
    unittest.main()
