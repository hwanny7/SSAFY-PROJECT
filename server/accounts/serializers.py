from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):

    nickname = serializers.CharField(max_length=100)
    followings = serializers.ModelSerializer(many=True, read_only=True)
    blockings = serializers.ModelSerializer(many=True, read_only=True)
    img_url = serializers.CharField(max_length=100)
    point = serializers.IntegerField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)


    def get_cleaned_data(self):
        cleaned_data = super().get_cleaned_data()
        cleaned_data['img_url'] = self.validated_data.get('img_url', '')
        cleaned_data['point'] = self.validated_data.get('point', '')
        cleaned_data['date_joined'] = self.validated_data.get('date_joined', '')


        return cleaned_data

# class FollowerSerializer(serializers.ModelSerializer):
#     followers = EachUserSerializer(many=True, read_only= True)
#     followings = EachUserSerializer(many=True,read_only=True)

#     class Meta:
#         model = UserProfile
#         fields = ('followers','followings')