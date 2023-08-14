#!/usr/bin/python3
"""Defines unittests for models/place.py"""

import unittest
from models.place import Place
import os

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def tearDown(self):
        del self.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_attributes(self):
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(self.place.city_id, "")
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(self.place.user_id, "")
        # Add more assertions for other attributes

if __name__ == "__main__":
    unittest.main()
