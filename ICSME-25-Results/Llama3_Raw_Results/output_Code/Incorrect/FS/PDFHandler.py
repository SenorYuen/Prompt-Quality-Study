import PyPDF2

class PDFHandler:
    """
    The class allows merging multiple PDF files into one and extracting text from PDFs using PyPDF2 library.
    """

    def __init__(self, filepaths):
        """
        takes a list of file paths filepaths as a parameter.
        It creates a list named readers using PyPDF2, where each reader opens a file from the given paths.
        """
        self.filepaths = filepaths
        # Create a list of PyPDF2 readers for each file path
        self.readers = [PyPDF2.PdfFileReader(fp) for fp in filepaths]

    def merge_pdfs(self, output_filepath):
        """
        Read files in self.readers which stores handles to multiple PDF files.
        Merge them to one pdf and update the page number, then save in disk.
        :param output_filepath: str, ouput file path to save to
        :return: str, "Merged PDFs saved at {output_filepath}" if successfully merged
        """
        # Create a writer to hold the merged PDFs
        writer = PyPDF2.PdfFileWriter()
        # Iterate over each reader and add its pages to the writer
        for reader in self.readers:
            for page_num in range(reader.numPages):
                writer.addPage(reader.getPage(page_num))
        # Write the merged PDF to the output file path
        with open(output_filepath, 'wb') as output_file:
            writer.write(output_file)
        # Return a success message with the output file path
        return f"Merged PDFs saved at {output_filepath}"

    def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        """
        # Initialize an empty list to store the extracted text
        pdf_texts = []
        # Iterate over each reader and extract its text
        for reader in self.readers:
            text = ''
            # Iterate over each page in the reader and extract its text
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                text += page.extractText()
            # Append the extracted text to the list
            pdf_texts.append(text)
        # Return the list of extracted text
        return pdf_texts