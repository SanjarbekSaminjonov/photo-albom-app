from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('add/', views.addPhoto, name='add'),
    path('categories/', views.categoryManager, name='category_manager'),
    path('photo/<int:pk>/', views.viewPhoto, name='photo'),
    path('delete/<int:pk>/', views.deletePhoto, name='delete'),
    path('delete_category/<int:pk>/', views.deleteCategory, name='delete_category'),
]
