from django.shortcuts import render_to_response, redirect, RequestContext
from forms import UploadForm
import hashlib
from models import GreenButtonData
from django.db import IntegrityError
import cStringIO, base64, uuid
#from lxml import etree
#from GreenButtonLauncher.settings import STATIC_ROOT

def index(request):
    
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
            data.pin = base64.b64encode(uuid.uuid4().bytes)[:7]
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
                
            
            print "Data Saved"
            context = RequestContext(request,
                         {'errors':form.errors,
                         'form':UploadForm()})
            return render_to_response('index.html',context)
    else:
        return render_to_response('index.html',{'form':UploadForm()},
                              context_instance=RequestContext(request))

def getData(request):
    """
    The API URL for returning data to the Android App
    """
    pass

def delete(request):
    pass
    