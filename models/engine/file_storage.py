#!/usr/bin/python3
"""
Module that contains FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances
"""
import json
import uuid
import datetime

class FileStorage:
    """
    FileStorage Class
    """

    def __init__(self, file_path):
        self.__file_path = file_path
        self.__objects = {}

    @property
    def file_path(self):
        return self.__file_path
    
    def all(self):
        return self.__objects
    def new(self, obj):
        if obj.__class__.__name__ not in self.__objects:
            self.__objects[obj.__class__.__name__] = []
        self.__objects[obj.__class__.__name__]= obj
    def save(self):
        with open(self.__file_path,'w',
    