from django.db import models

# Create your models here.
class GreenButtonData(models.Model):
    pin = models.CharField(max_length=10, blank=False,null=False,unique=True)
    added = models.DateTimeField(auto_now_add=True)
    data = models.TextField(blank=False,null=False)
    data_hash = models.CharField(max_length=32,blank=False,null=False)