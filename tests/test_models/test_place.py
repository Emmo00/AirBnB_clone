#!/usr/bin/python3
"""test_place module
test module for place module
"""
from time import sleep
import unittest
import sys
from models.place import Place
from datetime import datetime

sys.path.insert(0, '../../')


class TestPlaceClass(unittest.TestCase):
    """TestPlaceClass class
    tests the Place class
    """
    def test_unique_id(self):
        model1 = Place()
        model2 = Place()
        self.assertFalse(model1.id == model2.id)

    def test_id_type(self):
        model = Place()
        self.assertIsInstance(model.id, str)

    def test_created_updated_type(self):
        model = Place()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str_representation(self):
        model = Place()
        self.assertIsInstance(model.__str__(), str)

    def test_updated_after_save(self):
        model = Place()
        update_time = model.updated_at
        sleep(2)
        model.save()
        self.assertNotEqual(update_time, model.updated_at)

    def test_default_values(self):
        place = Place()
        self.assertTrue(place.city_id == "")
        self.assertTrue(place.user_id == "")
        self.assertTrue(place.name == "")
        self.assertTrue(place.description == "")
        self.assertTrue(place.number_rooms == 0)
        self.assertTrue(place.number_bathrooms == 0)
        self.assertTrue(place.max_guest == 0)
        self.assertTrue(place.price_by_night == 0)
        self.assertTrue(place.latitude == 0.0)
        self.assertTrue(place.longitude == 0.0)
        self.assertTrue(place.amenity_ids == [])

    def test_to_dict(self):
        model = Place()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], model.__class__.__name__)
        self.assertIsInstance(model_dict['created_at'], str)

    def test_keyword_created_object(self):
        model1 = Place()
        model1_dict = model1.to_dict()
        model2 = Place(**model1_dict)
        self.assertFalse(model1 is model2)
        self.assertIsInstance(model2.created_at, datetime)


if __name__ == '__main__':
    unittest.main()
