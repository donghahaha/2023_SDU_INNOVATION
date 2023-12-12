from rest_framework import serializers
from .models import Community, Comment

class CommunitySerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()

    def get_userName(self, objects):
        return objects.user.username

    class Meta:
        model = Community
        fields = '__all__' 
        read_only_fields = ('user','like')
       
class CommentSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()

    def get_userName(self, objects):
        return objects.user.username

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'community',)
