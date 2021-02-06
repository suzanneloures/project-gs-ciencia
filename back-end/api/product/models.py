from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=100)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
