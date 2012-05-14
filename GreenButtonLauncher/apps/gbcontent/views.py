# Create your views here.
from django.shortcuts import render_to_response, redirect, RequestContext, get_object_or_404
from django.middleware.csrf import get_token
from ajaxuploader.views import AjaxFileUploader
from backend import GreenButtonBackend
def start(request):
    csrf_token = get_token(request)
    return render_to_response('index.html',
        {'csrf_token': csrf_token}, context_instance = RequestContext(request))

import_uploader = AjaxFileUploader(backend=GreenButtonBackend)