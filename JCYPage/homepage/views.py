# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
import json
from bs4 import BeautifulSoup
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import News


def index(request):
    return render(request, 'index.html')
# Create your views here.

def search(request):
    return render(request, 'search.html')

def find(request):
    post = News()
    post.text=request.POST['text']
    post.title=request.POST['title']
    post.url=request.POST['url']
    post.save()

    return redirect('search.html')