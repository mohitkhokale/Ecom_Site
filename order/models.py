from re import M
import django
from random import choices
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from product.models import Product

# Create your models here.
class Order(models.Model):
    """Order Model"""
    order_status_choices = (
        ("Pending","Pending"),
        ("Inprogress","Inprogress"),
        ("Cancelled","Cancelled"),
        ("Delivered","Delivered")
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    date_time = models.DateTimeField(default=django.utils.timezone.now)
    order_status = models.CharField(max_length=255,choices = order_status_choices, default='pending')
    payment_status = models.BooleanField(default = False)
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return str(self.user)

class OrderDetail(models.Model):
    """Order Details"""
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.order)

class Payment(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=255,null=True,blank=True)
    payment_status = models.CharField(max_length=255,null=True,blank=True)
    payment_method = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.CharField(max_length=255,null=True,blank=True)
    amount = models.CharField(max_length=255,null=True,blank=True)
    

    
    def __str__(self):
        return str(self.transaction_id)
