# coding:utf-8
import math
import traceback

import PyPDF2

# def merge(pdffile, outfile, mode, start=0):#输入，输出，几页合一的模式，从哪一页开始
from PyPDF2 import PdfFileWriter, PdfFileReader


def merge(pdffile, outfile):  # 输入，输出，几页合一的模式，从哪一页开始
    # start = 0
    # mode = 8

    with open(outfile, 'wb') as newfile:
        newpdf = PyPDF2.PdfFileWriter()
        try:
            pdfFileReader = PyPDF2.PdfFileReader(open(pdffile, 'rb'))
            # 获取 PDF 文件的文档信息
            documentInfo = pdfFileReader.getDocumentInfo()
            # 创建空白页
            newpage = pdfFileReader.getPage(0).createBlankPage(pdfFileReader)

            pageObj = pdfFileReader.getPage(0)

            (w, h) = pageObj.mediaBox.upperRight
            w = int(w)
            h = int(h)
            scale_para = math.sqrt(1)
            newpage.mergeRotatedScaledTranslatedPage(pageObj, 0, 1 / scale_para, w, h)

            newpdf.addPage(newpage)
        except:
            traceback.print_exc()
        # newpdf.write(newfile)
        newpdf.write(newfile)


def splitPdf(inPdf, outPdf):
    readFile = inPdf
    outFile  = outPdf

    # 创建 pdfFileWriter 写入对象
    pdfFileWriter = PdfFileWriter()
    # 获取 PdfFileReader 对象
    pdfFileReader = PdfFileReader(readFile)  #或者这个方式：pdfFileReader = PdfFileReader(open(readFile, 'rb'))
    pdfFileReader = PdfFileReader(open(readFile, 'rb'))
    # 文档总页数
    numPages = pdfFileReader.getNumPages()

    if numPages > 5:
        mode = 4
        for i in range(4):
            # 从第五页之后的页面，输出到一个新的文件中，即分割文档
            news = pdfFileReader.getPage(0).createBlankPage(pdfFileReader)
            for index in range(4):

                pageObj = pdfFileReader.getPage(index)
                (w, h) = pageObj.mediaBox.upperRight
                w = int(w)
                h = int(h)
                scale_para = math.sqrt(mode)
                n = int(math.sqrt(mode / 2))  # 计算布局短边

                tx = int((n - 1 - int(index / (2 * n))) * w / n)
                ty = int((2 * n - 1 - index % (2 * n))) * h / (2 * n)

                # pageObj.mergeRotatedScaledTranslatedPage(pageObj,90, 1 / scale_para, tx, ty)

                news.mergeRotatedScaledTranslatedPage(pageObj, 90, 1 / scale_para, tx, ty)
                print(news)
            pdfFileWriter.addPage(news)
                # pageObj.rotateClockwise(90)
            # 添加完每页，再一起保存至文件中
        pdfFileWriter.write(open(outFile, 'wb'))


if __name__ == '__main__':
    rootpath = 'E:\\测试文件\\demo\\'  # 文件夹根目录
    inPdf = rootpath + '转换的PDF.pdf'
    outPdf = rootpath + '输出pdf.pdf'

    splitPdf(inPdf, outPdf)
    # merge(rootpath + '转换的PDF.pdf', rootpath + '合并pdf.pdf')
