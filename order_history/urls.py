from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'order_history', views.OrderHistoryViewset)  # Consistent naming
router.register(r'review', views.ReviewViewset)  # Register ReviewViewset properly

urlpatterns = [
    path('', include(router.urls)),  # Include all registered routes
]
