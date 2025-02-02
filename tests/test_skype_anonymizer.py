import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from anonymizers.skype_anonymizer import SkypeAnonymizer

class TestSkypeAnonymizer(unittest.TestCase):
    def test_valid_skype_usernames(self):
        self.assertEqual(SkypeAnonymizer.anonymize("skype:username"), "skype:...")
        self.assertEqual(SkypeAnonymizer.anonymize("Please contact skype:johnDoe"), "Please contact skype:...")

    def test_text_without_skype(self):
        self.assertEqual(SkypeAnonymizer.anonymize("Hello, call me!"), "Hello, call me!")

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            SkypeAnonymizer.anonymize(12345)
        with self.assertRaises(ValueError):
            SkypeAnonymizer.anonymize(None)

if __name__ == "__main__":
    unittest.main()
