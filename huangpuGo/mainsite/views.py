from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Store


def homepage(request):
    datas = Store.objects.all()
    return render(request,'map.html',locals())


