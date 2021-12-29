# -*- coding: utf-8 -*-

from django.contrib import admin
from todos.models import Todo
# from todos.models import Todo, Category


class TodoAdmin(admin.ModelAdmin):
    # list_display = ('todo_title', 'todo_desc', 'created_date', 'updated_date', 'todo_status', 'created_by', 'category')
    list_display = ('todo_title', 'todo_status')
    search_fields = ('todo_title', )
    list_filter = ('todo_title', )
    list_per_page = 15

    class Meta:
        model = Todo

    # # associate user with specific todo entry
    # def save_model(self, request, obj, form, change):
    #     obj.created_by = request.user
    #     super().save_model(request, obj, form, change)

admin.site.register(Todo, TodoAdmin)
