from .models import UpcomingMovie, Movie, RecommendMovie, SimilarMovie, Director, Actor
from django.http import JsonResponse, HttpResponse
import requests
from datetime import datetime
from pprint import pprint

API_KEY = '4e117d07b2367287ebca5cffeff8a553'
UPCOMING_MOVIE_URL = 'https://api.themoviedb.org/3/movie/upcoming'
RECOMMEND_MOVIE_URL = 'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'


def get_youtube_key(movie_dict):    
    movie_id = movie_dict.get('id')
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/videos',
        params={
            'api_key': API_KEY
        }
    ).json()
    for video in response.get('results'):
        if video.get('site') == 'YouTube':
            return video.get('key')
    return 'nothing'

def get_actors(movie):
    movie_id = movie.id
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}/credits',
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',
        }
    ).json()
    
    for person in response.get('crew'):
        if person.get('department') != 'Directing': continue
        director_id = person.get('id')
        if not Director.objects.filter(pk=director_id).exists():
            director = Director.objects.create(
                id=person.get('id'),
                name=person.get('name')
            )
            movie.directors.add(director.id)
            if movie.directors.count() == 2:
                break

    for person in response.get('cast'):
        if person.get('known_for_department') != 'Acting': continue
        actor_id = person.get('id')
        if not Actor.objects.filter(pk=actor_id).exists():
            actor = Actor.objects.create(
                id=person.get('id'),
                name=person.get('name')
            )
            movie.actors.add(actor.id)
            if movie.actors.count() == 5:       # 5명의 배우 정보만 저장
                break

def movie_data(page=1):
    response = requests.get(
        UPCOMING_MOVIE_URL,
        params={
            'api_key': API_KEY,
            'language': 'ko-KR',
            'page': page,       
        }
    ).json()

    for movie_dict in response.get('results'):
        if not movie_dict.get('release_date'): continue   # 없는 필드 skip
        if not movie_dict.get('poster_path'): continue
        if movie_dict.get('original_language') not in ['ko', 'en']: continue

        release_date = movie_dict.get('release_date')
        year = int(release_date[0:4])
        month = int(release_date[5:7])
        day = int(release_date[8:10])
        now = datetime.now()

        if (year < now.year) or (month < now.month) or (day < now.day): continue
        # 유투브 key 조회
        youtube_key = get_youtube_key(movie_dict)

        movie = UpcomingMovie.objects.create(
            id=movie_dict.get('id'),
            title=movie_dict.get('title'),
            release_date=movie_dict.get('release_date'),
            overview=movie_dict.get('overview'),
            poster_path=movie_dict.get('poster_path'),   
            youtube_key=youtube_key         
        )
        for genre_id in movie_dict.get('genre_ids', []):
            movie.genres.add(genre_id)

def get_upcoming_movie(request):
    if UpcomingMovie.objects.all().exists():
        # if UpcomingMovie.objects.get(pk=)
        UpcomingMovie.objects.all().delete()
        get_upcoming_movie(request)
    else:
        for i in range(1, 20):
            movie_data(i)
    return HttpResponse('OK >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


def movie_data2(mode, page=1):
    movies = Movie.objects.all()
    for movie in movies:
        if mode == 'recommend':
            URL = f'https://api.themoviedb.org/3/movie/{movie.id}/recommendations'
            model = RecommendMovie
        else:
            URL = f'https://api.themoviedb.org/3/movie/{movie.id}/similar'
            model = SimilarMovie

        response = requests.get(
            URL,
            params={
            'api_key': API_KEY,
            'language': 'ko-KR',
            'page': page,       
        }).json()

        for movie_dict in response.get('results'):
            if not movie_dict.get('release_date'): continue   # 없는 필드 skip
            if not movie_dict.get('poster_path'): continue
            youtube_key = get_youtube_key(movie_dict)

            if model.objects.filter(pk=movie_dict.get('id')).exists():
                n_movie = model.objects.get(pk=movie_dict.get('id'))
                n_movie.movie.add(movie)
                continue
        
            new_movie = model.objects.create(
                id=movie_dict.get('id'),
                title=movie_dict.get('title'),
                popularity=movie_dict.get('popularity'),
                vote_count=movie_dict.get('vote_count'),
                vote_average=movie_dict.get('vote_average'),
                release_date=movie_dict.get('release_date'),
                overview=movie_dict.get('overview'),
                poster_path=movie_dict.get('poster_path'),   
                youtube_key=youtube_key,     
            )
            new_movie.movie.add(movie)
                

            get_actors(new_movie)
            for genre_id in movie_dict.get('genre_ids', []):
                new_movie.genres.add(genre_id)

            print(new_movie.title)


def get_recommend_movie(request):
    RecommendMovie.objects.all().delete()
    for page in range(1,3):
        movie_data2('recommend', page)

    SimilarMovie.objects.all().delete()
    for page in range(1,3):
        movie_data2('similar')
    return HttpResponse('OK!!!!!!!!!!!!!!!!!!')

def get_similar_movie(request):
    pass
    return HttpResponse('OK!!!!!!!!!!!!!!!!!!')