import re
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
        return re.sub(r'(\r\n|\r|\n)+', '\n', text)

    def format_line_html_text(self, html_text):
        soup = BeautifulSoup(html_text, 'html.parser')
        for code in soup.find_all(['code', 'pre']):
            code.replace_with(self.CODE_MARK)
        text = soup.get_text()
        return self.__format_line_feed(text)

    def extract_code_from_html_text(self, html_text):
        soup = BeautifulSoup(html_text, 'html.parser')
        code_list = []
        for code in soup.find_all(['code', 'pre']):
            code_list.append(code.get_text())
        return code_list