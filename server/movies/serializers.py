from rest_framework import serializers
from .models import (Movie, MovieReview, Actor, Genre, Director)




class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name',)

class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ('name',)

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieReview
        fields = ('id','content', 'vote', 'created_at','movies','user')
        read_only_fields = ('movies','user',)
        

# 이건 전체를 주는 serializer
class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'poster_path','id')

# recommend, similar movie 포장할 serializer
class RSMovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('id','title','poster_path',)
    
# 영환 하나 골랐을 때 주는 serializer
class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)
    actors = DirectorSerializer(many=True)
    directors = DirectorSerializer(many=True)
    recommendmovie = RSMovieSerializer(many=True)
    similarmovie = RSMovieSerializer(many=True)
    review_set = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)

    class Meta:
        model = Movie
        exclude = ('one_game', 'win', 'game', 'victory')