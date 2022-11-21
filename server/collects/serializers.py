from rest_framework import serializers
from .models import Collection, Collection_Review, Movie_choice
from movies.models import Movie
from accounts.models import User
from accounts.serializers import CustomUserDetailsSerializer

# user = CustomUserDetailsSerializer() >> 다른 사람들 목록도 다 보여줄 때는 user 닉네임이나 이런 것도 같이 보여줄 때 쓰기 (field값 조정해야함)


# class MovieChoiceSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Movie_choice
#         fields = ('content',)

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('nickname', 'image', 'id')


class CollectionReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Collection_Review
        fields = ('__all__')
        read_only_fields = ('user', 'choice', 'collection', 'like_users')



class CollectionSerializer(serializers.ModelSerializer):

    movies = serializers.SerializerMethodField()

    class Meta:
        model = Collection
        fields = ('__all__')
        read_only_fields = ('user', 'movies', 'like_users')

 
    def get_movies(self, obj):
        movies = obj.movies.all()
        if not movies:
            return []
        else:
            lst = []
            for movie in movies:
                dic = {}
                dic['id'] = movie.pk
                dic['title'] = movie.title
                dic['poster_path'] = movie.poster_path
                dic['youtube_key'] = movie.youtube_key
                dic['content'] = Movie_choice.objects.get(movie_id=movie.id, collection_id=obj.id).content
                lst.append(dic)
            return lst

class AllCollectionSerializer(serializers.ModelSerializer):
#유저 정보랑 like, comment 부분 수정해야함

    movies = serializers.SerializerMethodField()
    # collection_review_set = CollectionReviewSerializer(many = True, read_only = True)
    user = CustomUserDetailsSerializer()

    class Meta:
        model = Collection
        fields = ('__all__')

 
    def get_movies(self, obj):
        movies = obj.movies.all()
        if not movies:
            return []
        else:
            lst = []
            for movie in movies:
                dic = {}
                dic['id'] = movie.pk
                dic['poster_path'] = movie.poster_path
                dic['title'] = movie.title
                dic['youtube_key'] = movie.youtube_key
                dic['content'] = Movie_choice.objects.get(movie_id=movie.id, collection_id=obj.id).content
                lst.append(dic)
            return lst



#     class MovieSerializer(serializers.ModelSerializer):
#         content = serializers.SerializerMethodField()

#         class Meta:
#             model = Movie
#             fields = ('id', 'title', 'content')

#         def get_content(self, obj):
#             obj
#             return obj['content']
            


#     movies = MovieSerializer(serializers.ModelSerializer, many = True, read_only = True)
    # collection_review_set = CollectionReviewSerializer(many = True, read_only = True)