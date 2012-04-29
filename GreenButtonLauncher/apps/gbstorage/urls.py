'''
Created on Apr 29, 2012

@author: Bryan
'''

from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

urlpatterns = patterns('GreenButtonLauncher.apps.gbstorage.views',
    (r'^$', 'index'),
)
