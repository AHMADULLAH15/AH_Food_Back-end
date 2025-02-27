from django.shortcuts import render
from rest_framework import viewsets
from .models import OrderHistory, Review
from .serializers import OrderHistorySerializer, ReviewSerializer

class OrderHistoryViewset(viewsets.ModelViewSet):
    queryset = OrderHistory.objects.all()  # Ensure queryset is defined
    serializer_class = OrderHistorySerializer

class ReviewViewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()  # Ensure queryset is defined
    serializer_class = ReviewSerializer
