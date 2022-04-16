from rest_framework.authtoken.models import Token
from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, status
from shouts.serializers import PostSerializer, CommentsSerializer, LikeSerializer
from shouts.models import Post, Comments, Like
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.



@api_view(['post'])
@permission_classes([IsAuthenticated])
def postPosts(request):
    pre_token = request.META['HTTP_AUTHORIZATION']
    token = pre_token[6:]
    from_user = Token.objects.get(key=token).user_id
    print(from_user)
    request.data._mutable = True
    user_post = request.data
    user_post['user'] = from_user
    serializer_class = PostSerializer
    serializers= serializer_class(data = user_post)
    serializers.is_valid(raise_exception=True)

    #serializers.validate(users_data)
    serializers.save()
    return Response(serializers.data, status=status.HTTP_200_OK)
    '''
    {
    "tweet": "post by postman",
    "pic": "/media/shouts/Capture_07WpD84.PNG",
    "tags": "#nothing"
    }
    '''
    
class GetPosts(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['post'])
@permission_classes([IsAuthenticated])
def postComment(request):
    pre_token = request.META['HTTP_AUTHORIZATION']
    token = pre_token[6:]
    from_user = Token.objects.get(key=token).user_id

    request.data._mutable = True
    user_post = request.data
    user_post['username'] = from_user
    
    serializer_class = CommentsSerializer
    serializers= serializer_class(data = user_post)
    serializers.is_valid(raise_exception=True)

    #serializers.validate(users_data)
    serializers.save()
    return Response(serializers.data, status=status.HTTP_200_OK)

    '''
    post
    comment
    '''


@api_view(['get'])
@permission_classes([IsAuthenticated])
def getPostComments(request, pk):
    queryset = Comments.objects.filter(post =  pk)
    serializers = CommentsSerializer(queryset, many=True)
    #serializers.is_valid(raise_exception=True)
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['post'])
@permission_classes([IsAuthenticated])
def likePost(request):
    pre_token = request.META['HTTP_AUTHORIZATION']
    token = pre_token[6:]
    from_user = Token.objects.get(key=token).user_id

    request.data._mutable = True
    user_like = request.data
    user_like['user'] = from_user

    serializer_class = LikeSerializer
    serializers= serializer_class(data = user_like)
    serializers.is_valid(raise_exception=True)

    #serializers.validate(users_data)
    serializers.save()
    return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['get'])
@permission_classes([IsAuthenticated])
def getPostLikes(request, pk):
    queryset = Like.objects.filter(post =  pk)
    serializers = LikeSerializer(queryset, many=True)
    #serializers.is_valid(raise_exception=True)
    return Response(serializers.data, status=status.HTTP_200_OK)

       
      
    
    
  




