#!/usr/bin/python3
"""Defines unittests for models/base_model.py"""

import unittest
from models.base_model import BaseModel
from models import storage
import json
import os

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        del self.base_model
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_attributes(self):
        self.assertTrue(hasattr(self.base_model, "id"))
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))

    def test_save_method(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        base_model_dict = self.base_model.to_dict()
        self.assertTrue("id" in base_model_dict)
        self.assertTrue("created_at" in base_model_dict)
        self.assertTrue("updated_at" in base_model_dict)
        self.assertTrue("__class__" in base_model_dict)

if __name__ == "__main__":
    unittest.main()
