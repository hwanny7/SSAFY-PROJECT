from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieListSerializer, MovieSerializer, ReviewSerializer, RSMovieSerializer, UpcomingMovieSerializer, GenreSerializer
from .models import Movie, Genre, Actor , Genre_count, Actor_count, Director_count, MovieReview, UpcomingMovie
from worldcups.models import Worldcup
from django.contrib.auth import get_user_model
from pprint import pprint
# 나중에 지울거
import random
from django.http.response import JsonResponse


# Create your views here.
User = get_user_model()

############################## 여기 수정해야함 ######################################
@api_view(['GET', 'POST'])
def select(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

# like_movie, hate_movie는 안 펼치는게 정신 건강에 좋음....
@api_view(['GET', 'POST'])
def like_movie(request, user_pk):
    person = get_object_or_404(User, pk=user_pk)

    # 좋아요 목록 보여주기
    if request.method == 'GET':
        movies = person.like_movies.all()
        if movies:
            serializer = MovieListSerializer(movies, many=True)
            return Response(serializer.data)
        else:
            return Response(['없음'])

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
                movie.hate_users.remove(person)
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
            return Response(['없음'])

@api_view(['GET', 'POST'])
def hate_movie(request, user_pk):
    person = get_object_or_404(User, pk=user_pk)

    # 좋아요 목록 보여주기
    if request.method == 'GET':
        movies = person.hate_movies.all()
        if movies:
            serializer = MovieListSerializer(movies, many=True)
            return Response(serializer.data)
        else:
            return Response(['없음'])

    # 싫어요 추가 삭제.
    elif request.method == 'POST':
        select = request.data
        movie = get_object_or_404(Movie, pk=int(select['movie']))
        genres = movie.genres.all()
        actors = movie.actors.all()
        directors = movie.directors.all()

        # 영화를 싫어하는 사람 중에 유저가 있으면 -> 싫어요 취소
        if movie.hate_users.filter(pk=person.pk).exists():
            movie.hate_users.remove(person)
            for genre in genres:
                gen = Genre_count.objects.get(genre_id=genre.id, user_id=person.id)
                gen.cnt +=  5
                gen.save()

            
            for actor in actors:
                act = Actor_count.objects.get(actor_id=actor.id, user_id=person.id)
                act.cnt += 5
                act.save()
                
            for director in directors:
                dir = Director_count.objects.get(director_id=director.id, user_id=person.id)
                dir.cnt += 5
                dir.save()

        # 영화를 싫어하는 사람 중에 유저가 없으면 -> 싫어요
        else:
            if movie.like_users.filter(pk=person.pk).exists():
                movie.like_users.remove(person)
            movie.hate_users.add(person)
            for genre in genres:
                if person.genre_count_set.filter(genre_id=genre.id, user_id=person.id).exists():
                    gen = Genre_count.objects.get(genre_id=genre.id, user_id=person.id)
                    gen.cnt = gen.cnt - 5
                    gen.save()
                    
                else:
                    person.genre_set.add(genre, through_defaults={'cnt':-5})
            
            for actor in actors:
                if person.actor_set.filter(pk=actor.pk).exists():
                    act = Actor_count.objects.get(actor_id=actor.id, user_id=person.id)
                    act.cnt -= 5
                    act.save()
                else:
                    person.actor_set.add(actor, through_defaults={'cnt':-5})

            for director in directors:
                if person.director_set.filter(pk=director.pk).exists():
                    dir = Director_count.objects.get(director_id=director.id, user_id=person.id)
                    dir.cnt -= 5
                    dir.save()
                else:
                    person.director_set.add(director, through_defaults={'cnt':-5})

        if person.hate_movies.all():
            serializer = MovieListSerializer(person.hate_movies.all(), many=True)
            return Response(serializer.data)
        else:
            return Response(['없음'])

@api_view(['GET'])
def moviedetail(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['GET','POST'])
def review_create(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        reviews = movie.moviereview_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(movies=movie, user=user)
            return Response(serializer.data)
    
@api_view(['PUT', 'DELETE'])
def review_update(request, comment_id):
    review = get_object_or_404(MovieReview, pk=comment_id)
    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    if request.method == 'DELETE':
        if request.user.pk == review.user.pk :
            review.delete()
            return Response({'data':'삭제 완료'})
        return Response({'data':'삭제할 수 없습니다.'})

@api_view(['POST'])
def review_block(request, comment_id):
    if request.method == 'POST':
        review = get_object_or_404(MovieReview, pk=comment_id)

        if request.user.pk != review.user.pk :
            review.block_users.add(request.user)
            return Response({'data':'차단완료'})

@api_view(['GET'])
def recommend(request):
    person = get_object_or_404(User, pk=request.user.pk)

    worldcup = person.worldcup_set.all()
    worldcup_movies = []
    if worldcup:
        worldcup_movies = worldcup[0].movies.all()
    like_movies = person.like_movies.all()
    hate_movies = person.hate_movies.all()
    
    if len(worldcup_movies) + len(like_movies) < 3:
        return Response(['없음'])

    # 좋아요 누른 영화랑 비슷한 영화
    Candidate ={}
    for movie in like_movies:
        recommend_movies = movie.recommendmovie.all()
        similar_movies = movie.similarmovie.all()

        for rmovie in recommend_movies:
            point = Candidate.get(rmovie.id, 0)
            if point:
                point = point[0] + 5
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
                    point += Actor_count.objects.filter(user_id=request.user.id, actor_id=actor.id)[0].cnt
                    
            for director in directors:
                if Director_count.objects.filter(user_id=request.user.id, director_id=director.id).exists():
                    point += Director_count.objects.filter(user_id=request.user.id, director_id=director.id)[0].cnt
            
            Candidate[rmovie.id] = [point]

        for smovie in similar_movies:
            point = Candidate.get(rmovie.id, 0)
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
            
            Candidate[smovie.id] = [point]

    for movie in worldcup_movies:
            recommend_movies = movie.recommendmovie.all()
            similar_movies = movie.similarmovie.all()

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
                
                Candidate[rmovie.id] = [point]

            for smovie in similar_movies:
                point = Candidate.get(rmovie.id, 0)
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
                
                Candidate[smovie.id] = [point]

    for movie in hate_movies:
        if Candidate.get(movie.id, 0):
            del(Candidate[movie.id])

        similar_movies = movie.similarmovie.all()
        for smovie in similar_movies:
            if Candidate.get(movie.id, 0):
                del(Candidate[movie.id])
    print('사이1')        
    print(list(Candidate.items()))
    print('사이2')
    movie_list = sorted(Candidate.items(), key=lambda x: x[1][0],reverse=True)
    if len(movie_list) > 20:
        movie_list = movie_list[:20]
    res = []
    for info in movie_list:
        res.append(Movie.objects.get(pk=info[0]))
    if res:
        serializer = RSMovieSerializer(res, many=True)
        return Response(serializer.data)

    return Response('없음')

@api_view(['GET'])
def upcoming(request):
    if request.method == 'GET':
        upcomingmovies = get_list_or_404(UpcomingMovie)
        print(upcomingmovies)
        serializer = UpcomingMovieSerializer(upcomingmovies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_genre(request):
    genres = get_list_or_404(Genre)
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)