#!/usr/bin/python3
"""
Module that contains Amenity Class that inherits from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Class
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialization
        """
        super().__init__(self, *args, **kwargs)
