from .models import UpcomingMovie, Movie, Director, Actor, Genre
from django.http import JsonResponse, HttpResponse
import requests
from datetime import datetime
from pprint import pprint

API_KEY = '4e117d07b2367287ebca5cffeff8a553'

GENRE_URL = 'https://api.themoviedb.org/3/genre/movie/list'
POPULAR_MOVIE_URL = 'https://api.themoviedb.org/3/movie/popular'

UPCOMING_MOVIE_URL = 'https://api.themoviedb.org/3/movie/upcoming'
RECOMMEND_MOVIE_URL = 'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'

def tmdb_genres():
    response = requests.get(
        GENRE_URL,
        params={
            'api_key': API_KEY,
            'language': 'ko-KR',            
        }
    ).json()    
    for genre in response.get('genres'):
        if Genre.objects.filter(pk=genre['id']).exists(): continue        
        Genre.objects.create(
            id=genre['id'],
            name=genre['name']
        )
    return JsonResponse(response)

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
        movie.directors.add(director_id)
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
        movie.actors.add(actor_id)
        if movie.actors.count() == 5:       # 5명의 배우 정보만 저장
            break

def movie_data(page=1):
    response = requests.get(
        POPULAR_MOVIE_URL,
        params={
            'api_key': API_KEY,
            'language': 'ko-kr',     
            'page': page,       
        }
    ).json()

    for movie_dict in response.get('results'):
        if not movie_dict.get('release_date'): continue   # 없는 필드 skip
        # 유투브 key 조회
        youtube_key = get_youtube_key(movie_dict)
        if Movie.objects.filter(pk=movie_dict.get('id')).exists(): continue
        movie = Movie.objects.create(
            adult = movie_dict.get('adult'),
            id=movie_dict.get('id'),
            title=movie_dict.get('title'),
            release_date=movie_dict.get('release_date'),
            popularity=movie_dict.get('popularity'),
            vote_count=movie_dict.get('vote_count'),
            vote_average=movie_dict.get('vote_average'),
            overview=movie_dict.get('overview'),
            poster_path=movie_dict.get('poster_path'),   
            youtube_key=youtube_key         
        )
        for genre_id in movie_dict.get('genre_ids', []):
            movie.genres.add(genre_id)

        # 배우들 저장
        get_actors(movie)
        print('>>>', movie.title, '==>', movie.youtube_key)    

def upcoming_movie_data(page=1):
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
        if youtube_key == 'nothing':
            continue
        cnt = len(UpcomingMovie.objects.all())
        if cnt > 10:
            return
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
        get_actors(movie)
        print('>>>', movie.title, '==>', movie.youtube_key)


def recommend_movie_data(mode, page=1):

    movies = Movie.objects.all()
    for movie in movies:
        if mode == 'recommend':
            URL = f'https://api.themoviedb.org/3/movie/{movie.id}/recommendations'
            model = Movie.recommendmovie
        else:
            URL = f'https://api.themoviedb.org/3/movie/{movie.id}/similar'
            model = Movie.similarmovie

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

            find = Movie.objects.filter(pk=movie_dict.get('id'))
            
            if find:
                movie.recommendmovie.add(find[0])
                print('오류2')
                print(movie.title)
           
def get_upcoming_movie(request):
    if UpcomingMovie.objects.all().exists():

        UpcomingMovie.objects.all().delete()
        get_upcoming_movie(request)
    else:
        for i in range(1, 30):
            upcoming_movie_data(i)
    return HttpResponse('OK >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

def get_recommend_movie(request):
   
    for page in range(1,2):
        recommend_movie_data('recommend', page)

    for page in range(1,2):
        recommend_movie_data('similar', page)
    return HttpResponse('OK!!!!!!!!!!!!!!')

def get_movie(request):
    Genre.objects.all().delete()
    Actor.objects.all().delete()
    Movie.objects.all().delete()
    Director.objects.all().delete()

    tmdb_genres()
    for i in range(1, 60):
        movie_data(i)
    
    return HttpResponse('OK >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')