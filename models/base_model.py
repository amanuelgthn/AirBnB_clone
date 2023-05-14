#!/usr/bin/python3
"""
Module that defines all the common attributes/methods for other classes
"""


import uuid
import datetime
import models


class BaseModel:
    """
    BaseModel Class
    """

    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.datetime.strptime(value, time_format)
                elif key == "updated_at":
                    self.updated_at = datetime.datetime.strptime(value, time_format)
                else:
                   if key != "__class__":
                       setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

    def save(self):
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        public_attr = self.__dict__.copy()
        public_attr["created_at"] = self.created_at.isoformat()
        public_attr["updated_at"] = self.updated_at.isoformat()
        public_attr["__class__"] = __class__.__name__
        return public_attr

    def __str__(self):
        """
        __str__ method
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)
    def __repr__(self):
        return (self.__str__)
