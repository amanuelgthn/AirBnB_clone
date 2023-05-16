#!/usr/bin/python3
"""
Module that contains State Class that inherits from BaseModel
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State Class
    """

    name = ""

    def __init__(self, *args, **kwargs):
        """
        Initialization
        """
        super().__init__(self, *args, **kwargs)
