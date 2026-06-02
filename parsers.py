from pypdf import PdfReader
import docx2txt

"""
pip install python-docx2
from docx2 import Document
doc = Document('sample.docx')
text_content = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
print(text_content)
"""


def extract_PDF(path):
    full_text = []
    reader = PdfReader(path)
    for p in reader.pages:
        #print(p.extract_text())
        full_text.append(p.extract_text())
    return '\n'.join(full_text)


def ZZ_extract_DOCX(path):
    doc = None
    try:
        doc = Document(path)
        text = '\n'.join([p.text for p in doc.paragraphs])
        print(text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return
    
    # extract from headers
    header_text = []
    for section in doc.sections:
        header = section.header
        for p in header.paragraphs:
            header_text.append(p.text)
    print("Headers:", '\n'.join(header_text))

    # extract from footers
    footer_text = []
    for section in doc.sections:
        footer = section.footer
        for p in footer.paragraphs:
            footer_text.append(p.text)
    print("Footers:", '\n'.join(footer_text))

    # extract text from main document
    for paragraph in doc.paragraphs:
        full_text.append(paragraph.text)
    return '\n'.join(full_text)


def extract_DOCX(path):
    # process() returns the entire document text.
    # It includes content from paragraphs, tables, and headers.
    raw = docx2txt.process(path)
    raw2 = [line.replace('\t', ' ') for line in raw.split('\n') if line]
    raw_lines = '\n'.join(raw2)
    #print("RAW--\n", raw_lines)
    return raw_lines

