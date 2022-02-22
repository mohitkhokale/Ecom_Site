from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

""" realted_name is used for create realtion btw parent to child """

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="UserProfile")
    first_name = models.TextField(null=True,blank=True)
    last_name = models.TextField(null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    mobile = models.CharField(max_length=10,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    about = models.TextField(max_length=255,null=True,blank=True)
    user_img = models.ImageField(upload_to='media',null=True,blank=True)
    email = models.EmailField(max_length=255,default='example@email.com')

    def __str__(self):  
        return str(self.first_name)

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
     UserProfile.objects.create(user=instance)
    instance.UserProfile.save()