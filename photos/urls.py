from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('add/', views.addPhoto, name='add'),
    path('photo/<int:pk>/', views.viewPhoto, name='photo'),
]
