#!/usr/bin/python3
"""
Module that contains City Class that inherits from BaseModel
"""

from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """
    City Class
    """

    state_id = ""
    name = ""
    
    def __init__(self, *args, **kwargs):
        """
        Initialization
        """
        super().__init__(self, *args, **kwargs)


