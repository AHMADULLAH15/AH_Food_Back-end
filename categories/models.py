from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length = 40,blank=True)
    def __str__(self):
        return self.name