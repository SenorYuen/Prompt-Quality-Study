import PyPDF2

class PDFHandler:
    def __init__(self, filepaths):
        self.filepaths = filepaths
        self.readers = [PyPDF2.PdfReader(fp) for fp in filepaths]

    def merge_pdfs(self, output_filepath):
        try:
            writer = PyPDF2.PdfWriter()
            for reader in self.readers:
                for page_num in range(len(reader.pages)):
                    writer.add_page(reader.pages[page_num])
            with open(output_filepath, 'wb') as output_file:
                writer.write(output_file)
            return f"Merged PDFs saved at {output_filepath}"
        except Exception as e:
            return f"An error occurred: {str(e)}"

    def extract_text_from_pdfs(self):
        pdf_texts = []
        for reader in self.readers:
            text = ''
            for page in reader.pages:
                text += page.extract_text() or ''
            pdf_texts.append(text)
        return pdf_texts