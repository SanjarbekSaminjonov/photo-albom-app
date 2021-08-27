from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(blank=False, null=True)
    description = models.TextField()

    def __str__(self):
        return self.description
