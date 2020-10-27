# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import json
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def index(request):
    #news_list=News.objects.all()
    #return render(request, 'index.html',{'news_list':news_list})
    return render(request, 'index.html')
# Create your views here.

def search(request):
    """ newslist=News.objects.all()
    context={'newslist':newslist} """
    url = requests.get(
        "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=카카오")

    soup = BeautifulSoup(url.text, 'html.parser')
    title = soup.select('.news .type01 li dt a')
    #uploadTime = soup.select('.news .type01 li dd span')
    newstitle=[]
    for item in title:
        newstitle.append(item.attrs['title'])
    newstitles=json.dumps({"kinds":"title","values":newstitle})
    return render(request, 'search.html',newstitles)