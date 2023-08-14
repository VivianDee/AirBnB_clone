#!/usr/bin/python3
"""Defines unittests for models/amenity.py"""

import unittest
from models.amenity import Amenity
import os

class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        del self.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_attributes(self):
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")

if __name__ == "__main__":
    unittest.main()
