from django.urls import path
from . import views, views_tmdb

app_name = 'movies'
urlpatterns = [
    path('select/', views.select),
    path('like/', views.like_movie,),
    path('hate/', views.hate_movie),
    path('movieinform/', views.MovieInform),
    path('<int:movie_id>/review_create/', views.review_create),
    path('recommend/', views.recommend),
    # path('get/upcoming/', views_tmdb.get_upcoming_movie),
    # path('get/recommend/', views_tmdb.get_recommend_movie),
    # path('get/similar/', views_tmdb.get_similar_movie),
    # path('collection/', views.make_collection, name='collection'),
    # path('review/', views.review, name='review'),
    # path('worldcup/<int:num>/', views.worldcup, name='worldcup'),
    # path('test/', views.test, name='test'),
]