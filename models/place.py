#!/usr/bin/python3
"""
Module that contains Place Class that inherits from BaseModel
"""

from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity

class Place(BaseModel):
    """
    Place Class
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    
    def __init__(self, *args, **kwargs):
        """
        Initialization
        """
        super().__init__(self, *args, **kwargs)
        self.city_id = City.id
        self.user_id = User.id
        self.amenity_ids.append(Amenity.id)

