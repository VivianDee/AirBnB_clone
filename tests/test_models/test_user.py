#!/usr/bin/python3
"""Defines unittests for models/user.py"""

import unittest
from models.user import User
import os

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def tearDown(self):
        del self.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(self.user.email, "")
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(self.user.password, "")
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(self.user.first_name, "")
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.last_name, "")

if __name__ == "__main__":
    unittest.main()
