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
        self.assertTrue(hasattr(model, "place_id"))
        self.assertTrue(hasattr(model, "user_id"))
        self.assertTrue(hasattr(model, "text"))
        self.assertEqual(model.place_id, "")
        self.assertEqual(model.user_id, "")
        self.assertEqual(model.text, "")


if __name__ == "__main__":
    unittest.main()
