from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
class MenuItemsview(generics.ListCreateAPIView):
    queryset=MenuItem.objects.all()
    serializer_class=MenuItemSerializer