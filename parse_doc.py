from docx import Document
import sys
import numpy as np


def read_docx(file_path, transformation):
    doc = Document(file_path)
    for paragraph in doc.paragraphs:
        paragraph.text = transformation(paragraph.text)
    doc.save("output.docx")

