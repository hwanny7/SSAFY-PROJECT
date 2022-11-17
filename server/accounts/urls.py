
from django.urls import path
from . import views

urlpatterns = [
    path('follow/<int:user_pk>/', views.follow),
    path('block/<int:user_pk>/', views.block),
]