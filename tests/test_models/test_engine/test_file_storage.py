#!/usr/bin/python3
"""
Module to test file_storage.py module
"""


import unittest
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class FileStorage_testcase(unittest.TestCase):
    """
    test case for FileStorage
    """
    
    def setUp(self):
        self.storage = FileStorage()
    def test_all(self):
        self.assertEqual(self.storage.all(),{})
    def test_new(self):
        user = BaseModel()
        self.storage.new(user)
        self.assertIn("BaseModel.{}".format(user.id), self.storage.all())



if __name__ == "__main__":
    unittest.main()
