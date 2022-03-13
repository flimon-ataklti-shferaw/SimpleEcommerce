from django.db import models

from products.models import Product

class Cart(models.Model):
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, decimal_places=2, max_digits=100)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)