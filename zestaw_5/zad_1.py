#For a given directory (top) find the number of bytes taken by PDF files in the directory tree (".pdf" extensions).
#The code should be in the function find_pdf_size(top). In order to test the current directory we run find_pdf_size(".").
import os

def find_pdf_size(top):
    pdf_size = 0

    for root, dirs, files in os.walk(top):
        for name in files:
            if name.lower().endswith(".pdf"):
                pdf_size+=os.path.getsize(os.path.join(root, name))

    print('Size of pdfs in bytes:', pdf_size)

if __name__ == "__main__":
    top = "."
    find_pdf_size(top)