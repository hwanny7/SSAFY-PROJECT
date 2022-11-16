from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieListSerializer
from .models import Movie, Genre, Actor



# Create your views here.

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        print('호',serializer)
        return Response(serializer.data)

    
