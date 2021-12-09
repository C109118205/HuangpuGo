#from django.contrib import admin
from django.contrib.gis import admin
from mainsite.models import Store


class PostStrore(admin.ModelAdmin):
    list_display =('id','type','name','lat','lon')

admin.site.register(Store,PostStrore)
# Register your models here.
