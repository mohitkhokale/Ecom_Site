from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class Cart(models.Model):
    """Cart Model"""
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        """Example mohit samsung s21 FE Quantity:1"""
        return f'{self.user} {self.product} - {self.quantity}'

