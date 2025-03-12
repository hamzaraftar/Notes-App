from app import views
from django.urls import path
urlpatterns = [
    # get blog
    path('blog/', views.blog_list ),
    path('blog/<str:pk>/', views.blog_detail),
    # create blog
    path('blog_create/', views.blog_create),
    # update blog
    path('blog_update/<str:pk>/', views.blog_complete_update),
    path('blog_partial_update/<str:pk>/', views.blog_partial_update),
    # delete blog
    path('blog_delete/<str:pk>/', views.blog_delete),
    
]