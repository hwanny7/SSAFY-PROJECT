from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import CollectionSerializer, CollectionReviewSerializer, AllCollectionSerializer
from .models import Collection, Collection_Review, Movie_choice
from movies.models import Movie
from collects import serializers
from django.contrib.auth import get_user_model
# Create your views here.

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
#인증 관련 함수



# @permission_classes([IsAuthenticatedOrReadOnly])
# @api_view(['GET', 'POST']) # 이게 있어야 홈페이지랑 postman에서 처리가 가능
# def collection(request): # collection 생성하면서 추가
#     user = request.user
#     if request.method == 'GET':
#         collections = user.collection_set.all().order_by('-pk')
#         serializers = AllCollectionSerializer(collections, many=True) # collectionlistserializer comments도 같이 출력하도록 변경
#         return Response(serializers.data)

#     elif request.method == 'POST':
#         serializers = CollectionSerializer(data=request.data)
#         if serializers.is_valid(raise_exception=True):
#             collection = serializers.save(user=user) # 외래키는 빈칸으로 두고 넘어갈 수 없음
#             for obj in request.data.get('movies', ''): # 딕셔너리 형태로 보내기
#                 movie = get_object_or_404(Movie, pk= obj['id'])
#                 collection.movies.add(movie, through_defaults={'content':f'{obj["content"]}', 'user':user}) # collection에 담은 movie choice
#             # for movie in collection.movies.all():
#             # 여기서 movie.content를 넣어도 될 것 같음

#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def allcollection(request):
#     collections = get_list_or_404(Collection.objects.order_by('-pk'))
#     serializers = AllCollectionSerializer(collections, many=True)
#     return Response(serializers.data)


@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['GET', 'POST']) # 이게 있어야 홈페이지랑 postman에서 처리가 가능
def collection(request): # collection 생성하면서 추가
    if request.method == 'GET':
        collections = Collection.objects.all().order_by('-pk')
        serializers = AllCollectionSerializer(collections, many=True)
        return Response(serializers.data)

    elif request.method == 'POST':
        user = request.user
        serializers = CollectionSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            collection = serializers.save(user=user) # 외래키는 빈칸으로 두고 넘어갈 수 없음
            for obj in request.data.get('movies', ''): # 딕셔너리 형태로 보내기
                movie = get_object_or_404(Movie, pk= obj['id'])
                collection.movies.add(movie, through_defaults={'content':f'{obj["content"]}', 'user':user}) # collection에 담은 movie choice
            # for movie in collection.movies.all():
            # 여기서 movie.content를 넣어도 될 것 같음

            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# @permission_classes([IsAuthenticatedOrReadOnly])
def mycollection(request, user_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk = user_pk)
    collections = user.collection_set.all().order_by('-pk')
    serializers = CollectionSerializer(collections, many=True) # collectionlistserializer comments도 같이 출력하도록 변경
    return Response(serializers.data)


# 토큰 확인과 해당 유저가 맞는지 심사, 위에 함수랑 합쳐도 상관 없을 듯
# if request.user == collection.user:
@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['PUT', 'DELETE'])
def update(request, collection_pk): # 주소 통해서 collection 숫자 가져와도 될 듯함
    collection = get_object_or_404(Collection, pk = collection_pk)
    if request.user == collection.user:
        if request.method == 'PUT':
            serializers = CollectionSerializer(collection, data=request.data)
            if serializers.is_valid(raise_exception=True):
                collection = serializers.save()
                for movie_pk, content in request.data.get('movies', '').items():
                    movie = get_object_or_404(Movie, pk = movie_pk) # filter로 movie 있는건지 체크하고 add 하기
                    collection.movies.add(movie, through_defaults={'content': f'{content}'})
                return Response(serializers.data, status=status.HTTP_201_CREATED)
                #serializers를 리턴해도 상관없음. 같은 값을 참조하고 있기 때문에

        elif request.method == 'DELETE': # 하나씩 버튼으로 삭제
            collection.delete()
            return Response({'delete':'삭제 되었습니다.'})
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED) # 해당 게시글의 유저가 아님

    # collection 안에 movie를 하나씩 삭제하는 것도 구현해야함

# def updata_each(request):
#     movie_choice = Movie_choice.objects.get(movie_id = request.data['movie_id'], collection_id = request.data['collection_id'])
    


@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['POST']) # 내 게시글에 스스로 좋아요 누를 수 있음
def like(request, collection_pk):
    user = request.user
    collection = Collection.objects.get(pk = collection_pk)
    if collection.like_users.filter(pk = user.pk).exists():
        collection.like_users.remove(request.user)
    else:
        collection.like_users.add(request.user)
    serializers = CollectionSerializer(collection)
    return Response(serializers.data, status=status.HTTP_201_CREATED)



#==========================================================================리뷰
@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def Review(request, collection_pk):
    collection = Collection.objects.get(pk = collection_pk) # 유저가 댓글 달고 있는 컬렉션
    review = collection.collection_review_set.all()
    serializers = CollectionReviewSerializer(review, many=True)
    return Response(serializers.data)


@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['POST'])
def Review_create(request):
    user = request.user
    collection = Collection.objects.get(pk = request.data['collection_pk'])
    serializers = CollectionReviewSerializer(data = request.data)
    print(request.data)
    if serializers.is_valid():
        print('hi')
        review = serializers.save(user=user, collection=collection)
         # choice = user.movie_choice_set.get(pk = 1) #collection, movie 로 찾을지 / user.movie_choice로 찾을지??
         # review.choice.add(choice)
         # serializers = CollectionReviewSerializer(review)
        return Response(serializers.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['DELETE'])
def Review_delete(request, review_pk):
    review = Collection_Review.objects.get(pk = review_pk)
    if request.user == review.user:
        review.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)



# def Review_like(request, review_pk):
#     user = request.user
#     review = Collection_Review.objects.get(pk = review_pk)
#     if review.like_users.filter(pk = user.pk).exists():
#         review.like_users.remove(request.user)
#     else:
#         review.like_users.add(request.user)
#     serializers = CollectionReviewSerializer(collection)
#     return Response(serializers.data, status=status.HTTP_201_CREATED)

# 수정, 삭제 기능 구현

