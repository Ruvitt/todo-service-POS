from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Todo, Post, Comment
from .serializers import UserSerializer, TodoSerializer, PostSerializer, CommentSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    def get_queryset(self):
        user_id = self.kwargs.get('user_pk')
        if user_id is not None:
            return Todo.objects.filter(user_id=user_id)
        else:
            # Handle the case when 'user_pk' is not provided
            return Todo.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_pk')
        if user_id is not None:
            return Post.objects.filter(user_id=user_id)
        else:
            # Handle the case when 'user_pk' is not provided
            return Post.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_pk')
        if user_id is not None:
            return Comment.objects.filter(user_id=user_id)
        else:
            # Handle the case when 'user_pk' is not provided
            return Comment.objects.all()