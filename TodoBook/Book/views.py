from django.shortcuts import render
from rest_framework import generics
from .serializers import UsersSerializer
from .serializers import TaskSerializer
from .models import User
from .models import Task

class UserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    lookup_field = 'pk'

# class UserView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UsersSerializer

class TaskView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer