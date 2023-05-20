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
    def test_first_name(self):
        """
        test for public class attributes
        """
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        my_user.save()
        my_user2 = User()
        my_user2.first_name = "John"
        my_user2.email = "airbnb2@mail.com"
        my_user2.last_name = "Phalange"
        my_user2.password = "root2"
        my_user2.save()
        self.assertTrue(hasattr(my_user, "first_name"))
        self.assertEqual(my_user.first_name, "Betty")
        self.assertEqual(my_user.last_name, "Bar")
        self.assertEqual(my_user.email, "airbnb@mail.com")
        self.assertEqual(my_user.password, "root")
        self.assertEqual(my_user2.first_name, "John")
        self.assertEqual(my_user2.last_name, "Phalange")
        self.assertEqual(my_user2.email, "airbnb2@mail.com")
        self.assertEqual(my_user2.password, "root2")

if __name__ == "__main__":
    unittest.main()
    