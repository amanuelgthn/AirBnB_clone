#!/usr/bin/python3
"""
Module to test file_storage.py module
"""


import unittest
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class FileStorage_testcase(unittest.TestCase):
    """
    test case for FileStorage
    """
    def test_file_path(self):
        my_model = BaseModel(BaseModel(id= 'b6a6e15c-c67d-4312-9a75-9d084935e579', created_at="2017-09-28T21:05:54.119572", updated_at="2017-09-28T21:05:54.119572"))
        my_model.save()
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if obj_id == "id":
                self.assertEqual(all_objs[id], 'b6a6e15c-c67d-4312-9a75-9d084935e579')
            if obj_id == "created_at":
                self.assertEqual(all_objs[created_at], datetime(2017, 9, 28, 21, 5, 54, 119572))
            if obj_id == "updated_at":
                self.assertEqual(all_objs[updated_at], datetime(2017, 9, 28, 21, 5, 54, 119572))

if __name__ == "__main__":
    unittest.main()