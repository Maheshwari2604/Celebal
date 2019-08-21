# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class userprofile(models.Model):
    firstname = models.CharField(max_length=250, help_text='Required')
    email = models.EmailField(max_length=250, help_text='Required')
    password = models.CharField(max_length=250)
    
    def __str__(self):
        return str(self.id)
        