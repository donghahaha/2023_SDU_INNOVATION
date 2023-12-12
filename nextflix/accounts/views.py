from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
import urllib


@api_view(['POST'])
def signup(request):
	#1-1. Receive data from the Client
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	#1-2. Check for password matching
    if password != password_confirmation:
        return Response({'error': 'The password does not match.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#2. Serialize data with UserSerializer
    serializer = UserSerializer(data=request.data)
    
	#3. Validation operation proceeds -> Password also serializes
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. After hashing the password
        user.set_password(request.data.get('password'))
        user.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def my_profile(request):
    user = get_object_or_404(get_user_model(), pk=request.data.get('user_id'))
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def users_info(request):
    users = request.data.get('users')
    movies = []
    ages = []
    for user in users:
        user = get_object_or_404(get_user_model(), pk=user)
        serializer = UserSerializer(user)
        age = serializer.data.get('age')
        like_movies = serializer.data.get('like_movies')
        dislike_movies = serializer.data.get('dislike_movies')
        wish_movies = serializer.data.get('wish_movies')
        watched_movies = serializer.data.get('watched_movies')
        for movie in like_movies:
            if movie not in movies:
                movies.append(movie)
            if age==user.age and movie not in ages:
                ages.append(movie)
    return Response([movies, ages])