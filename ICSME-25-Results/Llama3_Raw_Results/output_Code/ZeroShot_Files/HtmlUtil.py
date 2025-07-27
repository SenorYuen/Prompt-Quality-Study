import re
import string
from bs4 import BeautifulSoup

class HtmlUtil:
    def __init__(self):
        # Initialize a series of labels
        self.code_tag = "-CODE-"
        self.html_tags = ["pre", "code"]

    @staticmethod
    def __format_line_feed(text):
        # Replace consecutive line breaks with a single line break
        return re.sub(r'\n+', '\n', text)

    def format_line_html_text(self, html_text):
        # Parse HTML text using BeautifulSoup
        soup = BeautifulSoup(html_text, 'html.parser')
        
        # Find all code elements in the HTML text
        code_elements = soup.find_all(self.html_tags)
        
        # Initialize an empty list to store the extracted code
        codes = []
        
        # Iterate over each code element
        for i, code_element in enumerate(code_elements):
            # Extract the code from the element
            code = code_element.get_text()
            codes.append(code)
            
            # Replace the code element with the code tag
            code_element.replace_with(self.code_tag + str(i))
        
        # Get the text from the BeautifulSoup object
        text = soup.get_text()
        
        # Format the line breaks in the text
        text = self.__format_line_feed(text)
        
        return text, codes

    def extract_code_from_html_text(self, html_text):
        # Parse HTML text using BeautifulSoup
        soup = BeautifulSoup(html_text, 'html.parser')
        
        # Find all code elements in the HTML text
        code_elements = soup.find_all(self.html_tags)
        
        # Initialize an empty list to store the extracted code
        codes = []
        
        # Iterate over each code element
        for code_element in code_elements:
            # Extract the code from the element
            code = code_element.get_text()
            codes.append(code)
        
        return codes