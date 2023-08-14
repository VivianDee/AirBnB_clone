#!/usr/bin/python3
"""Defines unittests for models/state.py"""

import unittest
from models.state import State
import os

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def tearDown(self):
        del self.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_attributes(self):
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

if __name__ == "__main__":
    unittest.main()
