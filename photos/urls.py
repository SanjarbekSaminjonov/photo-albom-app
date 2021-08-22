from django.contrib.auth import logout
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.gallery, name='gallery'),
    path('add/', views.addPhoto, name='add'),
    path('categories/', views.categoryManager, name='category_manager'),
    path('view-photo/<int:pk>/', views.viewPhoto, name='view_photo'),
    path('edit-photo/<int:pk>/', views.editPhoto, name='edit_photo'),
    path('delete-photo/<int:pk>/', views.deletePhoto, name='delete_photo'),
    path('delete-category/<int:pk>/', views.deleteCategory, name='delete_category'),
]
