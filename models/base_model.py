#!/usr/bin/python3
"""
Module that defines all the common attributes/methods for other classes
"""
import uuid
import datetime

class BaseModel:
    """
    BaseModel Class
    """


    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        
    def save(self):
        self.updated_at = datetime.datetime.now()
        
    def to_dict(self):
        return BaseModel.__dict__
    
    def __str__(self):
        """
        __str__ method
        """
        result = ""
        result = "[" + str(type(self).__name__) + "] " + "("
        result += str(self.id) + ") "
        result += str(self.__dict__)
        return result
        
