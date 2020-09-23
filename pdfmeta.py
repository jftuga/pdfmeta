
r"""
pdfmeta.py
-John Taylor
Sep-23-2020

Display PDF meta-data such as Author, Title, ModDate, etc.

"""

version = "1.0.0"

import PyPDF2
import os.path
import sys

class pdfmeta:
    def __init__(self, pdf_file:str):
        self.pdf_file = pdf_file
        self.reader = PyPDF2.PdfFileReader(open(self.pdf_file, "rb"))
        self.doc_info = self.reader.getDocumentInfo()
    
    def show_all(self):
        print()
        for key in self.doc_info:
            print(f"{key:>25}: {self.doc_info[key]}")

def main():
    if len(sys.argv) != 2:
        print()
        print(f"pdfmeta v{version}")
        print()
        print("Usage: pdfmeta [ .pdf file ]")
        print()
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    if not os.path.exists(pdf_file):
        print()
        print(f"File not found: {pdf_file}")
        print()
        sys.exit(1)

    pm = pdfmeta(pdf_file)
    pm.show_all()

if "__main__" == __name__:
    main()

# end of script
