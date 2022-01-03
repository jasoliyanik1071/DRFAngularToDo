# -*- coding: utf-8 -*-

from django.contrib import admin
from authusers.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "is_active")
    search_fields = ("todo_title", )
    list_filter = ("username", )
    list_per_page = 15

    class Meta:
        model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
