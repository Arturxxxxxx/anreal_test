from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer, CategorySerializer
from .models import ProductHome, Category

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = ProductHome.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductHome.objects.all()
    serializer_class = ProductSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
