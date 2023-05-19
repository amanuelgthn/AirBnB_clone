#!/usr/bin/python3
"""
Module to test Place module
"""

import unittest
from models import storage
from models.base_model import BaseModel
from models.place import Place


class City_testcase(unittest.TestCase):
    """
    test case for State
    """
    def test_public_attributes(self):
        """
        test for public class attributes
        """
        model = Place()
        model.name = "Suburbs"
        model.city_id = "12"
        model.user_id = "14"
        model.description = "New"
        model.number_rooms = 2
        model.number_bathrooms = 1
        model.max_guest = 2
        model.price_by_night = 100
        model.latitude = 4.5
        model.longitude = 5.8
        model.amenity_ids = [5,4]
        self.assertEqual(model.name, "Suburbs")
        self.assertEqual(model.city_id, "12")
        self.assertEqual(model.user_id, "14")
        self.assertEqual(model.description, "New")
        self.assertEqual(model.number_rooms, "2")
        self.assertEqual(model.number_bathrooms, "1")
        self.assertEqual(model.max_guest, 2)
        self.assertEqual(model.price_by_night, 100)
        self.assertEqual(model.latitude, 4.5 )
        self.assertEqual(model.longitude, 5.8)
        self.assertIn(model.amenity_ids, 5)

if __name__ == "__main__":
    unittest.main()