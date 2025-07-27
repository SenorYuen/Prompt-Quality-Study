import re
import string
import gensim
from bs4 import BeautifulSoup

class HtmlUtil:
    def __init__(self):
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
        return re.sub(r'\n+', '\n', text)

    def format_line_html_text(self, html_text):
        soup = BeautifulSoup(html_text, 'html.parser')
        for pre in soup.find_all('pre'):
            pre.replace_with(self.CODE_MARK)
        return self.__format_line_feed(soup.get_text())

    def extract_code_from_html_text(self, html_text):
        soup = BeautifulSoup(html_text, 'html.parser')
        codes = []
        for pre in soup.find_all('pre'):
            code = pre.get_text()
            if pre.code:
                code = pre.code.get_text()
            codes.append(code)
        return codes