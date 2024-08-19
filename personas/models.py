from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class User(models.Model):
    favourite_movies = models.ManyToManyField(Movie, related_name='users', blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthdate = models.DateField()
    has_insurance = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"