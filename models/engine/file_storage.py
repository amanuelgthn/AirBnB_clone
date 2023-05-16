#!/usr/bin/python3
"""
Module that contains FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""


from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import json
import os


class FileStorage():
    """
    FileStorage Class
    """

    __file_path = "file.json"
    __objects = {}
    dict_ref = {"BaseModel": BaseModel,
                "User": User,
                "Amenity": Amenity,
                "Place": Place,
                "City": City,
                "Review": Review,
                "State":State}

    def all(self):
        return self.__objects
    def new(self, obj):
        if obj:
            name = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[name] = obj

    def save(self):
        file_dict = {}
        for key in self.__objects.keys():
            file_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path,"w+", encoding="utf-8") as file:
            json.dump(file_dict,file)
    def reload(self):
        """Deserialize/convert obj dicts back to instances, if it exists"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
               objects= json.load(file)
            for key, value in objects.items():
                obj = self.dict_ref[value['__class__']](**value)
                self.__objects[key] = obj
    def remove(self, key):
        self.__objects.pop(key)
