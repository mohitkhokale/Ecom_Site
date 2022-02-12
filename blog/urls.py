from django.urls import path

from blog import views


urlpatterns = [
    path('blog/',views.Blogs.as_view(),name='blog'),
    path('blog/<int:blog_id>',views.Blogs.as_view(),name='blog'),
    path('blog-details/<int:blog_id>',views.blogdetails.as_view(),name='blogdetails'),
]