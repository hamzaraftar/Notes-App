from app import views
from django.urls import path
urlpatterns = [
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<str:pk>/', views.blog_detail, name='blog_detail'),

    path('blog_create/', views.blog_create, name='blog_create'),

    path('blog_update/<str:pk>/', views.blog_complete_update, name='blog_update'),
    path('blog_partial_update/<str:pk>/', views.blog_partial_update, name='blog_partial_update'),
    
]