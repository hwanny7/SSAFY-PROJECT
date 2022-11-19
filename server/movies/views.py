from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieListSerializer, MovieSerializer, ReviewSerializer
from .models import Movie, Genre, Actor , Genre_count, Actor_count, Director_count, MovieReview
from django.contrib.auth import get_user_model

from pprint import pprint
import random

# 나중에 지울거
from django.http.response import JsonResponse


# Create your views here.

@api_view(['GET', 'POST'])
def select(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def like_movie(request):
    User = get_user_model()
    person = get_object_or_404(User, pk=3)

    # 좋아요 목록 보여주기
    if request.method == 'GET':
        movies = person.movie_set.all()
        if movies:
            serializer = MovieListSerializer(movies, many=True)
            return Response(serializer.data)
        else:
            return Response({'data':'없습니다.'})

    # 좋아요 추가 삭제.
    elif request.method == 'POST':
        select = request.data
        movie = get_object_or_404(Movie, pk=int(select['movie']))
        genres = movie.genres.all()
        actors = movie.actors.all()
        directors = movie.directors.all()

        # 영화를 좋아하는 사람 중에 유저가 있으면 -> 좋아요 취소
        if movie.like_users.filter(pk=person.pk).exists():
            movie.like_users.remove(person)
            for genre in genres:
                gen = Genre_count.objects.get(genre_id=genre.id, user_id=person.id)
                gen.cnt -=  1
                gen.save()

            
            for actor in actors:
                act = Actor_count.objects.get(actor_id=actor.id, user_id=person.id)
                act.cnt -= 1
                act.save()
                
            for director in directors:
                dir = Director_count.objects.get(director_id=director.id, user_id=person.id)
                dir.cnt -= 1
                dir.save()

        # 영화를 좋아하는 사람 중에 유저가 없으면 -> 좋아요
        else:
            movie.like_users.add(person)
            for genre in genres:
                if person.genre_count_set.filter(genre_id=genre.id, user_id=person.id).exists():
                    gen = Genre_count.objects.get(genre_id=genre.id, user_id=person.id)
                    gen.cnt = gen.cnt + 1
                    gen.save()
                    
                else:
                    person.genre_set.add(genre, through_defaults={'cnt':1})
            
            for actor in actors:
                if person.actor_set.filter(pk=actor.pk).exists():
                    act = Actor_count.objects.get(actor_id=actor.id, user_id=person.id)
                    act.cnt += 1
                    act.save()
                else:
                    person.actor_set.add(actor, through_defaults={'cnt':1})

            for director in directors:
                if person.director_set.filter(pk=director.pk).exists():
                    dir = Director_count.objects.get(director_id=director.id, user_id=person.id)
                    dir.cnt += 1
                    dir.save()
                else:
                    person.director_set.add(director, through_defaults={'cnt':1})

        if person.movie_set.all():
            serializer = MovieListSerializer(person.movie_set.all(), many=True)
            return Response(serializer.data)
        else:
            return Response({'data':'없습니다.'})

@api_view(['GET'])
def MovieInform(request):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=request.movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['POST'])
def review_create(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(moive=movie)
            return Response(serializer.data)
    
@api_view(['PUT', 'DELETE'])
def review_datail(request, comment_pk):
    review = get_object_or_404(MovieReview, pk=comment_pk)
    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    if request.method == 'DELETE':
        review.delete()
        return Response({'data':'삭제 완료'})
