from django.shortcuts import render

# Create your views here.

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import User, Task, Category, Comment
from .serializers import UserSerializer, TaskSerializer, CategorySerializer, CommentSerializer

# User registration view
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Task management views
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

# Category management views
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# Comment views for a specific task
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        task_id = self.kwargs.get('task_id')
        return Comment.objects.filter(task_id=task_id)

    def perform_create(self, serializer):
        task_id = self.kwargs.get('task_id')
        task = Task.objects.get(id=task_id)
        serializer.save(user=self.request.user, task=task)
