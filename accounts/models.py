from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_phone = models.CharField(max_length=20)
    customer_address = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"