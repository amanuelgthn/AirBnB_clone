#!/usr/bin/python3
"""
Module that contains FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""
from models.base_model import BaseModel
import json
dict_ref = {"BaseModel": BaseModel}

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
            name = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[name] = obj

    def save(self):
        file_dict = {}
        for key in self.__objects.keys():
            file_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path,"w+", encoding="utf-8") as file:
            json.dump(file_dict,file)
    #def reload(self):
       # try:
           # with open(self.__file_path,'r',encoding="utf-8") as file:
            ##    objects = json.load(file)
               # for key in objects:
               #     self.__objects[key] = dict_ref[objects[key]["__class__"]](**objects[key])
       # except FileNotFoundError:
           # pass
    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass