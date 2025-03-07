from django.db import models
from django.contrib.auth.models import User
from menu.models import Menu  # Assuming Menu model exists in the 'menu' app
from accounts.models import Customer

class OrderHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The customer who placed the order
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)  # Ordered food item
    quantity = models.PositiveIntegerField(default=1)  # Quantity of the ordered item
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Total cost of the order
    order_status = models.CharField(
        max_length=20, 
        choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], 
        default='Pending'
    )  # Order status
    ordered_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the order was placed

    def __str__(self):
        return f"Order {self.id} by {self.user.username} - {self.menu_item.name}"


class Review(models.Model):
    order = models.ForeignKey(OrderHistory, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} - {self.menu_item.name} ({self.rating} stars)"
