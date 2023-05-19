#!/usr/bin/python3
"""
Module to test city module
"""

import unittest
from models import storage
from models.base_model import BaseModel
from models.city import City


class City_testcase(unittest.TestCase):
    """
    test case for State
    """
    def test_public_attributes(self):
        """
        test for public class attributes
        """
        model = City()
        model.name = "LA City"
        model.state_id = "12"
        self.assertEqual(model.name, "California")
        self.assertEqual(model.state_id, "12")

if __name__ == "__main__":
    unittest.main()