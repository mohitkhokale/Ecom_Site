from . import views
from django.urls import path



urlpatterns =[ 
    path('login/',views.Login.as_view(),name="login"),
    path('logout/',views.logout,name="logout"),
    path('', views.home_view, name="home"),
    # path('signup/',views.signup_view, name="signup")
    path('register/', views.signup_view, name='register'),
  

]