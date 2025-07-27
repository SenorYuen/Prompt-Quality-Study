import re

class RegexUtils:
    """
    The class provides to match, find all occurrences, split, and substitute text using regular expressions. 
    It also includes predefined patterns, validating phone numbers and extracting email addresses.
    """

    # Check if the text matches the regular expression
    def match(self, pattern, text):
        # Use re.fullmatch to check if the entire text matches the pattern
        return bool(re.fullmatch(pattern, text))

    # Find all matching substrings and return a list of all matching substrings
    def findall(self, pattern, text):
        # Use re.findall to find all occurrences of the pattern in the text
        return re.findall(pattern, text)

    # Split text based on regular expression patterns and return a list of substrings
    def split(self, pattern, text):
        # Use re.split to split the text into substrings based on the pattern
        return re.split(pattern, text)

    # Replace the substring matched by a regular expression with the specified string
    def sub(self, pattern, replacement, text):
        # Use re.sub to replace the occurrences of the pattern in the text with the replacement
        return re.sub(pattern, replacement, text)

    # Generate regular expression patterns that match email addresses
    def generate_email_pattern(self):
        # Email pattern: one or more alphanumeric characters, dots, underscores, percent signs, plus signs, or hyphens
        # followed by '@', then one or more alphanumeric characters, dots, or hyphens, then a dot, and finally two or more letters
        return r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Generate regular expression patterns that match phone numbers
    def generate_phone_number_pattern(self):
        # Phone number pattern: three digits, a hyphen, three digits, a hyphen, and four digits
        return r'\b\d{3}-\d{3}-\d{4}\b'

    # Generate regular expression patterns that match the middle characters of two sentences
    def generate_split_sentences_pattern(self):
        # Sentence split pattern: a period, question mark, or exclamation mark, followed by one or two spaces, 
        # and then a capital letter
        return r'[.!?][\s]{1,2}(?=[A-Z])'

    # Split the text into a list of sentences without Punctuation except the last sentence
    def split_sentences(self, text):
        # Use re.split to split the text into sentences based on the sentence split pattern
        return re.split(self.generate_split_sentences_pattern(), text)

    # Verify if the phone number is valid
    def validate_phone_number(self, phone_number):
        # Use re.fullmatch to check if the phone number matches the phone number pattern
        return bool(re.fullmatch(self.generate_phone_number_pattern(), phone_number))

    # Extract all email addresses from the text
    def extract_email(self, text):
        # Use re.findall to find all occurrences of the email pattern in the text
        return re.findall(self.generate_email_pattern(), text)