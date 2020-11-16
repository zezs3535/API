# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField()
    text = models.TextField()

    def __str__(self):
        return self.title
# Create your models here.

    