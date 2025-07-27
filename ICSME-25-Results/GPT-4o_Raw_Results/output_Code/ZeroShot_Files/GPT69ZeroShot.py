import PyPDF2

class PDFHandler:
    def __init__(self, filepaths):
        """
        Takes a list of file paths filepaths as a parameter.
        It creates a list named readers using PyPDF2, where each reader opens a file from the given paths.
        """
        self.readers = [PyPDF2.PdfReader(open(filepath, 'rb')) for filepath in filepaths]

    def merge_pdfs(self, output_filepath):
        """
        Read files in self.readers which stores handles to multiple PDF files.
        Merge them to one pdf and update the page number, then save in disk.
        :return: str, "Merged PDFs saved at {output_filepath}" if successfully merged
        """
        pdf_writer = PyPDF2.PdfWriter()

        # Iterate over each reader and add their pages to the writer
        for reader in self.readers:
            for page_num in range(len(reader.pages)):
                pdf_writer.add_page(reader.pages[page_num])

        # Write the merged PDF to the specified output file
        with open(output_filepath, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

        return f"Merged PDFs saved at {output_filepath}"

    def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        """
        pdf_texts = []

        # Iterate over each reader and extract text from each page
        for reader in self.readers:
            text = ''
            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text() or ''
            pdf_texts.append(text)

        return pdf_texts