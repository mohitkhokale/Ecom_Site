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

class Couponcode(models.Model):
    coupon_name = models.CharField(max_length=255, blank=True,null=True)
    amount = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.coupon_name
