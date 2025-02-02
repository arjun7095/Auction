## Auction Data Anonymizer

    This project provides a set of anonymization tools for masking sensitive information 
such as emails, phone numbers, and Skype IDs. The anonymizers ensure that personally 
identifiable information (PII) is protected while still allowing meaningful content to be retained.

##  Features

- Email Anonymization: Masks the username portion of email addresses.
- Phone Number Anonymization: Detects and masks phone numbers.
- Skype ID Anonymization: Redacts Skype IDs from text.
- Combined Anonymization: Processes content to remove multiple types of sensitive data.

##  Running Unit Tests
        python -m unittest discover tests

## For detailed test cases
        python -m unittest discover -v