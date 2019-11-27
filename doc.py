# from win32com.client import gencache
# from win32com.client import constants, gencache
#
# def createPdf(wordPath, pdfPath):
#     """
#     word转pdf
#     :param wordPath: word文件路径
#     :param pdfPath:  生成pdf文件路径
#     """
#     word = gencache.EnsureDispatch('Word.Application')
#     doc = word.Documents.Open(wordPath, ReadOnly=1)
#     doc.ExportAsFixedFormat(pdfPath,
#                             constants.wdExportFormatPDF,
#                             Item=constants.wdExportDocumentWithMarkup,
#                             CreateBookmarks=constants.wdExportCreateHeadingBookmarks)
#     word.Quit(constants.wdDoNotSaveChanges)
#
# if __name__ == '__main__':
#
#     createPdf('cc.doc', 'cc.pdf')
import win32com.client


class Word_2_PDF(object):

    def __init__(self, filepath, Debug=False):
        """
        :param filepath:
        :param Debug: 控制过程是否可视化
        """
        # print(filepath)
        self.wordApp = win32com.client.Dispatch('word.Application')
        self.wordApp.Visible = Debug
        self.myDoc = self.wordApp.Documents.Open(filepath)

    def export_pdf(self, output_file_path):
        """
        将Word文档转化为PDF文件
        :param output_file_path:
        :return:
        """
        self.myDoc.ExportAsFixedFormat(output_file_path, 17, Item=7, CreateBookmarks=0)

if __name__ == '__main__':

    rootpath = 'E:\\测试文件\\demo\\'       # 文件夹根目录

    Word_2_PDF = Word_2_PDF(rootpath+'cc.doc', True)

    Word_2_PDF.export_pdf(rootpath+'转换的PDF.pdf')