from django.db import models
from movies.models import Movie
from django.conf import settings



# Create your models here.
class Collection(models.Model):
    '''
    1. 어떤 유저가 만들었지?
    2. 어떤 제목으로 만들은거야?
    3. 공개야 비공개야?
    4. 어떤 영화를 추가했어?
        3.1 어떤 이유로 영화를 추가한거야?
    5. 공개면 review도 만들어야겠네
    6. 
     '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    open_public = models.BooleanField(default=False)
    movies = models.ManyToManyField(Movie, through='Movie_choice')
    content = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_collection')

class Collection_Review(models.Model):
    users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movies = models.ForeignKey(Movie, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    content = models.TextField()
    hate_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='hate_reviews')
    is_active = models.BooleanField(default=True)


class Movie_choice(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    content = models.TextField()
    