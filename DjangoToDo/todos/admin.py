# -*- coding: utf-8 -*-

from django.contrib import admin
from todos.models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ("todo_title", "created_date", "start_date", "end_date", "todo_status", "created_by")
    search_fields = ("todo_title", "created_by")
    list_filter = ("todo_title", "created_date", "start_date", "end_date", "created_by")
    list_per_page = 15

    class Meta:
        model = Todo

admin.site.register(Todo, TodoAdmin)
