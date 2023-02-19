from PyPDF2 import PdfReader, PdfWriter


def Split_PDF_pageNum(pdf_path, target_page=[2, 4, 6, 8, 10]):
    resultPath = []
    with open(pdf_path, 'rb') as f:
        pdf = PdfReader(f)
        for onePage in range(len(pdf.pages)):
            file_writer = PdfWriter()
            # 将遍历的每一页添加到实例化对象中
            file_writer.add_page(pdf.pages[onePage])
            for i in range(0, len(target_page)):
                if onePage == target_page[i] - 1:
                    with open("{}.pdf".format(onePage + 1), 'wb') as out:
                        resultPath.append(out.name)
                        file_writer.write(out)

    return resultPath
