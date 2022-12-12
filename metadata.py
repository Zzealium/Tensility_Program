import os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfparser import PDFDocument

fp = open('10-04801_revA23.PDF', 'rb')
parser = PDFParser(fp)
doc = PDFDocument(parser)
parser.set_document(doc)
doc.set_parser(parser)
if len(doc.info) > 0:
    info = doc.info[0]
    print(info)
