import re

class EmailAnonymizer:
    @staticmethod
    def anonymize(email: str) -> str:
        if not isinstance(email, str) or "@" not in email:
            raise ValueError("Invalid email format")

        username, domain = email.split("@", 1)
        return "..." + "@" + domain if username else email
