from rest_framework import serializers
from .models import OrderHistory, Review
from menu.models import Menu
from accounts.models import Customer
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']
class ReviewSerializer(serializers.ModelSerializer):
    order_id = serializers.PrimaryKeyRelatedField(queryset=OrderHistory.objects.all(), source='order')

    class Meta:
        model = Review
        fields = ['id', 'user', 'order_id', 'menu_item', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at']


class OrderHistorySerializer(serializers.ModelSerializer):
    user = Customer()
    user = UserSerializer() 
    menu_item = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.all())
    review = ReviewSerializer(source='review_set', many=True, read_only=True)  # Nested review serializer

    class Meta:
        model = OrderHistory
        fields = ['id', 'user', 'menu_item', 'quantity', 'total_price', 'order_status', 'ordered_at', 'review']
        read_only_fields = ['id', 'ordered_at']
