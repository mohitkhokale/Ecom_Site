from re import I
from django.contrib import admin, messages
from .models import Product, ProductCategory, ProductImages
# Register your models here.

def activeStatus(modeladmin,request,queryset):
    queryset.update(status=True)
    messages.success(request,"Selected record marked as active")

def inactiveStatus(modeladmin,request,queryset):
    queryset.update(status=False)
    messages.success(request,"Selected record marked as inactive")

#  Product Category admin config

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','status')
    list_filter = ('status','name')
    search_fields = ('name',)
    actions = (activeStatus,inactiveStatus)

admin.site.register(ProductCategory,ProductCategoryAdmin)

# #  Product admin Config
# class ProductImageAdmin(admin.TabularInline):
#     model = ProductImages
#     extra =1 
#     classes = ('collapse',)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImages
    extra =1 
    classes = ('collapse',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','product_category','stock','status']
    list_filter = ('product_category','status')
    search_fields = ['name','price']
    actions = (activeStatus,inactiveStatus)
    inlines = [ProductImageAdmin]

admin.site.register(Product,ProductAdmin)

admin.site.register(ProductImages)
