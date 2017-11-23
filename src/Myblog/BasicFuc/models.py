# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BlogPost(models.Model):
    article_title = models.CharField(max_length=255)
    article_content = models.TextField(max_length=10240)
    publish_time = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.article_title