# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context


# Create your views here.
def load_cabinet(request):
    view = get_template('cabinet.html')
    return HttpResponse(view.render({'name': 'Vlad'}))
