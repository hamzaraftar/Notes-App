from app import views
from django.urls import path
urlpatterns = [
    # get note
    path('note/', views.note_list ),
    path('note/<str:pk>/', views.note_detail),
    # create note
    path('note_create/', views.note_create),
    # update note
    path('note_update/<str:pk>/', views.note_complete_update),
    path('note_partial_update/<str:pk>/', views.note_partial_update),
    # delete note
    path('note_delete/<str:pk>/', views.note_delete),
    
]