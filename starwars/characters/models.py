from django.db import models
from django.db.models.base import Model

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=250, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name


class Planet(models.Model):
    name = models.CharField(max_length=250, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=250, unique=True, null=False, blank=False)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    opening_text = models.TextField(max_length=2000, blank=False, null=False)
    director_name = models.CharField(max_length=250, null=False, blank=False)
    planets = models.ManyToManyField(Planet, related_name='movies')
    characters = models.ManyToManyField(Character, related_name='movies')

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
