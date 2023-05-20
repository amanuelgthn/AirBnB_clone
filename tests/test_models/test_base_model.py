#!/usr/bin/python3
"""
Module to unittest the base_model.py module
"""


from datetime import datetime
from uuid import uuid4
import unittest
from models.base_model import BaseModel

class BaseModel_TestCase(unittest.TestCase):
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
        self.assertEqual(base.created_at, datetime(2017, 9, 28, 21, 5, 54, 119572))
        self.assertEqual(base.updated_at, datetime(2017, 9, 28, 21, 5, 54, 119572))

if __name__ == "__main__":
    unittest.main()





