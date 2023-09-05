from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Order(models.Model):
    items = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    total = models.CharField(max_length=200)

    def __str__(self):
        return self.name