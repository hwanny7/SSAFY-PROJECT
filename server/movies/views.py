from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieListSerializer
from .models import Movie, Genre, Actor , Genre_count
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
    # 좋아요 목록 보여주기
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

        '''
        1. 좋아요를 누른 영화를 가지고 온다.
        '''
    # 좋아요를 생성한다.
    elif request.method == 'POST':
        User = get_user_model()
        select = request.data
        person = get_object_or_404(User, pk=int(select['user']))
        movie = get_object_or_404(Movie, pk=int(select['movie']))
        genres = movie.genres.all()

        for genre in genres:
            if person.genre_count_set.filter(genre_id=genre.id, user_id=person.id).exists():
                gen = Genre_count.objects.get(genre_id=genre.id, user_id=person.id)
                gen.cnt = gen.cnt + 1
                gen.save()
                
            else:
                print('여기?')
                person.genre_set.add(genre, through_defaults={'cnt':1})

        pass
        '''
        1. 새로 선택한 좋아요 누른 영화에서 장르, 배우, 감독을 가지고 온다.
        2. 데이터를 저장한다.
        '''
    elif request.method == 'PUT':
        pass
        '''
        1. 기존 좋아하는 데이터를 가지고 온다.
        2. 새로 선택한 좋아요 누른 영화에서 장르, 배우, 감독을 가지고 온다.
        3. 기존 데이터와 새로운 데이터를 결합한다.
        4. 데이터를 저장한다.
        '''
    elif request.method == 'DELETE':
        pass
        '''
        1. 없애려는 영화 정보를 가지고 온다.
        2. 그 영화의 데이터만큼 좋아하는 수치를 감소시킨다.
        '''






# @api_view(['GET','PUT'])
# def worldcup(request, num):
#     if request.method == 'GET':
#         movies = get_list_or_404(Movie)
#         movie_lst = random.sample(movies, num)
#         serializer = MovieListSerializer(movie_lst, many=True)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         winners = request.data.winners
#         losers = request.data.losers
#         for loser in losers:
#             worldcup = winner.worldcup_set.all()
#             worldcup.one_game += 1
#             worldcup.game += 1

#         for winner in winners:
#             worldcup = winner.worldcup_set.all()
#             worldcup.one_game += 1
#             worldcup.win += 1

#         if len(winners) == 1:
#             worldcup = winners[0].worldcup_set.all()
#             worldcup.victory += 1
#             worldcup.game += 1
#             # 여기다 유저에게 추천하는 알고리즘 함수 실행
#             # return 최종결과
#         else:
#             serializer = MovieListSerializer(winners, many=True)
#             return (serializer.data)
                        
# def top_rating_person_movie(request):
#     User = get_user_model
#     user = User.objects.all().order_by('-point')
# @api_view(['POST','PUT'])
# def make_collection(request):
#     # post는 collection 형태만 만들 때 필요
#     inform = request.data
#     if request.method == 'POST':
#         # print('확인', inform)
#         # print('출력', type(inform['open_public']))
#         # print('bool 확인용', bool(1))
#         # print('오류 원인', bool(int(inform['open_public'])))
#         User = get_user_model()
#         user = User.objects.get(pk=int(inform['user']))
#         print(user)
#         collection = Collection.objects.create(
#             user=user,
#             title=inform['title'], 
#             open_public = bool(int(inform['open_public'])),
#             content = inform['content'],
#             )
#         return

#     # PUT은 collection에 영화 추가할 때
#     if request.method == 'PUT':
#         collection = Collection.objects.get(pk=int(inform['collection']))
#         movie = Movie.objects.get(pk=int(inform['movie']))
#         collection.movies.add(movie, through_defaults={ 'content': inform['content'] })
#         return JsonResponse(collection, safe=False)

# def review(request):
#     pass


# def test(request):
#     collection = Collection.objects.get(pk=1)
#     choices = collection.movie_choice_set.all()

#     collection_json = []
#     for choice in choices:
#         a = {
#             'title': collection.title,
#             'content': collection.content,
#             'movie' : choice.movie_id,
#             'movies content': choice.content,
#         }
        
#         collection_json.append(a)
#     print(collection_json)
#     return JsonResponse(collection_json, safe=False)

