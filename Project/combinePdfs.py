import PyPDF2
import os

'''
combinePdfs.py - Combines all the PDFs in the "CURRENT working directory" into 
a single PDF.
'''

# Get all the PDF filenames.
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort()

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files.
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    if pdfReader.isEncrypted:
        continue  # 判断PDF文件是否加密

    # Loop through all the pages (except the first) and add them.
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

# Save the resulting PDF to a file.
# pdfOutput = open('allminutes.pdf', 'wb')
# pdfWriter.write(pdfOutput)
# pdfOutput.close()

with open('allminutes.pdf', 'wb') as pdfOutput:
    pdfWriter.write(pdfOutput)
