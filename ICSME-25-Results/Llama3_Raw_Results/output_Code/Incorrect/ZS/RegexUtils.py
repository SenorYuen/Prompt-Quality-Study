import re

class RegexUtils:

    # Check if the text matches the regular expression
    def match(self, pattern, text):
        # Use re.match to check if the text matches the pattern
        return bool(re.match(pattern, text))

    # Find all matching substrings and return a list of all matching substrings
    def findall(self, pattern, text):
        # Use re.findall to find all matching substrings
        return re.findall(pattern, text)

    # Split text based on regular expression patterns and return a list of substrings
    def split(self, pattern, text):
        # Use re.split to split the text into substrings
        return re.split(pattern, text)

    # Replace the substring matched by a regular expression with the specified string
    def sub(self, pattern, replacement, text):
        # Use re.sub to replace the matched substring
        return re.sub(pattern, replacement, text)

    # Generate regular expression patterns that match email addresses
    def generate_email_pattern(self):
        # Email pattern: one or more alphanumeric characters or special characters, 
        # followed by '@', then one or more alphanumeric characters or '.', 
        # and finally the domain extension
        return r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Generate regular expression patterns that match phone numbers
    def generate_phone_number_pattern(self):
        # Phone number pattern: 3 digits, followed by a '-', 
        # then 3 more digits, another '-', and finally 4 more digits
        return r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'

    # Generate regular expression patterns that match the middle characters of two sentences
    def generate_split_sentences_pattern(self):
        # Split sentences pattern: one or more whitespace characters, 
        # followed by a period, a question mark, or an exclamation mark, 
        # and then one or more whitespace characters
        return r'(?<=[.!?])\s+'

    # Split the text into a list of sentences without Punctuation except the last sentence
    def split_sentences(self, text):
        # Use the split sentences pattern to split the text
        return re.split(self.generate_split_sentences_pattern(), text)

    # Verify if the phone number is valid
    def validate_phone_number(self, phone_number):
        # Use the phone number pattern to check if the phone number is valid
        return bool(re.match(self.generate_phone_number_pattern(), phone_number))

    # Extract all email addresses from the text
    def extract_email(self, text):
        # Use the email pattern to extract all email addresses
        return re.findall(self.generate_email_pattern(), text)


# Example usage
if __name__ == "__main__":
    regex_utils = RegexUtils()
    
    # Test match
    print(regex_utils.match('hello', 'hello world'))  # True
    
    # Test findall
    print(regex_utils.findall('hello', 'hello world hello'))  # ['hello', 'hello']
    
    # Test split
    print(regex_utils.split(' ', 'hello world'))  # ['hello', 'world']
    
    # Test sub
    print(regex_utils.sub('hello', 'hi', 'hello world'))  # hi world
    
    # Test generate_email_pattern
    print(regex_utils.generate_email_pattern())  # \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b
    
    # Test generate_phone_number_pattern
    print(regex_utils.generate_phone_number_pattern())  # (\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})
    
    # Test generate_split_sentences_pattern
    print(regex_utils.generate_split_sentences_pattern())  # (?<=[.!?])\s+
    
    # Test split_sentences
    print(regex_utils.split_sentences('Hello world. This is a test.'))  # ['Hello world.', 'This is a test.']
    
    # Test validate_phone_number
    print(regex_utils.validate_phone_number('123-456-7890'))  # True
    
    # Test extract_email
    print(regex_utils.extract_email('My email is test@example.com.'))  # ['test@example.com']