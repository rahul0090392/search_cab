# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from restapi.models import Driver


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "phone_number",
        "email",
        "license_number",
        "car_number",
        "row_last_updated",
    )

    list_filter = ("phone_number", "email", "license_number", "car_number")
