from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.seralizer import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.


@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'user': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def register(request):
    return None


def login(request):
    return None


def logout(request):
    return None


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
def getAllUsers(request):
    print("get the request--->", request.user)
    users = User.objects.all()
    seralizer = UserSerializer(users, many=True)

    return Response(seralizer.data, status=status.HTTP_200_OK)
