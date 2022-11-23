from django.urls import path
from . import views, views_tmdb

app_name = 'movies'
urlpatterns = [
    path('select/', views.select),
    path('<int:user_pk>/like/', views.like_movie,),
    path('<int:user_pk>/hate/', views.hate_movie),
    path('<int:movie_pk>/moviedetail/', views.moviedetail), # 영화 선택했을 때 나오는 상세 정보
    path('<int:movie_id>/review_create/', views.review_create),
    path('<int:comment_id>/review_update/', views.review_update),
    path('<int:comment_id>/review_block/', views.review_block),
    path('recommend/', views.recommend),
    path('upcoming/', views.upcoming),
    # path('get/upcoming/', views_tmdb.get_upcoming_movie),
    # path('get/recommend/', views_tmdb.get_recommend_movie),
    # path('get/similar/', views_tmdb.get_similar_movie),
    # path('collection/', views.make_collection, name='collection'),
    # path('review/', views.review, name='review'),
    # path('worldcup/<int:num>/', views.worldcup, name='worldcup'),
    # path('test/', views.test, name='test'),
]