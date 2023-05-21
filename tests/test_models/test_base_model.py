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
    def setUp(self):
        self.my_model = BaseModel()
    def test_save(self):
        self.assertEqual(self.my_model.created_at,  self.my_model.updated_at)
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
        base = BaseModel(id='b6a6e15c-c67d-4312-9a75-9d084935e579',
                         created_at="2017-09-28T21:05:54.119572",
                         updated_at="2017-09-28T21:05:54.119572")
        self.assertEqual(base.id, 'b6a6e15c-c67d-4312-9a75-9d084935e579')

    def test_to_dict(self):
        base = BaseModel(id='b6a6e15c-c67d-4312-9a75-9d084935e579',
                         created_at="2017-09-28T21:05:54.119572",
                         updated_at="2017-09-28T21:05:54.119572")
        dic = base.to_dict()
        self.assertEqual(dic, {'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
                               'created_at': '2017-09-28T21:05:54.119572',
                               'updated_at': '2017-09-28T21:05:54.119572',
                               '__class__': 'BaseModel'})

    def test__str__(self):
        base = BaseModel(id='b6a6e15c-c67d-4312-9a75-9d084935e579',
                         created_at="2017-09-28T21:05:54.119572",
                         updated_at="2017-09-28T21:05:54.119572")
        base_print = base.__str__()
        str_base = "[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) "
        str_base += "{'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', "
        str_base += "'created_at': datetime.datetime(2017, "
        str_base += "9, 28, 21, 5, 54, 119572), 'updated_at': "
        str_base += "datetime.datetime(2017, 9, 28, 21, 5, 54, 119572)}"
        self.assertEqual(base_print, str_base)


if __name__ == "__main__":
    unittest.main()
