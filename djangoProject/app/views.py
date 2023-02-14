# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
from django.conf import settings
from django.utils.datastructures import MultiValueDict


# Create your views here.

def index(request):
    import json
    # img = request.FILES.get('docx-46217')
    # print(img.size)
    fileinfo = []
    for i in request.FILES.items():
        file_Item = request.FILES.get(i[0])
        file_path = os.path.join(settings.MEDIA_ROOT, file_Item.name)
        with open(file_path, 'ab') as fp:
            for chunk in file_Item.chunks():
                fp.write(chunk)
        fileinfo.append(
            {"filepath": file_path, "filename": file_Item.name, "filesize": file_Item.size, "filetype": i[0]}
        )
    obj = HttpResponse(json.dumps(fileinfo))

    return obj
