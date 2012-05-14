from django.shortcuts import render_to_response, redirect, RequestContext, get_object_or_404
from models import GreenButtonData
from django.http import Http404, HttpResponse

def getData(request, apin):
    """
    The API URL for returning data to the Android App
    """
    obj = get_object_or_404(GreenButtonData,pin=apin)
    return HttpResponse(obj.data)


def delete(request, apin):
    """
    Delete an object based on the PIN
    """
    obj = get_object_or_404(GreenButtonData,pin=apin)
    obj.delete()
    return HttpResponse()

def getHash(request,apin):
    obj = get_object_or_404(GreenButtonData,pin=apin)
    return HttpResponse(obj.data_hash)
    