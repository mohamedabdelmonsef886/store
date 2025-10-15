

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
