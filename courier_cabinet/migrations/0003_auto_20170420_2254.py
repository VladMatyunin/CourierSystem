# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 22:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
        ('courier_cabinet', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='info.City'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='user',
            name='last_longitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='qwerty', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
