#!/usr/bin/python3
"""
Module that contains User Class that inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User Class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialization
        """
        super().__init__(self, *args, **kwargs)
