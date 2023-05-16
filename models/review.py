"""
Module that contains Review Class that inherits from BaseModel
"""

from models.base_model import BaseModel
from models.place import Place
from models.user import User


class City(BaseModel):
    """
    Review Class
    """

    place_id = ""
    user_id = ""
    text = ""
    
    def __init__(self, *args, **kwargs):
        """
        Initialization
        """
        super().__init__(self, *args, **kwargs)
        self.place_id = Place.id
        self.user_id = User.id
