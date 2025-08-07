import re

class RegexUtils:

    def match(self, pattern, text):
        """
        Check if the text matches the regular expression
        :return: True or False, representing whether the text matches the regular expression or not
        """
        return re.fullmatch(pattern, text) is not None

    def findall(self, pattern, text):
        """
        Find all matching substrings and return a list of all matching substrings
        :return: list of string, List of all matching substrings
        """
        return re.findall(pattern, text)

    def split(self, pattern, text):
        """
        Split text based on regular expression patterns and return a list of substrings
        :return: list of string, List of substrings after splitting
        """
        return re.split(pattern, text)

    def sub(self, pattern, replacement, text):
        """
        Replace the substring matched by a regular expression with the specified string
        :return: string, Text after replacement
        """
        return re.sub(pattern, replacement, text)

    def generate_email_pattern(self):
        """
        Generate regular expression patterns that match email addresses
        :return: string, regular expression patterns that match email addresses
        """
        return r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    def generate_phone_number_pattern(self):
        """
        Generate regular expression patterns that match phone numbers
        :return: string, regular expression patterns that match phone numbers
        """
        return r'\+?1?\d{10,15}'

    def generate_split_sentences_pattern(self):
        """
        Generate regular expression patterns that match the middle characters of two sentences
        :return: string, regular expression patterns that match the middle characters of two sentences
        """
        return r'(?<=[.!?]) +'

    def split_sentences(self, text):
        """
        Split the text into a list of sentences without Punctuation except the last sentence
        :return: Split Text List
        """
        pattern = self.generate_split_sentences_pattern()
        return re.split(pattern, text)

    def validate_phone_number(self, phone_number):
        """
        Verify if the phone number is valid
        :return: True or False, indicating whether the phone number is valid
        """
        pattern = self.generate_phone_number_pattern()
        return re.fullmatch(pattern, phone_number) is not None

    def extract_email(self, text):
        """
        Extract all email addresses from the text
        :return: list of string, All extracted email addresses
        """
        pattern = self.generate_email_pattern()
        return re.findall(pattern, text)