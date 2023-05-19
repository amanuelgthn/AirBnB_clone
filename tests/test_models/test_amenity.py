#!/usr/bin/python3
"""
Module to test amenity module
"""

import unittest
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity


class Amenity_testcase(unittest.TestCase):
    """
    test case for User
    """
    def test_public_attributes(self):
        """
        test for public class attributes
        """
        model = Amenity()
        model.name = "Pools"
        self.assertEqual(model.name, "Pools")

