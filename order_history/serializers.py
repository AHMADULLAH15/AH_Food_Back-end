# from rest_framework import serializers
# from .models import OrderHistory, Review
# from menu.models import Menu

# class OrderHistorySerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())  # Use CurrentUserDefault
#     menu_item = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.all()) # Use PrimaryKeyRelatedField and specify queryset
#     review = serializers.SerializerMethodField() # SerializerMethodField for review

#     class Meta:
#         model = OrderHistory
#         # fields = ['id', 'user', 'menu_item', 'quantity', 'total_price', 'order_status', 'ordered_at', 'review']
#         # read_only_fields = ['id', 'ordered_at', 'review'] 
#         fields = '__all__'

#     def get_review(self, obj):
#         review = Review.objects.filter(order=obj).first()
#         if review:
#             return ReviewSerializer(review).data
#         return None



# class ReviewSerializer(serializers.ModelSerializer):
#     user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
#     menu_item = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.all())
#     order = serializers.PrimaryKeyRelatedField(queryset=OrderHistory.objects.all())

#     class Meta:
#         model = Review
#         fields = ['id', 'user', 'menu_item', 'order', 'rating', 'comment', 'created_at']
#         read_only_fields = ['id', 'created_at']
from rest_framework import serializers
from .models import OrderHistory, Review
from menu.models import Menu

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    menu_item = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.all())

    class Meta:
        model = Review
        fields = ['id', 'user', 'menu_item', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at']

class OrderHistorySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    menu_item = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.all())
    review = ReviewSerializer(source='review_set', many=True, read_only=True)  # Nested review serializer

    class Meta:
        model = OrderHistory
        fields = ['id', 'user', 'menu_item', 'quantity', 'total_price', 'order_status', 'ordered_at', 'review']
        read_only_fields = ['id', 'ordered_at']
