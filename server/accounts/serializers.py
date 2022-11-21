from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer


from .models import User


class CustomRegisterSerializer(RegisterSerializer):

    nickname = serializers.CharField(max_length=100)
    followings = serializers.ModelSerializer(many=True, read_only=True)
    blockings = serializers.ModelSerializer(many=True, read_only=True)
    image = serializers.ImageField(use_url=True)
    point = serializers.IntegerField(read_only=True) 
    date_joined = serializers.DateTimeField(read_only=True)


    def get_cleaned_data(self):
        cleaned_data = super().get_cleaned_data()
        cleaned_data['nickname'] = self.validated_data.get('nickname', '')
        cleaned_data['image'] = self.validated_data.get('image', '')
        cleaned_data['point'] = self.validated_data.get('point', '')
        cleaned_data['date_joined'] = self.validated_data.get('date_joined', '')

        return cleaned_data


class CustomUserDetailsSerializer(UserDetailsSerializer): # dj_rest_auth.urls/user => user 정보 불러오는 걸 custom
    
    class followerSerializer(serializers.ModelSerializer):

        class Meta:
            model = User
            fields = ('nickname', 'image', 'id')
    
    followers_count = serializers.IntegerField(source='followers.count')
    followers_info = followerSerializer(source="followers", many=True)

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('nickname', 'image', 'point', 'date_joined', 'followings', 'followers', 'followers_info', 'followers_count')


# REST_AUTH_SERIALIZERS = {
#     "USER_DETAILS_SERIALIZER": "apps.custom_users.serializers.CustomUserSerializer"
# } => settings에 serializers를 custom 한다는 것을 명시

# serialiazer에 상단과 같이 커스텀 class를 만들어준다.

#https://velog.io/@ready2start/DRF-djrestauth%EB%A1%9C-%EC%BB%A4%EC%8A%A4%ED%85%80-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0
