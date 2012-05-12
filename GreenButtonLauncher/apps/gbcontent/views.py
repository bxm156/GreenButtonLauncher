# Create your views here.
from django.shortcuts import render_to_response, redirect, RequestContext, get_object_or_404

def index(request):
    return render_to_response('index.html',RequestContext(request))
    