from django.contrib import admin

from blog.models import BlogCategory
from blog.models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display= ('id','blog_name','date','description','author','Blog_Category')

admin.site.register(Blog,BlogAdmin)


class BlogAdminCategorys(admin.ModelAdmin):
        list_display= ('id','name','status')
admin.site.register(BlogCategory,BlogAdminCategorys)
