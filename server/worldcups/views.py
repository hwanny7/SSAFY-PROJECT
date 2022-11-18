from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from movies.serializers import MovieListSerializer
from movies.models import Movie, Genre_count, Actor_count, Director_count
import random

# Create your views here.
@api_view(['GET','POST'])
def worldcup(request, num):
    User = get_user_model()
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        movie_lst = random.sample(movies, num)
        serializer = MovieListSerializer(movie_lst, many=True)
        print(serializer.data)
        return Response(serializer.data)

    elif request.method == 'POST':
        winners = request.data.winners
        losers = request.data['losers']
        winners = request.data['winners']
        print(request.data['losers'])
        for loser in losers:
            movie = Movie.objects.get(pk=loser['id'])
            movie.one_game += 1
            movie.game += 1
            movie.save()
        
        candidate = []
        for winner in winners:
            movie = Movie.objects.get(pk=winner['id'])
            candidate.append(MovieListSerializer(movie).data)

            if len(winners) <= 4:
                person = get_object_or_404(User, pk=request.user.pk)
                genres = movie.genres.all()
                actors = movie.actors.all()
                directors = movie.directors.all()
                for genre in genres:
                    if person.genre_count_set.filter(genre_id=genre.id, user_id=person.id).exists():
                        gen = Genre_count.objects.get(genre_id=genre.id, user_id=person.id)
                        gen.cnt +=  2**(5-len(winners)) - 1
                        gen.save()
                        
                    else:
                        person.genre_set.add(genre, through_defaults={'cnt':1})
                
                for actor in actors:
                    if person.actor_set.filter(pk=actor.pk).exists():
                        act = Actor_count.objects.get(actor_id=actor.id, user_id=person.id)
                        act.cnt += 2**(5-len(winners)) - 1
                        act.save()
                    else:
                        person.actor_set.add(actor, through_defaults={'cnt':1})

                for director in directors:
                    if person.director_set.filter(pk=director.pk).exists():
                        dir = Director_count.objects.get(director_id=director.id, user_id=person.id)
                        dir.cnt += 2**(5-len(winners)) - 1
                        dir.save()
                    else:
                        person.director_set.add(director, through_defaults={'cnt':1})

            movie.one_game += 1
            movie.game += 1
            if len(winners) == 1:
                movie.game += 1
                movie.victory += 1
            movie.save()
    
        return Response(candidate)
        
