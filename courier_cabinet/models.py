# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from info.models import Address,City


# Create your models here.
class User(models.Model):
    class Meta:
        db_table = "system_users"
    id = models.BigIntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    biography = models.TextField()
    start_working_date = models.DateField()
    rating = models.IntegerField()
    password = models.CharField(max_length=30, default='qwerty')
    city = models.ForeignKey(City, default=None)
    last_latitude = models.FloatField(default=0.0)
    last_longitude = models.FloatField(default=0.0)


class Order(models.Model):
    class Meta:
        db_table = "courier_order"
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField()
    responsible = models.ForeignKey(User)
    address = models.ForeignKey(Address)

