from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieListSerializer, MovieSerializer, ReviewSerializer
from .models import Movie, Genre, Actor , Genre_count, Actor_count, Director_count, MovieReview, RecommendMovie, SimilarMovie
from worldcups.models import Worldcup
from django.contrib.auth import get_user_model
from pprint import pprint
import random
# 나중에 지울거
from django.http.response import JsonResponse


# Create your views here.
User = get_user_model()

@api_view(['GET', 'POST'])
def select(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

# like_movie, hate_movie는 안 펼치는게 정신 건강에 좋음....
@api_view(['GET', 'POST'])
def like_movie(request):
    person = get_object_or_404(User, pk=request.user.pk)

    # 좋아요 목록 보여주기
    if request.method == 'GET':
        movies = person.like_movies.all()
        if movies:
            serializer = MovieListSerializer(movies, many=True)
            return Response(serializer.data)
        else:
            return Response({'data':'좋아요를 누른 영화가없습니다.'})

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
                gen.cnt -=  5
                gen.save()

            
            for actor in actors:
                act = Actor_count.objects.get(actor_id=actor.id, user_id=person.id)
                act.cnt -= 5
                act.save()
                
            for director in directors:
                dir = Director_count.objects.get(director_id=director.id, user_id=person.id)
                dir.cnt -= 5
                dir.save()

        # 영화를 좋아하는 사람 중에 유저가 없으면 -> 좋아요
        else:
            if movie.hate_users.filter(pk=person.pk).exists():
                movie.like_users.remove(person)
            movie.like_users.add(person)
            for genre in genres:
                if person.genre_count_set.filter(genre_id=genre.id, user_id=person.id).exists():
                    gen = Genre_count.objects.get(genre_id=genre.id, user_id=person.id)
                    gen.cnt = gen.cnt + 5
                    gen.save()
                    
                else:
                    person.genre_set.add(genre, through_defaults={'cnt':5})
            
            for actor in actors:
                if person.actor_set.filter(pk=actor.pk).exists():
                    act = Actor_count.objects.get(actor_id=actor.id, user_id=person.id)
                    act.cnt += 5
                    act.save()
                else:
                    person.actor_set.add(actor, through_defaults={'cnt':5})

            for director in directors:
                if person.director_set.filter(pk=director.pk).exists():
                    dir = Director_count.objects.get(director_id=director.id, user_id=person.id)
                    dir.cnt += 5
                    dir.save()
                else:
                    person.director_set.add(director, through_defaults={'cnt':5})

        if person.like_movies.all():
            serializer = MovieListSerializer(person.like_movies.all(), many=True)
            return Response(serializer.data)
        else:
            return Response({'data':'없습니다.'})

@api_view(['GET', 'POST'])
def hate_movie(request):
    person = get_object_or_404(User, pk=request.user.pk)

    # 좋아요 목록 보여주기
    if request.method == 'GET':
        movies = person.hate_movies.all()
        if movies:
            serializer = MovieListSerializer(movies, many=True)
            return Response(serializer.data)
        else:
            return Response({'data':'싫어요를 누른 영화가 없습니다.'})

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
                gen.cnt +=  10
                gen.save()

            
            for actor in actors:
                act = Actor_count.objects.get(actor_id=actor.id, user_id=person.id)
                act.cnt += 10
                act.save()
                
            for director in directors:
                dir = Director_count.objects.get(director_id=director.id, user_id=person.id)
                dir.cnt += 10
                dir.save()

        # 영화를 좋아하는 사람 중에 유저가 없으면 -> 좋아요
        else:
            if movie.like_users.filter(pk=person.pk).exists():
                movie.hate_users.remove(person)
            movie.like_users.add(person)
            for genre in genres:
                if person.genre_count_set.filter(genre_id=genre.id, user_id=person.id).exists():
                    gen = Genre_count.objects.get(genre_id=genre.id, user_id=person.id)
                    gen.cnt = gen.cnt - 10
                    gen.save()
                    
                else:
                    person.genre_set.add(genre, through_defaults={'cnt':-10})
            
            for actor in actors:
                if person.actor_set.filter(pk=actor.pk).exists():
                    act = Actor_count.objects.get(actor_id=actor.id, user_id=person.id)
                    act.cnt -= 10
                    act.save()
                else:
                    person.actor_set.add(actor, through_defaults={'cnt':-10})

            for director in directors:
                if person.director_set.filter(pk=director.pk).exists():
                    dir = Director_count.objects.get(director_id=director.id, user_id=person.id)
                    dir.cnt -= 10
                    dir.save()
                else:
                    person.director_set.add(director, through_defaults={'cnt':-10})

        if person.hate_movies.all():
            serializer = MovieListSerializer(person.hate_movies.all(), many=True)
            return Response(serializer.data)
        else:
            return Response({'data':'없습니다.'})

@api_view(['GET'])
def MovieInform(request):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=request.data.movie_pk)
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


@api_view(['GET'])
def recommend(request):
    person = get_object_or_404(User, pk=request.user.pk)
    user_worldcup = Worldcup.user.get(pk=person.pk)


    worldcup_movies = user_worldcup.movies.all()
    like_movies = person.like_movies.all()
    hate_movies = person.hate_movies.all()
    

    # 좋아요 누른 영화랑 비슷한 영화
    Candidate ={}
    for movie in like_movies:
        recommend_movies = movie.recommendMovie_set.all()
        similar_movies = movie.similarmMovie_set.all()

        for rmovie in recommend_movies:
            point = Candidate.get(rmovie.id, 0)
            if point:
                point = point[0]
            else:
                point = 5

            genres = rmovie.genres.all()
            actors = rmovie.actors.all()
            directors = rmovie.directors.all()
            for genre in genres:
                if Genre_count.objects.filter(user_id=request.user.id, genre_id=genre.id).exists():
                    point += Genre_count.objects.filter(user_id=request.user.id, genre_id=genre.id)[0].cnt
                    
            for actor in actors:
                if Actor_count.objects.filter(user_id=request.user.id, actor_id=actor.id).exists():
                    point += Genre_count.objects.filter(user_id=request.user.id, actor_id=actor.id)[0].cnt
                    
            for director in directors:
                if Director_count.objects.filter(user_id=request.user.id, director_id=director.id).exists():
                    point += Director_count.objects.filter(user_id=request.user.id, director_id=director.id)[0].cnt
            
            Candidate[rmovie.id] = [point, rmovie.id, RecommendMovie]

        for smovie in similar_movies:
            if point:
                point = point[0]
            else:
                point = 5
            genres = smovie.genres.all()
            actors = smovie.actors.all()
            directors = smovie.directors.all()
            for genre in genres:
                if Genre_count.objects.filter(user_id=request.user.id, genre_id=genre.id).exists():
                    point += Genre_count.objects.filter(user_id=request.user.id, genre_id=genre.id)[0].cnt
                    
            for actor in actors:
                if Actor_count.objects.filter(user_id=request.user.id, actor_id=actor.id).exists():
                    point += Actor_count.objects.filter(user_id=request.user.id, actor_id=actor.id)[0].cnt
                    
            for director in directors:
                if Director_count.objects.filter(user_id=request.user.id, director_id=director.id).exists():
                    point += Director_count.objects.filter(user_id=request.user.id, director_id=director.id)[0].cnt
            
            Candidate[smovie.id] = [point, smovie.id, SimilarMovie]

    for movie in worldcup_movies:
            recommend_movies = movie.recommendMovie_set.all()
            similar_movies = movie.similarmMovie_set.all()

            for rmovie in recommend_movies:
                point = Candidate.get(rmovie.id, 0)
                if point:
                    point = point[0]
                else:
                    point = 5

                genres = rmovie.genres.all()
                actors = rmovie.actors.all()
                directors = rmovie.directors.all()
                for genre in genres:
                    if Genre_count.objects.filter(user_id=request.user.id, genre_id=genre.id).exists():
                        point += Genre_count.objects.filter(user_id=request.user.id, genre_id=genre.id)[0].cnt
                        
                for actor in actors:
                    if Actor_count.objects.filter(user_id=request.user.id, actor_id=actor.id).exists():
                        point += Genre_count.objects.filter(user_id=request.user.id, actor_id=actor.id)[0].cnt
                        
                for director in directors:
                    if Director_count.objects.filter(user_id=request.user.id, director_id=director.id).exists():
                        point += Director_count.objects.filter(user_id=request.user.id, director_id=director.id)[0].cnt
                
                Candidate[rmovie.id] = [point, rmovie.id, RecommendMovie]

            for smovie in similar_movies:
                if point:
                    point = point[0]
                else:
                    point = 5
                genres = smovie.genres.all()
                actors = smovie.actors.all()
                directors = smovie.directors.all()
                for genre in genres:
                    if Genre_count.objects.filter(user_id=request.user.id, genre_id=genre.id).exists():
                        point += Genre_count.objects.filter(user_id=request.user.id, genre_id=genre.id)[0].cnt
                        
                for actor in actors:
                    if Actor_count.objects.filter(user_id=request.user.id, actor_id=actor.id).exists():
                        point += Actor_count.objects.filter(user_id=request.user.id, actor_id=actor.id)[0].cnt
                        
                for director in directors:
                    if Director_count.objects.filter(user_id=request.user.id, director_id=director.id).exists():
                        point += Director_count.objects.filter(user_id=request.user.id, director_id=director.id)[0].cnt
                
                Candidate[smovie.id] = [point, smovie.id, SimilarMovie]

    for movie in hate_movies:
        if Candidate.get(movie.id, 0):
            del(Candidate[movie.id])

        similar_movies = movie.similarmMovie_set.all()
        for smovie in similar_movies:
            if Candidate.get(movie.id, 0):
                del(Candidate[movie.id])
            
    movie_list = sorted(Candidate.values(), lambda x : x[0], reverse=True)

    res = []
    for info in movie_list:
        if info[0] >= 0:
            movie = info[2].objects.get(pk=info[1])
            res.append(movie)
        
    serializer = MovieSerializer(res, many=True)
    return Response(serializer.data)




