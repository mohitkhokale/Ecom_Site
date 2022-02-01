from re import search
from django.contrib import admin
from .models import Cart
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ['user','product','quantity']
    search_fields = ['product__name','user__first_name']


admin.site.register(Cart,CartAdmin)
