#!/usr/bin/python3
import json
import os
from ..base_model import BaseModel
from ..user import User


class FileStorage:
    def __init__(self):
        self.__file_path = 'file.json'
        self.__objects = {}
    
    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects["{}.{}".format(
            obj.__class__.__name__,
            obj.id
        )] = obj
    
    def save(self):
        with open(self.__file_path, 'w') as f:
            to_save = {}
            for key, value in self.__objects.items():
                to_save[key] = value.to_dict()
            json.dump(to_save, f)
    
    def reload(self):
        if os.path.exists(self.__file_path) == False:
            return
        with open(self.__file_path, 'r') as f:
            self.__objects = json.load(f)
        for key, value in self.__objects.items():
            self.__objects[key] = eval(f"{value['__class__']}(**value)")
