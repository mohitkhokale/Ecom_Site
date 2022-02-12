from django.db import models
from django.db.models.fields.related import ForeignKey


# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)
    
class Blog(models.Model):
    Blog_Category = models.ForeignKey(BlogCategory,on_delete=models.CASCADE,related_name="BlogCategory")
    blog_name = models.CharField(max_length=255,null=True,blank=True)
    blog_img = models.ImageField( null=True,blank=True)
    date = models.DateField()
    description = models.TextField(blank=True)
    author = models.CharField(default="Admin",max_length=255)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.blog_name)

