from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .models import User, Task, Category, Comment
from .serializers import (
    UserSerializer,
    TaskSerializer,
    CategorySerializer,
    CommentSerializer,
    RegisterSerializer,
)

# ------------------- User Registration -------------------
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer   # 👈 make sure it uses RegisterSerializer
    permission_classes = [AllowAny]         # anyone can register


# ------------------- User View -------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


# ------------------- Task View -------------------
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # auto-assign task owner


# ------------------- Category View -------------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


# ------------------- Comment View -------------------
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # auto-assign comment owner
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "Send a POST request to register"}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserDetailView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAdminUser]  # only admin can delete
    from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializers import CommentSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
