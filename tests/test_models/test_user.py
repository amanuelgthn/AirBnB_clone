#!/usr/bin/python3
"""
Module to test user module
"""

import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User


class User_testcase(unittest.TestCase):
    """
    test case for User
    """
    def test_public_attributes(self):
        """
        test for public class attributes
        """
        User.first_name = "Betty"
        User.last_name = "Bar"
        User.email = "airbnb@mail.com"
        User.password = "root"
        self.assertEqual(User.first_name, 'Betty')
        self.assertEqual(User.last_name, "Bar")
        self.assertEqual(User.email, "airbnb@mail.com")
        self.assertEqual(User.password, "root")

if __name__ == "__main__":
    unittest.main()
