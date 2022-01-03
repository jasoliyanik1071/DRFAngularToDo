# -*- coding: utf-8 -*-

# from django.utils.timesince import timesince


from django.utils import timezone
import datetime

from rest_framework import serializers
from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):

    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ("id", "todo_title", "created_date", "start_date", "end_date", "todo_status", "created_by")

    def get_created_by(self, obj):
        return obj.created_by.username if obj and obj.created_by else ""

    # def get_created_date(self,obj):
    #     return timesince(obj.created_date)

    # def get_start_date(self,obj):
    #     return timesince(obj.start_date)

    # def get_end_date(self,obj):
    #     return timesince(obj.end_date)

    
    def create(self, validated_data, created_by=None):
        """
            - Override the serializers
            - Used to set Start & End date, if its blank
        """
        instance = Todo(**validated_data)
        if instance and not instance.start_date:
            instance.start_date = datetime.datetime.now(tz=timezone.utc)

        if instance and not instance.end_date:
            instance.end_date = datetime.datetime.now(tz=timezone.utc)
        instance.save()
        return instance
