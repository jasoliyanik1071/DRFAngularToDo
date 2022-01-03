# -*- coding: utf-8 -*-

from rest_framework import serializers
from authusers.models import CustomUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("id", "first_name", "last_name", "email", "password", "jwt_token")

        extra_kwargs = {
            "password": {"write_only": True}
        }

    def  create(self, validated_data):
        """
            - Override the serializers
            - Used to set password and email
        """
        password = validated_data.pop("password", None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        # Set Username as Email
        instance.username = instance.email
        instance.save()
        return instance
