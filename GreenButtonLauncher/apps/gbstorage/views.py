# Create your views here.

from django.shortcuts import render_to_response, redirect, RequestContext

def index(request):
    return render_to_response('index.html',{},
                              context_instance=RequestContext(request))

def getData(request):
    """
    The API URL for returning data to the Android App
    """
    pass

def delete(request):
    pass
    