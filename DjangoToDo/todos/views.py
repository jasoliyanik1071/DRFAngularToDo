# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse

from rest_framework import generics, permissions, status

from rest_framework.response import Response
from rest_framework.views import APIView

from todos.models import Todo
from todos.serializers import TodoSerializer
from todos.permissions import IsOwnerOrReadOnly


def index(request):
    return HttpResponse("Hello, world. You're at the todoapp index.")


class TodoList(APIView):
    """
        - List of all ToDos or Create new ToDos
    """
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

    def get(self, request, format=None):
        serializer = TodoSerializer(Todo.objects.all(), many=True)
        # serializer2 = CategorySerializer(Category.objects.all(), many=True)
        return Response({
            'data': {
                'alltodos': serializer.data,
                # 'categories': serializer2.data
            }
        })

    def post(self, request, format=None):
        """
            - If we are using JSON format then use below two lines
            - If we are using Key-Value pair then comment below two lines
        """
        # print(request.data['todos'])
        # serializer = TodoSerializer(data=request.data['todos'])
        """
            - If we are using Key-Value pair then use below two lines
            - If we are using JSON then comment below two lines
        """
        print(request.data)
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class TodoDetail(APIView):
    """
        - Retrieve, update or delete a ToDos instance.
    """
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TodoSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = TodoSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
