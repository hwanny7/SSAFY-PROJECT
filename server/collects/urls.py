from django.urls import path
from . import views

urlpatterns =[
    path('collection/', views.collection), # 내가 생선한 컬렉션 요청과 생성
    path('revise/<int:collection_pk>', views.onecollection),
    path('update/<int:collection_pk>/', views.update), # 내가 생선한 컬렉션 수정과 삭제
    path('like/<int:collection_pk>/', views.like), # 해당 컬렉션 좋아요
    path('review/<int:collection_pk>/', views.Review), # 해당 컬렉션 댓글
    path('review/create/', views.Review_create),
    path('review/delete/<int:review_pk>/', views.Review_delete),
    path('mycollection/<int:user_pk>/', views.mycollection),
]