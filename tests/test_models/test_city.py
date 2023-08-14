#!/usr/bin/python3
"""Test suite for the City class of the models.city module"""

import unittest
from models.city import City
import os

class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()

    def tearDown(self):
        del self.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_attributes(self):
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.state_id, "")
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.name, "")

if __name__ == "__main__":
    unittest.main()
