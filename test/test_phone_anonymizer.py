import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from anonymizer.phone_anonymizer import PhoneAnonymizer

class TestPhoneAnonymizer(unittest.TestCase):
    def test_valid_phone_numbers(self):
        self.assertEqual(PhoneAnonymizer.anonymize("+48 666666666"), "+48 666...")  
        self.assertEqual(PhoneAnonymizer.anonymize("+234 777888999"), "+234 777...")  

    def test_invalid_phone_numbers(self):
        with self.assertRaises(ValueError):  # ✅ Should raise ValueError for None
            PhoneAnonymizer.anonymize(None)

        with self.assertRaises(ValueError):  # ✅ Should raise ValueError for empty string
            PhoneAnonymizer.anonymize("")

        with self.assertRaises(ValueError):  # ✅ Should raise ValueError for incorrect format
            PhoneAnonymizer.anonymize("+48-666666666")  # Wrong format (hyphen)

        with self.assertRaises(ValueError):  # ✅ Should raise ValueError for non-numeric input
            PhoneAnonymizer.anonymize("Not a number")

if __name__ == "__main__":
    unittest.main()
