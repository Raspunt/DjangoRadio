from django.shortcuts import render
from . models import *



def StartPage(request):
    radioStream = RadioStream.objects.all()
    return render(request,"Radio/index.html",{'radios':radioStream})
