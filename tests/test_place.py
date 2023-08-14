#!/usr/bin/python3
"""Defines unittests for models/place.py"""

import unittest
from models.place import Place

class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()

    def tearDown(self):
        del self.place

    def test_attributes(self):
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        # ... add more attribute checks ...

if __name__ == "__main__":
    unittest.main()

