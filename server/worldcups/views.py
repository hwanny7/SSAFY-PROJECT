from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Worldcup
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
            l_movie = Movie.objects.get(pk=loser['id'])
            l_movie.one_game += 1
            l_movie.game += 1
            l_movie.save()
        
        candidate = []
        for winner in winners:
            w_movie = Movie.objects.get(pk=winner['id'])
            candidate.append(MovieListSerializer(w_movie).data)

            if len(winners) <= 4:
                person = get_object_or_404(User, pk=request.user.pk)
                genres = w_movie.genres.all()
                actors = w_movie.actors.all()
                directors = w_movie.directors.all()
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

            w_movie.one_game += 1
            w_movie.game += 1
            if len(winners) == 1:
                worldcup = Worldcup.user.get(id=request.user.id)
                if not worldcup.movies.filter(pk=w_movie.pk).exists():
                    worldcup.movies.add(w_movie)
                if not worldcup.movies.filter(pk=l_movie.pk).exists():
                    worldcup.movies.add(l_movie)

                w_movie.game += 1
                w_movie.victory += 1
            w_movie.save()
    
        return Response(candidate)
        
