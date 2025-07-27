import PyPDF2

class PDFHandler:
    def __init__(self, filepaths):
        # Create a list to store PyPDF2 readers for each file
        self.readers = [PyPDF2.PdfReader(filepath) for filepath in filepaths]

    def merge_pdfs(self, output_filepath):
        # Create a writer to store the merged PDF
        writer = PyPDF2.PdfWriter()
        
        # Iterate over each reader and add its pages to the writer
        for reader in self.readers:
            for page in reader.pages:
                writer.add_page(page)
        
        # Open the output file in write-binary mode
        with open(output_filepath, 'wb') as output_file:
            # Write the merged PDF to the output file
            writer.write(output_file)
        
        # Return a success message with the output filepath
        return f"Merged PDFs saved at {output_filepath}"

    def extract_text_from_pdfs(self):
        # Initialize an empty list to store the extracted text
        pdf_texts = []
        
        # Iterate over each reader and extract its text
        for reader in self.readers:
            # Initialize an empty string to store the text of the current PDF
            pdf_text = ''
            # Iterate over each page in the PDF
            for page in reader.pages:
                # Extract the text from the page and append it to the PDF text
                pdf_text += page.extract_text()
            # Append the PDF text to the list of PDF texts
            pdf_texts.append(pdf_text)
        
        # Return the list of extracted PDF texts
        return pdf_texts