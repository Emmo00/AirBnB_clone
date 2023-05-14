#!/usr/bin/python3
import unittest
import sys

sys.path.insert(0, '../../../')

from models.engine.file_storage import FileStorage


class TestFileStorageClass(unittest.TestCase):
    # test that object data is persisted
        # create a BaseModel instance
        # save the instance with the .save() method
        # call FileStorage().all() and confirm that the instance is there
    # test that the data persisted is the correct type and correct format generally i.e {'str': dict} (👍⚡)
    # test if file.json exists after we save from the base model
    # implement a clean up method that would delete the file.json file (you can use the tearDownClass method)
    pass

if __name__ == '__main__':
    unittest.main()