#!/usr/bin/python3
"""
Module to test file_storage.py module
"""


import unittest
import json
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
    def test_save(self):
        user = User()
        self.storage.new(user)
        self.storage.save()
        with open(self.storage.file_path, 'r', encoding="UTF-8") as file:
            objects = json.load(file)
        self.assertEqual(objects["User.{}".format(user.id)], user.to_dict())


if __name__ == "__main__":
    unittest.main()
