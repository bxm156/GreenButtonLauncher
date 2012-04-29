'''
Created on Apr 29, 2012

@author: Bryan
'''

from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

urlpatterns = patterns('GreenButtonLauncher.apps.gbstorage.views',
    (r'^$', 'index'),
    (r'^get/(?P<apin>[a-zA-Z0-9+/]{7})/$','getData'),
    (r'^delete/(?P<apin>[a-zA-Z0-9+/]{7})/$','delete'),
)
