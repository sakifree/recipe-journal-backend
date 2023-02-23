from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    directions = models.TextField()