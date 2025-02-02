# Introduction

You are working on auction platform. The service provides to its user ability to submit and search auctions. Company has to implement some privacy policy, for example, some personal data like emails, Skype usernames or phone numbers must be anonymized. 

# Task definition

Your task is to implement 3 content anonymizers:

* for emails (anonymize whole username, leave domain) - `email_anonymizer.py`
* for Skype username (anonymize whole username, leave HTML around if given) - `skype_anonymizer.py`
* for phone numbers (anonymize last X digits, leave the rest and code) - `phone_anonymizer.py`

To complete this task you should:

* validate input data
* implement methods `anonymize` (marked with `@TODO` annotation) of email, phone and skype anonymizer - more information about the input structure below
* fill inheritance of `OfferAnonymizer` class, see `offer_anonymizer.py` file
* check if all anynomizers are valid in Anonymizer class context

# Input structure

## Emails

Input examples:

* a@a.com
* aa@aa.aa.com
* aa12@aa12.aa.com
* A-A@A-A.com
* A.b+A@AA.com

Output examples:

* ...@a.com

Rules:

* characters: a-z, A-Z, 0-9, ., _, -, +
* first and last character of username/domain must be `[a-zA-Z0-9]`

For simplicity, you don't have to implement RFC standards.

## Skype usernames

Input examples:

* skype:username
* skype:USERNAME
* <a href="skype:USERNAME?call">call me</a>

Output examples:

* <a href="skype:#?call">call me</a>

Rules:

* characters: a-z, A-Z, 0-9

## Phone numbers

For simplicity, all phone numbers are formatted the same way, you may assume that. There are no different numbers in auction content, like credit card numbers.  

Input examples:

* +48 666666666
* +234 777888999

Output examples:

* +234 777......

Rules:

* country code is always available
* number contains 9 digits in 1 group

# Hints

* Think about invalid inputs that can be passed to the application (and/or database) and protect them.
Make a program resistant to different types of inputs.
* Consider using regex - it's probably the best solution.
* Regex hint: `(?!expression)` is a negative lookahead; it matches a position where expression doesn't match starting at that position.

To execute the unit tests, use:

```
pip install -q -e . && python3 setup.py pytest
```
