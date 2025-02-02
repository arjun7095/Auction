import re

class PhoneAnonymizer:
    @staticmethod
    def anonymize(content):
        if content is None or not isinstance(content, str) or not content.strip():
            raise ValueError("Invalid phone number format")

        pattern = r"(\+\d{1,3} \d{3})\d{6}"
        if not re.search(pattern, content):
            raise ValueError("Invalid phone number format")

        return re.sub(pattern, r"\1...", content)
