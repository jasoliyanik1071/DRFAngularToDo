# -*- coding: utf-8 -*-
from django.urls import path
from todos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todoapp/api/todos/', views.TodoList.as_view()),
    path('todoapp/api/todos/<int:pk>/', views.TodoDetail.as_view()),
]