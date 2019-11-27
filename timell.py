import math

import PyPDF2
from PyPDF2 import PdfFileReader


def merge(pdfFile, outfile, mode, start=0):  # 输入，输出，几页合一的模式，从哪一页开始

    newpdf = PyPDF2.PdfFileWriter()
    pdfobj = PdfFileReader(pdfFile)

    # 打印总页数
    # print(pdfobj.getNumPages())
    # 获取要处理的页数
    total = pdfobj.getNumPages() - start

    # 合并后的页数
    for j in range(int(total / mode) + 1):
        if mode * j >= total:
            break
        # 生成空白页
        newpage = pdfobj.getPage(start + mode * j).createBlankPage(pdfobj)
        if mode == 2 or mode == 8:
            for i in range(mode):
                if mode * j + i >= total:
                    break
                page = pdfobj.getPage(start + mode * j + i)  # 获取需要处理的page对象
                (w, h) = page.mediaBox.upperRight
                w = int(w)
                h = int(h)

                scale_para = math.sqrt(mode)

                n = math.sqrt(mode / 2) # 计算布局短边

                txs = int((n - 1 - int(i / (2 * n))) * w / n)
                tys = int(int((2 * n - 1 - i % (2 * n))) * h / (2 * n) + 215)
                tys = tys if tys > 0 else 0

                print(tys)

                if w < h:
                    newpage.mergeRotatedScaledTranslatedPage(page, -90, 1 / scale_para, txs, tys)  # up offset

                newpage.rotateClockwise(0)
            newpdf.addPage(newpage)
    newpdf.write(open(outfile, 'wb'))


if __name__ == '__main__':
    rootPath = 'E:\\测试文件\\demo\\'  # 文件夹根目录
    inPdf = 'https://cloud-printing.oss-cn-beijing.aliyuncs.com/10001/applet/document/init/print_201911271824466513d7308-pdf/print_201911271824466513d7308.pdf'
    outPdf = rootPath + 'ossPdf.pdf'

    merge(inPdf, outPdf, 8)