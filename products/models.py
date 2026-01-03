from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]

    GENDER_CHOICES = [
        ('MEN', 'Men'),
        ('WOMEN', 'Women'),
        ('UNISEX', 'Unisex'),
    ]

    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    stock_quantity = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
