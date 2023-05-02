from rest_framework.serializers import ModelSerializer

from accounts.models import customerProfile
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email',)

    def create(self, validated_data):
        # hash the password
        validated_data['password'] = make_password(validated_data['password'])

        user = User.objects.create_user(**validated_data)
        #customerprofile = customerProfile.objects.create(user=user)
        return user


# class UserLoginSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'password',)
#
#     def create(self, validated_data):
#         # hash the password
#         validated_data['password'] = make_password(validated_data['password'])
#
#         user = User.objects.create_user(**validated_data)
#         customerprofile = customerProfile.objects.create(user=user)
#         return customerprofile


