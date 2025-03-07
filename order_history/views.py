from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import OrderHistory,Review
from menu.models import Menu
from accounts.models import Customer
from .serializers import OrderHistorySerializer,ReviewSerializer
from rest_framework.permissions import IsAuthenticated

class OrderHistoryViewset(viewsets.ModelViewSet):
    queryset = OrderHistory.objects.all()  # Ensure queryset is defined
    serializer_class = OrderHistorySerializer

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()  # Ensure queryset is defined
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PlaceOrderView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user  
        menu_item_id = request.data.get("menu_item_id")
        quantity = request.data.get("quantity")

        try:
            menu_item = Menu.objects.get(id=menu_item_id)
        except Menu.DoesNotExist:
            return Response({"error": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)

        total_price = menu_item.price * quantity

        order = OrderHistory.objects.create(
            user=user,
            menu_item=menu_item,
            quantity=quantity,
            total_price=total_price,
            order_status="Pending"
        )

        serializer = OrderHistorySerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
