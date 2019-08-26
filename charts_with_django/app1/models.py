# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Passenger(models.Model):
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100)
    s = models.BooleanField()
    age = models.FloatField()
    AClass = models.PositiveSmallIntegerField()
