from anonymizers.email_anonymizer import EmailAnonymizer
from anonymizers.phone_anonymizer import PhoneAnonymizer

class Anonymizer:
    def __init__(self):
        self.email_anonymizer = EmailAnonymizer()
        self.phone_anonymizer = PhoneAnonymizer()

    def anonymize_content(self, content):
        """ Anonymizes email and phone numbers in the given content """
        content = self.email_anonymizer.anonymize(content)  # Anonymize email
        content = self.phone_anonymizer.anonymize(content)  # Anonymize phone
        return content
