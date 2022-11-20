from rest_framework import serializers
from .models import Movie, MovieReview


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieReview
        fields = ('content', 'vote','user')
        read_only_fields = ('movies')


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'poster_path','id')

class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'