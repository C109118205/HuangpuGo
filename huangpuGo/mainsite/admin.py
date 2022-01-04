#from django.contrib import admin
from django.contrib.gis import admin
from mainsite.models import Store


class PostStrore(admin.ModelAdmin):
    list_display =('id','type','name','lat','lon','note','phone_number','address','FBLink','IGLink','OtherLink','Logo','Picture1','Picture2')

admin.site.register(Store,PostStrore)
# Register your models here.
