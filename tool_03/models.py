# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=50, default='default name')
    user_id = models.IntegerField(default=1)
    user_name = models.CharField(max_length=10, default='default name')
    content = models.CharField(max_length=500, default='default content')
    created_at = models.IntegerField(default=1514879938)

    def __str__(self):
        return self.name

class Comment(models.Model):
    blog_id = models.IntegerField(default=1)
    user_id = models.IntegerField(default=1)
    user_name = models.CharField(max_length=10, default='default name')
    content = models.CharField(max_length=500, default='default content')
    created_at = models.IntegerField(default=1514879938)
