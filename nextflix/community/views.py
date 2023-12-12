from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Community, Comment
from .serializers import CommunitySerializer, CommentSerializer

# Create your views here.
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def community_list_create(request):
    if request.method == 'GET':
        community_lists = Community.objects.all()
        serializer = CommunitySerializer(community_lists, many=True)
        return Response(serializer.data)
    else:
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def community_detail(request, community_pk):
        community = get_object_or_404(Community, pk=community_pk)
        if request.method == 'GET':
            serializer = CommunitySerializer(community)
            return Response(serializer.data)
        elif request.method == 'DELETE':
            community.delete()
            return Response({'pk': community_pk})
        else :
            # PUT
            serializer = CommunitySerializer(community, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                print(serializer.data)
                return Response(serializer.data)

@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comments(request, community_pk):
    if request.method == 'POST':
        community = get_object_or_404(Community, pk=community_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, community=community)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        community = get_object_or_404(Community, pk=community_pk)
        comments = community.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['DELETE'])
def comment_detail(request, community_pk, comment_pk):
    community = get_object_or_404(Community, pk=community_pk)
    comment = community.comment_set.get(pk=comment_pk)
    if request.method == 'DELETE':
        comment.delete()
        return Response({'pk': comment_pk})