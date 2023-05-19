#!/usr/bin/python3
"""
Module to test State module
"""

import unittest
from models import storage
from models.base_model import BaseModel
from models.state import State


class State_testcase(unittest.TestCase):
    """
    test case for State
    """
    def test_public_attributes(self):
        """
        test for public class attributes
        """
        model = State()
        model.name = "California"
        self.assertEqual(model.name, "California")

if __name__ == "__main__":
    unittest.main()