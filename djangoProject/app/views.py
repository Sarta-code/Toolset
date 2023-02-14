# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
from django.conf import settings
from django.utils.datastructures import MultiValueDict


# Create your views here.

def index(request):
    import json
    print("FILES:", type(request.FILES))
    img = request.FILES.get('filekeyname')

    for i in request.FILES.items():
        print("$$:\n", i)

    # fileinfo = {"filepath": '', "filename": '', "filesize": '', "filetype": ''}

    # file_path = os.path.join(settings.MEDIA_ROOT, img.name)
    # with open(file_path, 'ab') as fp:
    #     for chunk in img.chunks():
    #         fp.write(chunk)

    obj = HttpResponse(json.dumps({'name': ''}))

    return obj
