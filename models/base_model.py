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

    def __init__(self, *args, **kwargs):
        id_found = False
        created_found = False
        updated_found = False
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                    id_found = True
                elif key == "created_at":
                    self.created_at = value
                    created_found = True
                elif key == "updated_at":
                    self.updated_at = value
                    updated_found = True
                else:
                    self.key = value
        if id_found is False:
            self.id = str(uuid.uuid4())
        if created_found is False:
            self.created_at = datetime.datetime.now()
        if updated_found is False:
            self.updated_at = datetime.datetime.now()

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        public_attr = self.__dict__.copy()
        if "created_at" in public_attr.keys():
            public_attr["created_at"] = public_attr["created_at"].isoformat()
        if "updated_at" in public_attr.keys():
            public_attr["updated_at"] = public_attr["updated_at"].isoformat()
        public_attr["__class__"] = str(type(self).__name__)
        return public_attr

    def __str__(self):
        """
        __str__ method
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id, self.__dict__)
