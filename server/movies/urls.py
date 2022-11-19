from django.urls import path
from . import views, views_tmdb

app_name = 'movies'
urlpatterns = [
    path('select/', views.select, name='select'),
    path('like/', views.like_movie ,name='like_movie'),
    path('upcoming/', views_tmdb.get_upcoming_movie),
    # path('collection/', views.make_collection, name='collection'),
    # path('review/', views.review, name='review'),
    # path('worldcup/<int:num>/', views.worldcup, name='worldcup'),
    # path('test/', views.test, name='test'),
]