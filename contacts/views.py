from django.shortcuts import render
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView,RetrieveAPIView
from rest_framework.generics import CreateAPIView
from .serializers import TaskSerializer
from .models import Task

class TaskList(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CreateView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UpdateTaskView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DeleteTaskView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class DeleteTaskListView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'


class TaskDetail(RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'pk'
