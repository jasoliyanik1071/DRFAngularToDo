# -*- coding: utf-8 -*-

from django.db import models

# from django.utils import timezone


class Todo(models.Model):
    todo_title = models.CharField(max_length=200,blank=True,verbose_name='Title',)
    # todo_desc = models.TextField(default='', blank=False, verbose_name='Description')
    # created_date = models.DateField(verbose_name='Created Date', default=timezone.now())
    # updated_date = models.DateField(verbose_name='Updated Date', default=timezone.now())
    todo_status = models.BooleanField(default=False,verbose_name='Completed',)
    # created_by = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        ordering = ["-id", "todo_status"]

    def __str__(self):
        return self.todo_title
