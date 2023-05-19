#!/usr/bin/python3
"""
Module to test review module
"""

import unittest
from models import storage
from models.base_model import BaseModel
from models.review import Review



class Review_testcase(unittest.TestCase):
    """
    test case for State
    """
    def test_public_attributes(self):
        """
        test for public class attributes
        """
        model = Review()
        model.place_id = "5555"
        model.user_id = "4444"
        model.text = "Great"
        self.assertEqual(model.place_id, "5555")
        self.assertEqual(model.user_id, "4444")
        self.assertEqual(model.text, "Great")

if __name__ == "__main__":
    unittest.main()