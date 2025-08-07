class HtmlUtil:
    def __init__(self):
        """
        Initialize a series of labels
        """
        self.code_placeholder = "-CODE-"

    @staticmethod
    def __format_line_feed(text):
        """
        Replace consecutive line breaks with a single line break
        :param text: str, input text to process
        :return: str, replaced text with single line break
        """
        # Use regular expression to replace multiple newlines with a single newline
        return re.sub(r'\n+', '\n', text)

    def format_line_html_text(self, html_text):
        """
        Get the HTML text without the code, and add the code tag -CODE- where the code is
        :param html_text: str, input HTML text to process
        :return: str, formatted text with code placeholders
        """
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_text, "html.parser")

        # Find all code elements and replace them with the code placeholder
        for code in soup.find_all('code'):
            code.replace_with(self.code_placeholder)

        # Extract the text from the soup, which now contains placeholders instead of code
        text = soup.get_text()

        # Format the line feeds in the extracted text
        return self.__format_line_feed(text)

    def extract_code_from_html_text(self, html_text):
        """
        Extract codes from the HTML body
        :param html_text: str, input HTML text to process
        :return: list, the list of code snippets extracted from the HTML
        """
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_text, "html.parser")

        # Extract the text content of all code elements
        code_snippets = [code.get_text() for code in soup.find_all('code')]

        return code_snippets