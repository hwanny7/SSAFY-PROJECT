from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Genre_count')

class Genre_count(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cnt = models.IntegerField(default = 0)

class Actor(models.Model):
    name = models.CharField(max_length=50)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Actor_count')

class Actor_count(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cnt = models.IntegerField(default = 0)

class Director(models.Model):
    name = models.CharField(max_length=50)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Director_count')

class Director_count(models.Model):
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cnt = models.IntegerField(default = 0)

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
    one_game = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    game = models.IntegerField(default=0)
    victory = models.IntegerField(default=0)

class UpcomingMovie(models.Model):
    updated_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    youtube_key = models.CharField(max_length=100)

class RecommendedMovie(models.Model):
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
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE)

class MovieReview(models.model):
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    vote = models.IntegerField()
    block_users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    banned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DatetimeField(auto_now=True)