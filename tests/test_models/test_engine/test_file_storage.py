#!/usr/bin/python3
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorageClass(unittest.TestCase):
    def setUp(self):
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_typeof_tmp_storage(self):
        my_storage = FileStorage()
        self.assertIsInstance(my_storage.all(), dict)

    def test_object_saved(self):
        my_storage = FileStorage()
        obj1 = BaseModel()
        my_storage.new(obj1)
        self.assertTrue(
            f"{obj1.__class__.__name__}.{obj1.id}" in my_storage.all()
            )

    def test_date_persist(self):
        # test that object data is persisted
        my_storage = FileStorage()
        self.assertIsInstance(my_storage.all(), dict)
        self.assertTrue(my_storage.all() == {})
        my_storage.reload()
        self.assertTrue(my_storage.all() == {})
        obj1 = BaseModel()
        my_storage.new(obj1)
        self.assertTrue(len(my_storage.all()) == 1)
        self.assertTrue(
            f"{obj1.__class__.__name__}.{obj1.id}" in my_storage.all()
        )
        my_storage.save()
        self.assertTrue(os.path.exists('file.json'))
        # reload from another file storage class
        another_storage = FileStorage()
        another_storage.reload()
        self.assertTrue(len(another_storage.all()) == 1)

    def test_storage_format(self):
        # test that the data persisted is the correct type and correct
        # format generally i.e {'str': dict} (👍⚡)
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj1.save()
        obj2.save()
        my_storage = FileStorage()
        my_storage.reload()
        for key, value in my_storage.all().items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(value, BaseModel)

    def test_storage_file_created(self):
        # test if file.json exists after we save from the base model
        self.assertTrue(not os.path.exists('file.json'))
        obj1 = BaseModel()
        obj1.save()
        self.assertTrue(os.path.exists('file.json'))

    def tearDown(self):
        if os.path.exists('file.json'):
            os.remove('file.json')


if __name__ == '__main__':
    unittest.main()
