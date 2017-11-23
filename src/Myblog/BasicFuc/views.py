# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from models import BlogPost

def homepage(request):
    return HttpResponse('You are at home page!')

def article(request):
    L = []
    for i in BlogPost.objects.all():
        L.append(i.id)
        L.append(i.article_title)
        L.append(i.article_content)
        L.append(i.publish_time)
    return HttpResponse(L)