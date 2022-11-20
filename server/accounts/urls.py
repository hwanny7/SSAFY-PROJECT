
from django.urls import path
from . import views

urlpatterns = [
    path('follow/', views.follow),
    path('block/<int:user_pk>/', views.block),
    path('profile/<int:user_pk>/', views.profile),
]