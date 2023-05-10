#!/usr/bin/python3
"""
Module that defines all the common attributes/methods for other classes
"""
import uuid
import datetime

class BaseModel():
    """
    BaseModel Class
    """


    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().strftime(%Y-%m-%dT%H:%M:%S.%f)
        self.updated_at = datetime.now().strftime(%Y-%m-%dT%H:%M:%S.%f)
    def save(self):
        self.updated_at = datetime.now().strftime(%Y-%m-%dT%H:%M:%S.%f)
    def to_dict(self):
    def __str__(self):
          """
        __str__ method
        """
        result = ""
        result = "[" + str(type(self).__name__) + "] " + "("
        result += str(self.id) + ") "
        result += str(self.__dict__)
        return result
        
