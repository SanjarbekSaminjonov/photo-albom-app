from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE)
    image = models.ImageField(blank=False, null=True)
    description = models.TextField()

    def __str__(self):
        return self.description
