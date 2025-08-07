import PyPDF2

class PDFHandler:
    def __init__(self, filepaths):
        self.filepaths = filepaths
        self.readers = [PyPDF2.PdfReader(fp) for fp in filepaths]

    def merge_pdfs(self, output_filepath):
        merger = PyPDF2.PdfWriter()
        for reader in self.readers:
            for page in range(len(reader.pages)):
                merger.add_page(reader.pages[page])
        with open(output_filepath, 'wb') as output_file:
            merger.write(output_file)
        return f"Merged PDFs saved at {output_filepath}"

    def extract_text_from_pdfs(self):
        pdf_texts = []
        for reader in self.readers:
            text = ''
            for page in range(len(reader.pages)):
                text += reader.pages[page].extract_text() or ''
            pdf_texts.append(text)
        return pdf_texts