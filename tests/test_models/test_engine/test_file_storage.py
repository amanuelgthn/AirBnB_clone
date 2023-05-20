#!/usr/bin/python3
"""
Module to test file_storage.py module
"""


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class FileStorage_testcase(unittest.TestCase):
    """
    test case for FileStorage
    """
    def test_file_path(self):
        my_model = BaseModel()
        my_model.save()
        self.assertEqual(my_model., "file.json")

if __name__ == "__main__":
    unittest.main()