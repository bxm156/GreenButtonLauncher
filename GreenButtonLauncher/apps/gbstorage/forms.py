'''
Created on Apr 29, 2012

@author: Bryan
'''
from django import forms

class UploadForm(forms.Form):
    gb_data = forms.FileField()