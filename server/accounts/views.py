from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CustomRegisterSerializer
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import get_user_model
from accounts.serializers import CustomUserDetailsSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# Create your views here.

#자기 자신이 아닌 경우에만 버튼 출력하기, True, false 반환해서 json에만 반영하기
#데코레이터 POST 추가, header 부분도 추가, CustomSerializer 를 새로 만들어야 하나?

# @require_POST
@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['post'])
def follow(request):
    User = get_user_model()
    person = get_object_or_404(User, pk=request.data['user_pk'])
    if person == request.user:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if person.followers.filter(pk=request.user.pk).exists():
        person.followers.remove(request.user)
    else:
        person.followers.add(request.user)
    return Response(status=status.HTTP_200_OK)
    # return 부분 성공인지 실패인지 수정하기. state로 보내 줘야 할 것 같은데

# @require_POST
def block(request, user_pk):
    User = get_user_model()
    me = get_object_or_404(User, pk=request.user.pk)
    you = get_object_or_404(User, pk=user_pk)
    if me.blockings.filter(pk=user_pk).exists():
        me.blockings.remove(you)
    else:
        me.blockings.add(you)
    return HttpResponse({'성공'})

@permission_classes([IsAuthenticatedOrReadOnly])
@api_view(['get'])
def profile(request, user_pk):
    User = get_user_model()
    person = get_object_or_404(User, pk=user_pk)
    serializers = CustomUserDetailsSerializer(person)
    return Response(serializers.data)
    
    
