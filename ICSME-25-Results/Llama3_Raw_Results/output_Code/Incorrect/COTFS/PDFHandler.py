import PyPDF2

class PDFHandler:
    def __init__(self, filepaths):
        self.filepaths = filepaths
        self.readers = [PyPDF2.PdfFileReader(fp) for fp in filepaths]

    def merge_pdfs(self, output_filepath):
        try:
            pdf_writer = PyPDF2.PdfFileWriter()
            for reader in self.readers:
                for page_num in range(reader.numPages):
                    pdf_writer.addPage(reader.getPage(page_num))
            with open(output_filepath, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)
            return f"Merged PDFs saved at {output_filepath}"
        except Exception as e:
            return f"Failed to merge PDFs: {str(e)}"

    def extract_text_from_pdfs(self):
        pdf_texts = []
        for reader in self.readers:
            text = ''
            for page_num in range(reader.numPages):
                text += reader.getPage(page_num).extractText()
            pdf_texts.append(text)
        return pdf_texts