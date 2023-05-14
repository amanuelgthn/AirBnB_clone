#!/usr/bin/python3
"""
Module that contains FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""
from models.base_model import BaseModel
import json

class FileStorage():
    """
    FileStorage Class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    def new(self, obj):
        if obj:
            name = "{}.{}".format(obj.__class__.__name__,obj.id)
            self.__objects[name] = obj

    def save(self):
        file_dict = {}
        for key in self.__objects.keys():
            file_dict[key] = self.__objects[key].to_dict()
        with open(FileStorage.__file_path,'w', encoding="utf-8") as file:
            json.dump(file_dict,file)
    def reload(self):
        try:
            with open(self.__file_path,'r',encoding="utf-8") as file:
                objects = json.loads(file.read())
                for key in objects:
                    FileStorage.__objects[key] =objects[key].to_dict()
        except FileNotFoundError:
            pass