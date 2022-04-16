from pyexpat import model
from rest_framework import serializers
from shouts.models import Post, Like, Comments

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'tweet',
            'pic',
            'date_posted',
            'user',
            'tags'
        ]

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            'id',
            'post',
            'username',
            'comment',
            'comment_date'
        ]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = [
            'id',
            'user',
            'post'
        ]


       