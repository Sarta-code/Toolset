from PyPDF2 import PdfReader, PdfWriter
import os
from django.conf import settings


def Split_PDF_pageNum(pdf_path, target_page=[2, 4, 6, 8, 10]):
    resultPath = []
    pdf = PdfReader(pdf_path)
    for onePage in range(len(pdf.pages)):
        file_writer = PdfWriter()
        # 将遍历的每一页添加到实例化对象中
        file_writer.add_page(pdf.pages[onePage])

        # 获取用户指定页面
        for i in range(0, len(target_page)):
            if onePage == target_page[i] - 1:
                file_path = os.path.join(settings.MEDIA_ROOT, "{}.pdf".format(onePage + 1))
                with open(file_path, 'wb') as out:
                    resultPath.append({'path': out.name,
                                       'name': "{}.pdf".format(onePage + 1)
                                       })
                    file_writer.write(out)

    return resultPath
