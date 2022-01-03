# -*- coding: utf-8 -*-

import datetime

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication
)

from authusers.serializers import UserSerializer
from authusers.models import CustomUser
from authusers.util import get_formatted_response, JSONWebTokenAuthentication

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class RegisterView(APIView):
    """
        Register View
    """

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
        Login View
    """

    def post(self, request):

        if request.data:
            email = request.data["email"]
            password = request.data["password"]

            if not email:
                return Response(get_formatted_response(
                    404,
                    "Email is missing"
                ))

            if not password:
                return Response(get_formatted_response(
                    404,
                    "Password is missing"
                ))

            user = CustomUser.objects.filter(email=request.data["email"]).first()

            if not user:
                message = "Account with this email does not exists"
                return Response(get_formatted_response(
                    404,
                    message
                ))

            user = CustomUser.objects.filter(email=email).first()

            if not user:
                raise AuthenticationFailed("User not found!!!")

            if not user.check_password(password):
                raise AuthenticationFailed("Incorrect Password!!!")

            payload = {
                "id": user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
                "iat": datetime.datetime.utcnow()
            }

            payload = jwt_payload_handler(user)
            jwt_token = jwt_encode_handler(payload)

            # jwt_token = jwt.encode(payload, "secret", algorithm="HS256").decode("utf-8")
            user.jwt_token = jwt_token
            user.save()

            response = Response()
            response.set_cookie(key="jwt_token", value=jwt_token, httponly=True)

            message = "Login Successfully"
            resp_status = 200
            response_data = {}
            response_params = {
                "jwt_token": jwt_token,
                "token": jwt_token,
                "user_id": user.id,
                "id": user.id,
                "full_name": user.get_full_name(),
                "email_id": user.email,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
            }
            response_data["data"] = response_params
            response_data["message"] = message
            response_data["status"] = resp_status
            response.data = response_data

            return response

        else:
            return Response(get_formatted_response(404, "Please enter proper data to login"))


class UserView(APIView):
    """
        Get User View
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)


    def get(self, request):

        token = False
        token = request.user.jwt_token if request.user and request.user.jwt_token else False

        if not token:
            raise AuthenticationFailed("UnAuthenticated!")

        serializer = UserSerializer(request.user)

        return Response(get_formatted_response(
            200,
            "Fetch user details successfully!!!",
            serializer.data
        ))


class LogoutView(APIView):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication, BasicAuthentication)

    def post(self, request):
        request.user.jwt_token = ""
        request.user.save()
        return Response(get_formatted_response(200, "User logged out successfully."))


class UserList(generics.ListAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication, BasicAuthentication)

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (
        JSONWebTokenAuthentication, SessionAuthentication, BasicAuthentication)

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
