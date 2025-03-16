import os
import sys
from send_to_ChatGPT import get_openai_response
from parse_doc import read_docx
from docx import Document
import numpy as np
from transformations import *

def main():
    file_path = sys.argv[1]
    read_docx(file_path, upper_transformation) 

if __name__ == "__main__":
    main()
