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
        test for first_name
        """
        my_user = User()
        my_user.save()
        my_user2 = User()
        my_user2.first_name = "John"
        my_user2.email = "airbnb2@mail.com"
        my_user2.last_name = "Phalange"
        my_user2.password = "root2"
        my_user2.save()
        self.assertTrue(hasattr(my_user, "first_name"))
        self.assertEqual(my_user.first_name, "")
        self.assertTrue(hasattr(my_user, "last_name"))
        self.assertEqual(my_user.last_name, "")
        self.assertEqual(my_user.email, "")
        self.assertTrue(hasattr(my_user, "email"))
        self.assertEqual(my_user.password, "")
        self.assertTrue(hasattr(my_user, "password"))
        self.assertEqual(my_user2.first_name, "John")
        self.assertEqual(my_user2.last_name, "Phalange")
        self.assertEqual(my_user2.email, "airbnb2@mail.com")
        self.assertEqual(my_user2.password, "root2")

if __name__ == "__main__":
    unittest.main()
    