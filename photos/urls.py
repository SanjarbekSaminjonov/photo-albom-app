from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('add/', views.addPhoto, name='add'),
    path('categories/', views.categoryManager, name='category_manager'),
    path('photo/<int:pk>/', views.viewPhoto, name='photo'),
    path('edit-photo/<int:pk>/', views.editPhoto, name='edit_photo'),
    path('delete-photo/<int:pk>/', views.deletePhoto, name='delete_photo'),
    path('delete-category/<int:pk>/', views.deleteCategory, name='delete_category'),
]
