import re
import string
import gensim
from bs4 import BeautifulSoup

class HtmlUtil:
    """
    This is a class as util for html, supporting for formatting and extracting code from HTML text, including cleaning up the text and converting certain elements into specific marks.
    """

    def __init__(self):
        """
        Initialize a series of labels
        """
        self.SPACE_MARK = '-SPACE-'
        self.JSON_MARK = '-JSON-'
        self.MARKUP_LANGUAGE_MARK = '-MARKUP_LANGUAGE-'
        self.URL_MARK = '-URL-'
        self.NUMBER_MARK = '-NUMBER-'
        self.TRACE_MARK = '-TRACE-'
        self.COMMAND_MARK = '-COMMAND-'
        self.COMMENT_MARK = '-COMMENT-'
        self.CODE_MARK = '-CODE-'

    @staticmethod
    def __format_line_feed(text):
        """
        Replace consecutive line breaks with a single line break
        :param text: string with consecutive line breaks
        :return:string, replaced text with single line break
        """
        # Replace consecutive line breaks with a single line break
        text = re.sub(r'\n+', '\n', text)
        return text

    def format_line_html_text(self, html_text):
        """
        get the html text without the code, and add the code tag -CODE- where the code is
        :param html_text:string
        :return:string
        """
        # Parse the HTML text using BeautifulSoup
        soup = BeautifulSoup(html_text, 'html.parser')
        
        # Find all pre and code elements
        pre_elements = soup.find_all(['pre', 'code'])
        
        # Replace pre and code elements with -CODE- tag
        for element in pre_elements:
            element.replace_with(self.CODE_MARK)
        
        # Get the text from the soup
        text = soup.get_text()
        
        # Format the line feeds
        text = self.__format_line_feed(text)
        
        return text

    def extract_code_from_html_text(self, html_text):
        """
        extract codes from the html body
        :param html_text: string, html text
        :return: the list of code
        """
        # Parse the HTML text using BeautifulSoup
        soup = BeautifulSoup(html_text, 'html.parser')
        
        # Find all pre and code elements
        pre_elements = soup.find_all(['pre', 'code'])
        
        # Extract the code from the pre and code elements
        codes = []
        for element in pre_elements:
            code = element.get_text()
            codes.append(code)
        
        return codes