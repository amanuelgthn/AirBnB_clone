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
        self.assertTrue(hasattr(model, "name"))
        self.assertTrue(hasattr(model, "state_id"))
        self.assertEqual(model.name, "")
        self.assertEqual(model.state_id, "")


if __name__ == "__main__":
    unittest.main()
