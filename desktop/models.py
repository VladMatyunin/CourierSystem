# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from info.models import Address


# Create your models here.
class Item(models.Model):
    id = models.BigIntegerField(primary_key=True, unique=True)
    dateTimeDeliver = models.DateTimeField()
    cost = models.IntegerField()
    address = models.ForeignKey(Address)
