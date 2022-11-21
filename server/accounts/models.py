from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
# from imagekit.models import ProcessedImageField, ImageSpecField
# from imagekit.processors import ResizeToFill
# from imagekit.processors import Thumbnail

#email 넣으면 대상 컴퓨터 연결 거부 뜸
class User(AbstractUser):
    nickname = models.CharField(max_length=100)
    followings = models.ManyToManyField('self',symmetrical=False, related_name='followers')
    blockings = models.ManyToManyField('self',symmetrical=False)
    image = models.ImageField(blank=True)
    point = models.IntegerField(default= 0, validators=[MinValueValidator(0)])
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


# https://www.appsloveworld.com/django/100/149/django-rest-auth-custom-register-serializer-not-saving-custom-fields
# https://velog.io/@ready2start/DRF-djrestauth%EB%A1%9C-%EC%BB%A4%EC%8A%A4%ED%85%80-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0


    # img_url = models.CharField(max_length=10000)
    # format='JPEG',
    #     options={'quality': 70}