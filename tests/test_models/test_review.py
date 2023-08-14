#!/usr/bin/python3
"""Test suite for Review class in models.review"""

import unittest
from models.review import Review
import os

class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()

    def tearDown(self):
        del self.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_attributes(self):
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(self.review.place_id, "")
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(self.review.user_id, "")
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.text, "")

if __name__ == "__main__":
    unittest.main()
