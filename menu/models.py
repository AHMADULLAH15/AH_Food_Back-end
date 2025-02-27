from django.db import models
from categories.models import Category
# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Food item name
    description = models.TextField(blank=True, null=True)  # Description of the food item
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the food item
    category = models.ForeignKey(Category, related_name='categories', on_delete= models.CASCADE)  # Category (e.g., Pizza, Burger, Drinks)
    image = models.ImageField(upload_to='menu/food_images/', blank=True, null=True)  # Image of the item
    quantity = models.IntegerField(default=1)
    available = models.BooleanField(default=True)  # Availability status
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when item is added
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for last update

    def __str__(self):
        return self.name