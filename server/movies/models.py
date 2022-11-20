from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_genres')

class Actor(models.Model):
    name = models.CharField(max_length=50)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_actors')

class Director(models.Model):
    name = models.CharField(max_length=50)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_directors')

class genre_count():
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)



class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    youtube_key = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    actors = models.ManyToManyField(Actor)
    directors = models.ManyToManyField(Director)

class Worldcup(models.Model):
    movies = models.ForeignKey(Movie,on_delete=models.CASCADE)
    one_game = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    game = models.IntegerField(default=0)
    victory = models.IntegerField(default=0)
