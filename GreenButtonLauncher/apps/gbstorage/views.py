from django.shortcuts import render_to_response, redirect, RequestContext, get_object_or_404
from forms import UploadForm
from models import GreenButtonData
from django.db import IntegrityError
import cStringIO, hashlib, base64, uuid
from django.http import Http404, HttpResponse

#from lxml import etree
#from GreenButtonLauncher.settings import STATIC_ROOT

def index(request):
    """
    The Index page
    """
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)
        if form.is_valid():
            fileData = request.FILES['gb_data']
            #xmlschema_file = open(STATIC_ROOT + "/xsd/espi.xsd",'rb')
            #xmlschema_doc = etree.parse(xmlschema_file)
            #xmlschema = etree.XMLSchema(xmlschema_doc)
            
            output = cStringIO.StringIO()
            for chunk in fileData.chunks():
                output.write(chunk)
            
            #print output.getvalue()
            #xmlschema.validate(etree.parse(output))
            
            data = GreenButtonData()
            data.pin = base64.b64encode(uuid.uuid4().bytes,"az")[:7]
            print data.pin
            data.data = output.getvalue()
            output.close()
            data.data_hash = hashlib.md5(data.data).hexdigest()
            success = False
            while not success:
                try:
                    data.save()
                    success = True
                except IntegrityError:
                    success = False
                    data.pin = base64.b64encode(uuid.uuid4().bytes)[:7]

            context = RequestContext(request,
                         {'errors':form.errors,
                         'form':UploadForm(),
                         'pin':data.pin})
            return render_to_response('index.html',context)
    else:
        return render_to_response('index.html',{'form':UploadForm()},
                              context_instance=RequestContext(request))

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
    