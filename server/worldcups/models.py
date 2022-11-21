from django.db import models
from movies.models import Movie
from django.conf import settings

# Create your models here.
class Worldcup(models.Model):
    movies = models.ManyToManyField(Movie)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)