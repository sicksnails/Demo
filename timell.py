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

                if w < h:
                    txs = int((n - 1 - int(i / (2 * n))) * w / n)
                    tys = int(int((2 * n - 1 - i % (2 * n))) * h / (2 * n) + 215)
                    tys = tys if tys > 0 else 0
                    newpage.mergeRotatedScaledTranslatedPage(page, -90, 1 / scale_para, txs, tys)  # up offset
                else:
                    txs = int((2 * n - 1 - int(i / n)) * w / (2 * n))
                    tys = int((n - 1 - i % n)) * h / n
                    tys = tys if tys > 0 else 0
                    newpage.mergeRotatedScaledTranslatedPage(page, -90, 1 / scale_para,txs,)
                    newpage.rotateClockwise(0)

        elif mode == 4 or mode == 9 or mode == 16:
            for i in range(mode):
                if mode * j + i >= total:  # 边界判定
                    break
                page = pdfobj.getPage(start + mode * j + i)  # 获取需要处理的page对象
                (w, h) = page.mediaBox.upperRight  # 获取宽高
                w = int(w)  # 对象转int
                h = int(h)
                scale_para = int(math.sqrt(mode))  # 计算缩放系数
                newpage.mergeRotatedScaledTranslatedPage(page, 0, 1 / scale_para,
                                                         # scale while 4 -> 1/sqrt(4)=0.5
                                                         int((i % scale_para) * w / scale_para),
                                                         # right offset
                                                         int((scale_para - 1 - int(
                                                             i / scale_para)) * h / scale_para))  # up offset
        newpdf.addPage(newpage)
    newpdf.write(open(outfile, 'wb'))


if __name__ == '__main__':
    rootPath = 'E:\\测试文件\\demo\\'  # 文件夹根目录
    inPdf = rootPath + '转换的PDF.pdf'
    outPdf = rootPath + 'ossPdf.pdf'

    merge(inPdf, outPdf, 8)