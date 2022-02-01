from importlib.resources import path
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage.as_view(),name="Homepage"),
    path('ProductListing/',views.ProductListing.as_view(),name="ProductListing"),
    path('ProductListing/<int:product_category_id>',views.ProductListing.as_view(),name="ProductListing"),
    path('product-details/<int:product_id>',views.ProductDetails.as_view(),name="ProductDetails")
]
