# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class City(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()


class Address(models.Model):
    id = models.BigIntegerField(primary_key=True)
    city = models.ForeignKey(City)
    address = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()
