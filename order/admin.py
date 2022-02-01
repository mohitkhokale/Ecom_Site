from operator import mod
from django.contrib import admin , messages
from .models import Order, OrderDetail

# Register your models here.


def Mark_as_Pending(modeladmin,request,queryset):
    queryset.update(order_status="Pending")
    messages.success(request,"Selected record marked as Pending")

def Mark_as_InProgress(modeladmin,request,queryset):
    queryset.update(order_status="InProgress")
    messages.success(request,"Selected record marked as InProgress")

def Mark_as_Delivered(modeladmin,request,queryset):
    queryset.update(order_status="Delivered")
    messages.success(request,"Selected record marked as Delivered")

def Mark_as_Cancelled(modeladmin,request,queryset):
    queryset.update(order_status="Cancelled")
    messages.error(request,"Selected record marked as Cancelled")

class OrderDetailsInline(admin.StackedInline):
     model = OrderDetail
     extra = 1 

class OrderAdmin(admin.ModelAdmin):
    #  generic need to be written similar 

    list_display = ['user','name','date_time','order_status','payment_status']
    list_filter = ['order_status','payment_status']
    date_hierarchy = 'date_time'
    actions = [Mark_as_Pending,Mark_as_InProgress,Mark_as_Delivered,Mark_as_Cancelled]

admin.site.register(Order,OrderAdmin)
# admin.site.register(OrderDetail)


