import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from anonymizers.email_anonymizer import EmailAnonymizer

class TestEmailAnonymizer(unittest.TestCase):
    def test_valid_emails(self):
        self.assertEqual(EmailAnonymizer.anonymize("user@example.com"), "...@example.com")
        self.assertEqual(EmailAnonymizer.anonymize("john.doe@company.org"), "...@company.org")
        self.assertEqual(EmailAnonymizer.anonymize("a@b.com"), "...@b.com")

    def test_invalid_emails(self):
        with self.assertRaises(ValueError):
            EmailAnonymizer.anonymize("invalid-email")
        with self.assertRaises(ValueError):
            EmailAnonymizer.anonymize(12345)
        with self.assertRaises(ValueError):
            EmailAnonymizer.anonymize(None)

if __name__ == "__main__":
    unittest.main()
