# -*- coding: utf-8 -*-

# from django.utils.timesince import timesince

from rest_framework import serializers
from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):

    # created_by = serializers.SerializerMethodField()
    # created_date = serializers.SerializerMethodField()
    # updated_date = serializers.SerializerMethodField()
    # category = serializers.SerializerMethodField()


    class Meta:
        model = Todo
        fields = ('id', 'todo_title', 'todo_status')
        # fields = ('id', 'todo_title', 'todo_desc', 'created_date', 'updated_date', 'todo_status', 'created_by', 'category')

    # def get_created_by(self, obj):
    #     return obj.created_by.username if obj and obj.created_by else ""
    
    # def get_category(self, obj):
    #     return obj.category.category_name if obj and obj.category else ""

    # def get_created_date(self,obj):
    #     return timesince(obj.created_date)

    # def get_updated_date(self,obj):
    #     return timesince(obj.updated_date)
