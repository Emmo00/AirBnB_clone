import json
import os


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
        )] = obj.to_dict()
    
    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)
    
    def reload(self):
        if os.path.exists(self.__file_path) == False:
            return
        with open(self.__file_path, 'r') as f:
            self.__objects = json.load(f)
