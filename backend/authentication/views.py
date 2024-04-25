from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from .models import User

# Create your views here.

class UserListCreate(generics.ListCreateAPIView):
    """
    Provides get and post handlers.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer