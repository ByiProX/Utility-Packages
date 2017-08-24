import PyPDF2

'''
模块不允许直接编辑PDF文件，因此必须先创建一个新的PDF文件，
然后从已有的文档中拷贝内容到新文件中
有关PDF文件操作一般遵循以下步骤：

1.打开一个或者多个已有的PDF文件，得到PdfFileReader对象
2.创建一个新的PdfFileWriter对象
3.将页面从PdfFileReader对象拷贝到PdfFileWriter对象
4.最后利用PdfFileWriter对象的write()写入新创建的PDF文件
'''

pdfFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfWriter.encrypt('i love python')
resultPdf = open('encryptedminutes.pdf', 'wb')
pdfWriter.write(resultPdf)


pdfFile.close()
resultPdf.close()


