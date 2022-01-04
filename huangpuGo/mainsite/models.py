#from django.db import models
from django.contrib.gis.db import models

class Store(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)    
    FBLink = models.URLField(max_length = 400, null=True, blank=True)
    IGLink = models.URLField(max_length = 400, null=True, blank=True)
    OtherLink = models.URLField(max_length = 400, null=True, blank=True)
    Logo = models.TextField(null=True, blank=True)
    Picture1 = models.TextField(null=True, blank=True)
    Picture2 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.type
