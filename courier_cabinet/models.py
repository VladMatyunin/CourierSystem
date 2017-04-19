# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    class Meta:
        db_table = "system_users"
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    biography = models.TextField()
    start_working_date = models.DateField()
    rating = models.IntegerField()
