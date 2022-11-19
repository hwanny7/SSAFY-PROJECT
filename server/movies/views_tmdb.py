from .models import UpcomingMovie
from django.http import JsonResponse, HttpResponse
import requests
from datetime import datetime
from pprint import pprint

API_KEY = '4e117d07b2367287ebca5cffeff8a553'
UPCOMING_MOVIE_URL = 'https://api.themoviedb.org/3/movie/upcoming'

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

