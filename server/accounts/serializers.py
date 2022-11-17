from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer


class CustomRegisterSerializer(RegisterSerializer):

    nickname = serializers.CharField(max_length=100)
    followings = serializers.ModelSerializer(many=True, read_only=True)
    blockings = serializers.ModelSerializer(many=True, read_only=True)
    # image = serializers.ImageField(read_only=True)
    image = serializers.ImageField(use_url=True)
    # image = serializers.SerializerMethodField()
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

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('nickname', 'image', 'point', 'date_joined')


# REST_AUTH_SERIALIZERS = {
#     "USER_DETAILS_SERIALIZER": "apps.custom_users.serializers.CustomUserSerializer"
# } => settings에 serializers를 custom 한다는 것을 명시

# serialiazer에 상단과 같이 커스텀 class를 만들어준다.