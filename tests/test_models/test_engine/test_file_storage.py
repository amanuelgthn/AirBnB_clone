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
    
    
    def test_all(self):
        model= FileStorage()
        self.assertTrue(model.all() == {})


if __name__ == "__main__":
    unittest.main()
