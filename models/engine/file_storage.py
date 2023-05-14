#!/usr/bin/python3
"""
Module that contains FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""
from models.base_model import BaseModel
import json
import uuid
import os
import datetime

class FileStorage():
    """
    FileStorage Class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    def new(self, obj):
        if obj.__class__.__name__ not in self.__objects:
            FileStorage.__objects[obj.__class__.__name__] = []
        FileStorage.__objects[obj.__class__.__name__]= obj

    def save(self):
        file_dict = {}
        for key in self.__objects.keys():
            file_dict[key] = self.__objects[key].to_dict()
        with open(FileStorage.__file_path,'w', encoding="utf-8") as file:
            json.dump(file_dict,file)
    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path,'r',encoding="utf-8") as file:
                objects = json.loads(file.read())
                for key in objects:
                    FileStorage.__objects[key] =objects[key]
