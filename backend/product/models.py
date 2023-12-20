from decimal import Decimal
from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name
    @property
    def get_discount(self):
        return self.price * Decimal(0.5)
