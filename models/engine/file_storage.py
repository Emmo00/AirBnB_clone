#!/usr/bin/python3
"""file_storage module.
Defines the FileStorage class
"""
import json
import os
from ..base_model import BaseModel
from ..user import User
from ..amenity import Amenity
from ..city import City
from ..place import Place
from ..review import Review
from ..state import State


class FileStorage:
    """FileStorage class
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the objects loaded
        from json file
        """
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(
            obj.__class__.__name__,
            obj.id
        )] = obj

    def save(self):
        """save the object in __objects to file
        in dictionary form
        """
        with open(self.__file_path, 'w') as f:
            to_save = {}
            for key, value in self.__objects.items():
                to_save[key] = value.to_dict()
            json.dump(to_save, f)

    def reload(self):
        """reload objects from file
        """
        if not os.path.exists(self.__file_path):
            return
        with open(self.__file_path, 'r') as f:
            self.__objects = json.load(f)
        for key, value in self.__objects.items():
            self.__objects[key] = eval(f"{value['__class__']}(**value)")
