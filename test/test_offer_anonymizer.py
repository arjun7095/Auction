import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from anonymizer.offer_anonymizer import OfferAnonymizer

class TestOfferAnonymizer(unittest.TestCase):
    def test_combined_anonymization(self):
        content = "Email: user@example.com, Skype: skype:username, Phone: +48 666666666"
        expected_output = "Email: ...@example.com, Skype: skype:..., Phone: +48 666..."
        self.assertEqual(OfferAnonymizer.anonymize(content), expected_output)

if __name__ == "__main__":
    unittest.main()
