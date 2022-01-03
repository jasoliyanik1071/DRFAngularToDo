# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
        docstring for CustomUser
    """
    
    first_name = models.CharField(max_length=1024)
    last_name = models.CharField(max_length=1024)
    email = models.CharField(max_length=1024, unique=True)
    password = models.CharField(max_length=1024)

    jwt_token = models.CharField(max_length=1024, null=True, blank=True)
    # username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

