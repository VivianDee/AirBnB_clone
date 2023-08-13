#!/usr/bin/python3
"""Defines unittests for models/user.py"""

import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def tearDown(self):
        del self.user

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        # ... add more attribute checks ...

if __name__ == "__main__":
    unittest.main()
