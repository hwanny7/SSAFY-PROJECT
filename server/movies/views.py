from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieListSerializer
from .models import Movie, Genre, Actor, Worldcup

from pprint import pprint
import random



# Create your views here.

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET','PUT'])
def worldcup(request, num):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        movie_lst = random.sample(movies, num)
        serializer = MovieListSerializer(movie_lst, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        winners = request.data.winners
        losers = request.data.losers
        for loser in losers:
            worldcup = winner.worldcup_set.all()
            worldcup.one_game += 1
            worldcup.game += 1

        for winner in winners:
            worldcup = winner.worldcup_set.all()
            worldcup.one_game += 1
            worldcup.win += 1

        if len(winners) == 1:
            worldcup = winners[0].worldcup_set.all()
            worldcup.victory += 1
            worldcup.game += 1
            # 여기다 유저에게 추천하는 알고리즘 함수 실행
            # return 최종결과
        else:
            serializer = MovieListSerializer(winners, many=True)
            return (serializer.data)
                        

    
