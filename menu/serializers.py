from rest_framework import serializers
from .models import Menu
from categories.models import Category

class MenuSerializer(serializers.ModelSerializer):
    # Optionally, include the Category name in the serialized data
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Menu
        fields = ['id', 'name', 'description', 'price', 'category', 'category_name', 'image', 'quantity', 'available', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
