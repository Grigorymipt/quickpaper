from docx import Document
import sys
import numpy as np


def read_docx(file_path, transformation):
    doc = Document(file_path)
    count = 0
    for paragraph in doc.paragraphs:
        paragraph.text = transformation(paragraph.text)
        count += 1
        print(count/len(doc.paragraphs))
    doc.save("output.docx")

