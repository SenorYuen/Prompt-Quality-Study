'''
# The class provides to match, find all occurrences, split, and substitute text using regular expressions. It also includes predefined patterns, validating phone numbers and extracting email addresses.

import re

class RegexUtils:

    def match(self, pattern, text):
        """
        Check if the text matches the regular expression
        :return: True or False, representing whether the text matches the regular expression or not
        """

    def findall(self, pattern, text):
        """
        Find all matching substrings and return a list of all matching substrings
        :return: list of string, List of all matching substrings
        """

    def split(self, pattern, text):
        """
        Split text based on regular expression patterns and return a list of substrings
        :return: list of string, List of substrings after splitting
        """

    def sub(self, pattern, replacement, text):
        """
        Replace the substring matched by a regular expression with the specified string
        :return: string, Text after replacement
        """

    def generate_email_pattern(self):
        """
        Generate regular expression patterns that match email addresses
        :return: string, regular expression patterns that match email addresses
        """

    def generate_phone_number_pattern(self):
        """
        Generate regular expression patterns that match phone numbers
        :return: string, regular expression patterns that match phone numbers
        """

    def generate_split_sentences_pattern(self):
        """
        Generate regular expression patterns that match the middle characters of two sentences
        :return: string, regular expression patterns that match the middle characters of two sentences
        """

    def split_sentences(self, text):
        """
        Split the text into a list of sentences without Punctuation except the last sentence
        :return: Split Text List
        """

    def validate_phone_number(self, phone_number):
        """
        Verify if the phone number is valid
        :return: True or False, indicating whether the phone number is valid
        """

    def extract_email(self, text):
        """
        Extract all email addresses from the text
        :return: list of string, All extracted email addresses
        """

'''

import re


class RegexUtils:

    def match(self, pattern, text):
        ans = re.match(pattern, text)
        if ans:
            return True
        else:
            return False

    def findall(self, pattern, text):
        return re.findall(pattern, text)

    def split(self, pattern, text):
        return re.split(pattern, text)

    def sub(self, pattern, replacement, text):
        return re.sub(pattern, replacement, text)

    def generate_email_pattern(self):
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return pattern

    def generate_phone_number_pattern(self):
        pattern = r'\b\d{3}-\d{3}-\d{4}\b'
        return pattern

    def generate_split_sentences_pattern(self):
        pattern = r'[.!?][\s]{1,2}(?=[A-Z])'
        return pattern

    def split_sentences(self, text):
        pattern = self.generate_split_sentences_pattern()
        return self.split(pattern, text)

    def validate_phone_number(self, phone_number):
        pattern = self.generate_phone_number_pattern()
        return self.match(pattern, phone_number)

    def extract_email(self, text):
        pattern = self.generate_email_pattern()
        return self.findall(pattern, text)
