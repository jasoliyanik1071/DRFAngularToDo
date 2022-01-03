# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from todos.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # django rest-framework
    # path('', include('rest_framework.urls')),
    url('api-auth/', include('rest_framework.urls')),

    # Custom App URL's :: ToDos
    url(r'', include('todos.urls')),
    url(r'api/', include('authusers.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
