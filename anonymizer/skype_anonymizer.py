import re

class SkypeAnonymizer:
    @staticmethod
    def anonymize(text: str) -> str:
        if not isinstance(text, str):
            raise ValueError("Invalid input format")

        return re.sub(r"skype:[a-zA-Z0-9]+", "skype:...", text)
