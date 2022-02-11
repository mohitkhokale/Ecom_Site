from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.UserProfiles.as_view(),name="UserProfile"),
    path('updateprofile/',views.updateprofile.as_view(),name="updateprofile")
]