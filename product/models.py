from email.mime import image
from operator import mod
from django.db import models
from django.db.models.fields import BooleanField
from django.db.models.fields.related import ForeignKey

# Create your models here.
class ProductCategory(models.Model):
    """ Product Category Model"""
    name = models.CharField(max_length=150)
    status = models.BooleanField(default=True)

    def __str__(self):
        """String rep for object Product"""
        return str(self.name)

class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE,related_name="ProductCategory")
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8,decimal_places=2)
    stock = models.IntegerField(default =1)
    cover_img= models.ImageField()
    status = models.BooleanField(default=True)
    

    def __str__(self):
        """String rep for object Product"""
        return str(self.name)

class ProductImages(models.Model):
    """Product will have more the one image"""
    product = ForeignKey(Product,on_delete=models.CASCADE)
    cover_image= models.ImageField()

    def __str__(self):
        """String rep for object ProductImage """
        return str(self.product)
