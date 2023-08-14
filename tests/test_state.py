#!/usr/bin/python3
"""Defines unittests for models/state.py"""

import unittest
from models.state import State

class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def tearDown(self):
        del self.state

    def test_attributes(self):
        self.assertTrue(hasattr(self.state, "name"))
        # ... add more attribute checks ...

if __name__ == "__main__":
    unittest.main()
