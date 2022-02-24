from re import search
from django.contrib import admin
from .models import Cart, Couponcode
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ['user','product','quantity']
    search_fields = ['product__name','user__first_name']


admin.site.register(Cart,CartAdmin)



class CouponcodeAdmin(admin.ModelAdmin):
    list_display = ['id', 'coupon_name', 'amount','status',]
 
# Register your models here.
admin.site.register(Couponcode,CouponcodeAdmin)