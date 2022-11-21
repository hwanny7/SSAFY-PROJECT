from django.urls import path
from . import views, views_tmdb

app_name = 'movies'
urlpatterns = [
    path('select/', views.select),
    path('like/', views.like_movie,),
    path('hate/', views.hate_movie),
    path('movieinform/', views.MovieInform), # 영화 선택했을 때 나오는 상세 정보
    path('<int:movie_id>/review_create/', views.review_create),
    path('<int:comment_id>/review_datail/', views.review_datail),
    path('recommend/', views.recommend),

    # path('get/movie/', views_tmdb.get_movie),
    # path('get/upcoming/', views_tmdb.get_upcoming_movie),
    # path('get/recommend/', views_tmdb.get_recommend_movie),
    path('get/similar/', views_tmdb.get_recommend_movie),
]