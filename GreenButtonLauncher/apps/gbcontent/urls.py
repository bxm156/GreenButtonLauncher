'''
Created on Apr 29, 2012

@author: Bryan
'''

from django.conf.urls.defaults import *

urlpatterns = patterns('GreenButtonLauncher.apps.gbcontent.views',
    (r'^$', 'index'),
    (r'^news/$','news'),
    (r'^about/$','about'),
    (r'^contact/$','contact'),
    (r'^upload/$','upload')
)