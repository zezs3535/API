# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    #news_list=News.objects.all()
    #return render(request, 'index.html',{'news_list':news_list})
    return render(request, 'index.html')
# Create your views here.

def search(request):
    return render(request, 'search.html')