# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import  User, Group
from rest_framework import viewsets
import serializers
from courier_cabinet import models

from django.shortcuts import render

# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.WorkerSerializer

