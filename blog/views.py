# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
     nama = "PediMf"
     buah = ['Apel','Anggur','Semangka']
     return render(request,'index.html', {'nama':nama,'buahbuahan':buah})

def index(request):
     return render(request,'index.html')

def about(request):
     return render(request,'about.html')

def kontak(request):
    return render(request,'kontak.html')
def blog(request):
     return render(request,'blog.html')    
