from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # followings = models.ManyToManyField('self',symmetrical=False, related_name='followers')
    # 이건 차단 기능 때문에 미리 생성해둔거
    # blockings = models.ManyToManyField('self',symmetrical=False)
    # img_url = models.CharField(max_length=100)

    # point = models.IntegerField()
    # date_joined = models.DateTimeField(auto_now_add=True)
    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=True)
    pass
