from django.db import models
from movies.models import Movie
from django.conf import settings



# Create your models here.
class Collection(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    open_public = models.BooleanField(default=False)
    movies = models.ManyToManyField(Movie, through='Movie_choice') # through 부분 확인하기
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_collection')


class Movie_choice(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField() #### blank True 로 변경하기
    # 유저도 넣어서 유저 확인 후 불러오기를 해야 할 것 같고, 만약에 비공개된 컬렉션에서 꺼내 오려고 한다면?

class Collection_Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    choice = models.ManyToManyField(Movie_choice)
    content = models.TextField(max_length=200)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_review')
    # movies = models.ForeignKey(Movie, on_delete=models.CASCADE) # movie_chocie를 가져오기
    # hate_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='hate_reviews')
    # is_active = models.BooleanField(default=True)
    # 두개 삭제하기