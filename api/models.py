from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField( max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.ForeignKey('Category', related_name='products', on_delete=models.CASCADE)
    seller = models.ForeignKey('auth.user', related_name='products', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)