from rest_framework import serializers
from .models import Movie, Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie',)

class ReviewListSerializer(serializers.ModelSerializer):
  movie_title = serializers.SerializerMethodField()

  def get_movie_title(self, obj):
    return obj.movie.title

  userName = serializers.SerializerMethodField()
  
  def get_userName(self,obj):
    return obj.user.username

  class Meta:
    model = Review
    fields = ('id', 'user', 'userName', 'content', 'movie', 'rank', 'movie_title')
    read_only_fields = ('user',)

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_users','dislike_users', 'wish_users', 'watched_users')

