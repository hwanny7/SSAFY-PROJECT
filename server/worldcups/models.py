from django.db import models
from movies.models import Movie

# Create your models here.
class Worldcup(models.Model):
    movies = models.ForeignKey(Movie,on_delete=models.CASCADE)
    one_game = models.IntegerField(default=0)
    win = models.IntegerField(default=0)
    game = models.IntegerField(default=0)
    victory = models.IntegerField(default=0)