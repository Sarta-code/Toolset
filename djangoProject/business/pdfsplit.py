from borb.pdf import Document
from borb.pdf.pdf import PDF


def split_pdf(pdf_file_handle):
    # 阅读PDF
    input_pdf = PDF.loads(pdf_file_handle)

    # 创建两个空的PDF，以容纳分裂的每一半
    output_pdf_001 = Document()
    output_pdf_002 = Document()

    # 分割
    for i in range(0, 10):
        if i < 5:
            output_pdf_001.add_page(input_pdf.get_page(i))
        else:
            output_pdf_002.add_page(input_pdf.get_page(i))

    # 撰写PDF
    with open("output_001.pdf", "wb") as pdf_out_handle:
        PDF.dumps(pdf_out_handle, output_pdf_001)

    # 撰写PDF
    with open("output_002.pdf", "wb") as pdf_out_handle:
        PDF.dumps(pdf_out_handle, output_pdf_002)
