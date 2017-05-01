# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

import models


class UserAdminModel(admin.ModelAdmin):
    fields = ['name', 'surname',  'start_working_date', 'city']
    list_filter = ['city', 'name', 'surname']


class AddressAdminInline(admin.StackedInline):
    model = models.Address


class OrderAdminModel(admin.ModelAdmin):
    inlines = [AddressAdminInline]


# Register your models here.
admin.site.register(models.User, UserAdminModel)
admin.site.register(models.Order)
admin.site.register(models.Address)
