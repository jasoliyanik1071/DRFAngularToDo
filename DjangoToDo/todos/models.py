# -*- coding: utf-8 -*-

from django.utils import timezone
from django.db import models


class Todo(models.Model):
    todo_title = models.CharField(max_length=200,blank=True,verbose_name="Title",)
    # todo_desc = models.TextField(default='', blank=False, verbose_name='Description')

    created_date = models.DateTimeField(verbose_name="Created Date", default=timezone.now())
    start_date = models.DateTimeField(verbose_name="Start Date")
    end_date = models.DateTimeField(verbose_name="End Date")

    todo_status = models.BooleanField(default=False,verbose_name='Completed',)

    created_by = models.ForeignKey("authusers.CustomUser", related_name='todos_user', on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        ordering = ["-id", "created_date"]

    def __str__(self):
        return self.todo_title if self and self.todo_title else ""
