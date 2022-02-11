from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard.as_view(),name="dashboard"),
]