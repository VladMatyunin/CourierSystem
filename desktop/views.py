# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponse
from django.shortcuts import render
from courier_cabinet.models import Order
from models import Item
# Create your views here.
from django.template.loader import get_template


def load_desktop(request):
    return HttpResponse(get_template('desktop.html').render({'items': Item.objects.all()}))


def order_details(request, order_id=1):
    view = get_template('order.html')
    return HttpResponse(view.render({'id': order_id}))
