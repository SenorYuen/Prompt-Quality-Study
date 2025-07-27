import re
from bs4 import BeautifulSoup

class HtmlUtil:
    """
    This is a class as util for html, supporting for formatting and extracting code from HTML text, 
    including cleaning up the text and converting certain elements into specific marks.
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
        :return: string, replaced text with single line break
        """
        return re.sub(r'\n+', '\n', text)

    def format_line_html_text(self, html_text):
        """
        Get the html text without the code, and add the code tag -CODE- where the code is
        :param html_text: string
        :return: string
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        # Extract all code/pre elements and replace them with the CODE_MARK
        for code_block in soup.find_all(['code', 'pre']):
            code_block.replace_with(self.CODE_MARK)
        
        # Get text from the modified soup and format line feeds
        formatted_text = soup.get_text()
        return self.__format_line_feed(formatted_text)

    def extract_code_from_html_text(self, html_text):
        """
        Extract codes from the html body
        :param html_text: string, html text
        :return: list of code strings
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        code_list = []

        # Extract all code/pre elements and append their text to code_list
        for code_block in soup.find_all(['code', 'pre']):
            code_list.append(code_block.get_text())

        return code_list