import datetime
from django.shortcuts import render
from django.views import View
from blog.models import BlogCategory , Blog
from product.models import ProductCategory
from django.contrib.auth.models import User

from user_profile.models import UserProfile


# Create your views here.
class Blogs(View):
    
    def get(self, request,blog_id=None):
     
        navigationProductCategory = ProductCategory.objects.filter(status=True)
        blogcategory = BlogCategory.objects.filter(status=True)
        blog = Blog.objects.all()
        recent_news = Blog.objects.filter(date=datetime.datetime.now()).exclude(id = blog_id)
        context ={
            'navigationProductCategory':navigationProductCategory,
            'blogcategory':blogcategory,
            'blogs':blog,
            'recent_news':recent_news,
        }
        return render(request,"blog.html",context)


class blogdetails(View):
    def get(self, request,blog_id):
     
        print(blog_id)
        
       
        navigationProductCategory = ProductCategory.objects.filter(status=True)
        blogcategory = BlogCategory.objects.filter(status=True)
        blog = Blog.objects.filter(id = blog_id)
        admininfo = User.objects.filter(id=1)
        userprofile = UserProfile.objects.filter(id=3)
        recent_news = Blog.objects.filter(date=datetime.datetime.now()).exclude(id = blog_id)
        
        context ={
            'navigationProductCategory':navigationProductCategory,
            'blogcategory':blogcategory,
            'blogs':blog,
            'admininfo':admininfo,
            'userprofile':userprofile,
            'recent_news':recent_news,
             #  'recent_news':list(recent_news.values()),
            #  'userprofiles':list(userprofile.values()),
            #  'admininfo':list(admininfo.values()),
        }
        return render(request,"blogdetails.html",context)
