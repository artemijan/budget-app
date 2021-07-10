from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from core.customer.dto import UserSerializer
from core.customer.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
