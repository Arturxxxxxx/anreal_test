from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer
from .models import ProductHome, Category
from rest_framework import viewsets

class ProductView(viewsets.ModelViewSet):
    queryset = ProductHome.objects.all()
    serializer_class = ProductSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

