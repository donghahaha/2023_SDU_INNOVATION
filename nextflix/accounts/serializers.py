from rest_framework import serializers
# from allauth.account.adapter import get_adapter
from django.contrib.auth import get_user_model
# from rest_auth.registration.serializers import RegisterSerializer

User = get_user_model()
# Except for models.py , get_user_model() when using User Model
# DB -> JSON 
class UserSerializer(serializers.ModelSerializer): # ModelSerializer
    # Set the password to JSON so that it doesn't go out
    password = serializers.CharField(write_only=True) # write_only
    class Meta:
        model = User # Set which DB and Serializer to connect to
        fields = ('id','username', 'password', 'age', 'like_movies', 'dislike_movies', 'wish_movies', 'watched_movies') 
        read_only_fields = ('reviews', 'like_movies', 'dislike_movies', 'wish_movies', 'watched_movies')