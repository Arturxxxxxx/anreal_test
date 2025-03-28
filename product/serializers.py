from rest_framework import serializers
from .models import Category, ProductHome

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category', 'image')

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField() 

    class Meta:
        model = ProductHome
        fields = ('id', 'category', 'image', 'title', 'address', 'year', 'category_name')

    def get_category_name(self, obj):
        return obj.category.category  