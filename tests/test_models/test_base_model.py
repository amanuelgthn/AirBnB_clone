#!/usr/bin/python3
"""
Module to unittest the base_model.py module
"""


from models import storage
from datetime import datetime
from uuid import uuid4
import unittest
from models.base_model import BaseModel

class BaseModel_TestCase(unittest.TestCase):
    def test_save(self):
        my_model = BaseModel()
        self.assertEqual(my_model.created_at,my_model.updated_at)
        my_model.save()
        self.assertGreater(my_model.updated_at, my_model.created_at)

    def test_init(self):
        """
        test for initiallization
        """
        """with no arguments Passed"""
        base = BaseModel()
        self.assertIsNotNone(base.id)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)
        """ with arguments"""
        base = BaseModel(id= 'b6a6e15c-c67d-4312-9a75-9d084935e579', created_at="2017-09-28T21:05:54.119572", updated_at="2017-09-28T21:05:54.119572")
        self.assertEqual(base.id, 'b6a6e15c-c67d-4312-9a75-9d084935e579')
  
    def test_to_dict(self):
        base = BaseModel(id= 'b6a6e15c-c67d-4312-9a75-9d084935e579', created_at="2017-09-28T21:05:54.119572", updated_at="2017-09-28T21:05:54.119572")
        base_dict = base.to_dict()
        self.assertEqual(base_dict, {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': '2017-09-28T21:05:54.119572', 'updated_at': '2017-09-28T21:05:54.119572', '__class__': 'BaseModel'})

    def test__str__(self):
        base = BaseModel(id= 'b6a6e15c-c67d-4312-9a75-9d084935e579', created_at="2017-09-28T21:05:54.119572", updated_at="2017-09-28T21:05:54.119572")
        base_print = base.__str__()
        self.assertEqual(base_print,"[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572), 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572)}")

if __name__ == "__main__":
    unittest.main()





