# from django.shortcuts import render
from django.http import HttpResponse
import json
from business.pdfsplit import Split_PDF_pageNum


# Create your views here.
def upload(request):
    # img = request.FILES.get('docx-46217')
    # print(img.size)
    fileInfo = []
    for i in request.FILES.items():
        file_Item = request.FILES.get(i[0])
        fileInfo = Split_PDF_pageNum(file_Item)

    obj = HttpResponse(json.dumps(fileInfo))

    return obj
