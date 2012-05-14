'''
Created on May 14, 2012

@author: Bryan
'''
from ajaxuploader.backends.base import AbstractUploadBackend
import cStringIO, hashlib, base64, uuid
from django.db import IntegrityError
from GreenButtonLauncher.apps.gbstorage.models import GreenButtonData

class GreenButtonBackend(AbstractUploadBackend):
    
    def setup(self, filename):
        """Responsible for doing any pre-processing needed before the 
         upload
        starts."""
        self.output = cStringIO.StringIO()
    
#    def update_filename(self, request, filename):
#        """Returns a new name for the file being uploaded."""
    
    def upload_chunk(self, chunk):
        self.output.write(chunk)
    
    def upload_complete(self, request, filename):
        """Overriden to performs any actions needed post-upload, and 
         returns
        a dict to be added to the render / json context"""
        data = GreenButtonData()
        data.pin = base64.b64encode(uuid.uuid4().bytes,"az")[:7]
        data.data = self.output.getvalue()
        self.output.close()
        data.data_hash = hashlib.md5(data.data).hexdigest()
        success = False
        while not success:
            try:
                data.save()
                success = True
            except IntegrityError:
                success = False
                data.pin = base64.b64encode(uuid.uuid4().bytes)[:7]
        return {"success" : success, "pin":data.pin}