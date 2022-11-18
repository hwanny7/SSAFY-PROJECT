from rest_framework import serializers
from .models import Collection, Collection_Review, Movie_choice
from movies.models import Movie

# from accounts.serializers import CustomUserDetailsSerializer
# user = CustomUserDetailsSerializer() >> 다른 사람들 목록도 다 보여줄 때는 user 닉네임이나 이런 것도 같이 보여줄 때 쓰기 (field값 조정해야함)


# class MovieChoiceSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Movie_choice
#         fields = ('content',)


class CollectionReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection_Review
        fields = ('user', 'content', 'choice', 'like_users')
        read_only_fields = ('user', 'choice', 'collection', 'like_users')



class CollectionSerializer(serializers.ModelSerializer):

    # class MovieSerializer(serializers.ModelSerializer):
    #     movie_choice_set = MovieChoiceSerializer(many = True, read_only = True)

    #     class Meta:
    #         model = Movie
    #         fields = ('id', 'title', 'youtube_key', 'movie_choice_set')

    # movies = MovieSerializer(serializers.ModelSerializer, many = True)
    collection_review_set = CollectionReviewSerializer(many = True, read_only = True)
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
                dic['youtube_key'] = movie.youtube_key
                dic['content'] = Movie_choice.objects.get(movie_id=movie.id, collection_id=obj.id).content
                lst.append(dic)
            return lst
    
    






    # movies = serializers.SerializerMethodField()
    # def get_movies(self, obj):
    #     movies = obj.movies.all()
    #     if not movies:
    #         return []
    #     else:
    #         dic = {}
    #         for movie in movies:
    #             dic[movie.pk] = Movie_choice.objects.get(movie_id=movie.id, collection_id=obj.id).content
    #         return dic





# return 으로 반환하는 값 커스텀하기