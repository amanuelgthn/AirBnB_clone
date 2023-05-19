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
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        my_user.save()
        self.assertEqual(my_user.first_name, "Betty")
        self.assertEqual(my_user.last_name, "Bar")
        self.assertEqual(my_user.email, "airbnb@mail.com")
        self.assertEqual(my_user.first_name, "root")

if __name__ == "__main__":
    unittest.main()