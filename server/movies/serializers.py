from rest_framework import serializers
from .models import Movie, Actor, Director, Genre



class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'poster_path','id')
