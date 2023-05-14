#!/usr/bin/python3
"""file_storage module
Defines the FileStorage class.
"""
import json
import os
from ..base_model import BaseModel
from ..user import User


class FileStorage:
    """storage engine that that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        self.__objects["{}.{}".format(
            obj.__class__.__name__,
            obj.id
        )] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        with open(self.__file_path, 'w') as f:
            to_save = {}
            for key, value in self.__objects.items():
                to_save[key] = value.to_dict()
            json.dump(to_save, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if not os.path.exists(self.__file_path):
            return
        with open(self.__file_path, 'r') as f:
            self.__objects = json.load(f)
        for key, value in self.__objects.items():
            self.__objects[key] = eval(f"{value['__class__']}(**value)")
