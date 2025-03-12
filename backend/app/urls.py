from app import views
from django.urls import path
urlpatterns = [
    path('blogs/', views.blog_list, name='blog_list'),
    path('blog_create/', views.blog_create, name='blog_create'),
    
]