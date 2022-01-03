# -*- coding: utf-8 -*-

import datetime

# Django callables
from django.utils import timezone

# Django callables
from django.conf import settings
from django.http import Http404, HttpResponse
from django.template.loader import render_to_string

# REST callables
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Custom created callables
from todos.models import Todo
from todos.serializers import TodoSerializer
from todos.permissions import IsOwnerOrReadOnly
from todos.notification_email import *
from todos.utils import get_site


def index(request):
    return HttpResponse("Hello, world. You're at the todoapp index.")

class TodoDetail(APIView):
    """
        - LoggedIn users, Retrieve/Fetch all the ToDos
        - LoggedIn users able to perform Create, Update & Delete
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def update_start_and_end_date_payload(self, request_data, request_type="create"):
        """
            # Used to SET start & end date if not set in request
            # i.e:
                - If in request while Create or Edit any ToDo then lets assume that start or end date are not set then we can set both dates manually.
                - Also manage error handling for start_date & end_date like,
                    - In request by-mistake anyone can ignore/remove start_date params then will check and add start_date params
                    - In request by-mistake anyone can ignore/remove end_date params then will check and add end_date params

            ## Function Params:
                * request_data:
                    - To check, start or end date exist in payload or not?
                * request_type:
                    - This function all at Create & Update Todo,
                    - So, at the time of creation we need to set who is the creator of Todo,
                    - So, will set the created_by as current requested user.
        """

        if "start_date" in request_data:
            if not request_data["start_date"]:
                request_data.update({
                    "start_date": datetime.datetime.now(tz=timezone.utc)
                })
        else:
            request_data.update({
                "start_date": datetime.datetime.now(tz=timezone.utc)
            })

        if "end_date" in request_data:
            if not request_data["end_date"]:
                request_data.update({
                    "end_date": datetime.datetime.now(tz=timezone.utc)
                })
        else:
            request_data.update({
                "end_date": datetime.datetime.now(tz=timezone.utc)
            })

        if request_type == "create":
            request_data.update({
                "created_by": self.request.user
            })

        return request_data


    def send_notification_email(self, request, todo_instance, todo_action_type):
        """
            # Used to send notification email at any kind of action on ToDos like, Create, Update or Delete
            # i.e:
                - If any user Create new ToDo, then will send mail with Created ToDos details as reference.
                - If any user Uppdate existing ToDo, then will send mail with Updated ToDos details as reference.
                - If any user Deleted ToDo from his/her list, then will send mail with Deleted ToDos details as reference.

            Note:
                - This function manage all the Create, Update & Delete related notification for email
                - To reduce the code and manage in single function I have created this for generic code purpose.

            ## Function Params:
                * request:
                    - To get any params from request
                    - i.e:
                        - This func. will manage generic concept, so to define request wise params will use request

                * todo_instance:
                    - Used to store currently performed action ToDo instance object as reference
                    - To send todo-instancee in email context as reference

                * todo_action_type:
                    - To Dynamically manage which action perform
                    - i.e:
                        - if sending Create notification mail then having "Created" as value
                        - if sending Update notification mail then having "Updated" as value
                        - if sending Delete notification mail then having "Deleted" as value
        """

        site = get_site(request)
        context = {
            "site": site,
            "current_user": self.request.user.get_full_name() if self.request.user else  "",
            "settings": settings,
            "todo_instance" : todo_instance,
            "todo_action_type": todo_action_type,
            "icon": site + "/media/logo/todo-logo-icon-img.jpeg"
        }

        # Used to parse HTML to string with dynamically added context
        message_body = render_to_string('lms/emails/body_mail.html', context)

        subject = "{subject}: ToDo {todo_title}".format(subject=todo_action_type, todo_title=todo_instance.todo_title)
        send_todo_notification_email(subject, message_body, [todo_instance.created_by.email])


    def set_todo_updated_user(self, todo_obj):
        """
            - Used to set ToDos owner as per Created or Updated ToDos details
        """
        todo_obj.created_by=self.request.user
        todo_obj.save()

    def get_object(self, pk):
        """
            - Used to return ToDos object as instance
        """
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        """
            - Used to fetch all the todos with currently loggedin user
        """
        serializer = TodoSerializer(Todo.objects.filter(created_by=self.request.user), many=True)
        return Response({
            "data": {
                "alltodos": serializer.data,
            }
        })

    def post(self, request, format=None):
        """
            - Used to Create new Todo
        """

        # Set or Validate Start & End Date
        request_data = self.update_start_and_end_date_payload(request.data, request_type="create")

        #
        serializer = TodoSerializer(data=request_data)

        if serializer.is_valid():
            todo_obj = serializer.save()
            
            # Update Owner of the ToDo
            self.set_todo_updated_user(todo_obj)

            # Send Email as confirmation notification to manage this action has been successfully done
            self.send_notification_email(request, todo_obj, "Created")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        """
            - Used to Update existing ToDo
        """

        todo_instance = self.get_object(pk)
        request_data = self.update_start_and_end_date_payload(request.data, request_type="update")
        serializer = TodoSerializer(todo_instance, data=request_data)

        if serializer.is_valid():
            todo_obj = serializer.save()

            # Update Owner of the ToDo
            self.set_todo_updated_user(todo_obj)

            # Send Email as confirmation notification to manage this action has been successfully done
            self.send_notification_email(request, todo_instance, "Updated")

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
            - Used to Delete Existing ToDo or Delete Any ToDo from the List
        """

        todo_instance = self.get_object(pk)

        # Send Email as confirmation notification to manage this action has been successfully done
        self.send_notification_email(request, todo_instance, "Deleted")

        todo_instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
