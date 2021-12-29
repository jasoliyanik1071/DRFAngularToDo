# -*- coding: utf-8 -*-

"""ToDoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url

from todos.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # django rest-framework
    # path('', include('rest_framework.urls')),
    url('api-auth/', include('rest_framework.urls')),

    # Custom App URL's :: ToDos
    url(r'', include('todos.urls')),
]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from todos import views

# router = DefaultRouter()
# router.register(r'todos', views.TodoViewSet)
# router.register(r'users', views.UserViewSet)


# urlpatterns += [
#     path('', include(router.urls)),
#     path('', include('rest_framework.urls')),
# ]
