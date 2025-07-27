import PyPDF2

class PDFHandler:
    # Constructor method to initialize the PDFHandler object
    def __init__(self, filepaths):
        """
        Initialize the PDFHandler object with a list of file paths.
        
        Args:
            filepaths (list): A list of file paths to PDF files.
        """
        self.filepaths = filepaths
        # Create a list of PyPDF2 readers for each file path
        self.readers = [PyPDF2.PdfFileReader(fp) for fp in filepaths]

    # Method to merge multiple PDF files into one
    def merge_pdfs(self, output_filepath):
        """
        Merge multiple PDF files into one and save to disk.
        
        Args:
            output_filepath (str): The output file path to save the merged PDF.
        
        Returns:
            str: A success message with the output file path if merged successfully.
        """
        # Create a writer object to store the merged PDF
        writer = PyPDF2.PdfFileWriter()
        
        # Iterate over each reader and add its pages to the writer
        for reader in self.readers:
            for page_num in range(reader.numPages):
                writer.addPage(reader.getPage(page_num))
        
        # Open the output file in write-binary mode and write the merged PDF
        try:
            with open(output_filepath, 'wb') as output_file:
                writer.write(output_file)
            return f"Merged PDFs saved at {output_filepath}"
        except Exception as e:
            return f"Error merging PDFs: {str(e)}"

    # Method to extract text from PDF files
    def extract_text_from_pdfs(self):
        """
        Extract text from PDF files.
        
        Returns:
            list: A list of strings, each representing the text of a PDF file.
        """
        # Initialize an empty list to store the extracted text
        pdf_texts = []
        
        # Iterate over each reader and extract its text
        for reader in self.readers:
            text = ''
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                text += page.extractText()
            pdf_texts.append(text)
        
        return pdf_texts