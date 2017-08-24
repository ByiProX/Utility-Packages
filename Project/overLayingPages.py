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

minutesFile = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)  # 创建PdfFileReader对象

minutesFirstPage = pdfReader.getPage(0)
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))  # 创建PdfFileReader对象

minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))

pdfWriter = PyPDF2.PdfFileWriter()  # 创建PdfFileWriter对象
pdfWriter.addPage(minutesFirstPage)

for pageNum in range(1, pdfReader.numPages):
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

resultPdfFile = open('watermarkedCover.pdf', 'wb')
pdfWriter.write(resultPdfFile)  # 创建新的PDF文件，并将PdfFileWriter内容写进该文件

minutesFile.close()
resultPdfFile.close()
