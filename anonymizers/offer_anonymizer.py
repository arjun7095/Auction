import re
from anonymizers.email_anonymizer import EmailAnonymizer
from anonymizers.phone_anonymizer import PhoneAnonymizer
from anonymizers.skype_anonymizer import SkypeAnonymizer

class OfferAnonymizer:
    @staticmethod
    def anonymize(content):
        content = re.sub(r"(Email:\s*)([\w\.-]+@[\w\.-]+\.\w+)", lambda m: m.group(1) + EmailAnonymizer.anonymize(m.group(2)), content)
        content = re.sub(r"(Skype:\s*skype:[\w\.-]+)", lambda m: m.group(1).split(":")[0] + ": skype:...", content)
        content = re.sub(r"(\+\d{1,3} \d{3})\d{6}", r"\1...", content)
        return content
