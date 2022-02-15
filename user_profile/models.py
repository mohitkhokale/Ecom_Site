from django.db import models
from django.contrib.auth.models import User

# Create your models here.
""" realted_name is used for create realtion btw parent to child """

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="UserProfile")
    address = models.TextField(null=True,blank=True)
    mobile = models.CharField(max_length=10,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    user_img = models.ImageField(upload_to='media',null=True,blank=True)
    about = models.TextField(max_length=255,null=True,blank=True)
    first_name = models.TextField(null=True,blank=True)
    last_name = models.TextField(null=True,blank=True)
    def __str__(self):  
        return str(self.address)
