from django.urls import path
from . import views

urlpatterns = [
    path('update-user-profile/<int:pk>',views.UpdateUserProfile,name="UpdateUserProfile"),  
]