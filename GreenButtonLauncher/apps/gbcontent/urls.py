'''
Created on Apr 29, 2012

@author: Bryan
'''

from django.conf.urls.defaults import *

urlpatterns = patterns('GreenButtonLauncher.apps.gbcontent.views',
    url(r'^$', 'start', name="start"),
    url(r'ajax-upload$', 'import_uploader', name="my_ajax_upload"),
)
