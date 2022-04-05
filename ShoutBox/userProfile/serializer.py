from dataclasses import fields
from genericpath import exists

from django.forms import ValidationError
from .models import Profile, FriendRequest
from rest_framework.authtoken.models import Token
from unicodedata import name
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from django.utils.text import slugify




class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6,write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if username.isalnum():
            raise serializers.ValidationError(
                'The username and Email is not same entered')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=255, min_length=3,)

    class Meta:
        model = User
        fields = ['id','username','password']

    def generateToken(self, obj):
        is_tokened = Token.objects.filter(user=obj)
        if(is_tokened):
            token = Token.objects.get(user=obj)
            return {
                "token":token.key
            }
        else:
            token = Token.objects.create(user=obj)
            return {
                "token":token.key
            }
    def validate(self, attrs):
        username = attrs.get('username','')
        password = attrs.get('password', '')

        user = auth.authenticate(username=username, password=password)
        if not user:
            raise AuthenticationFailed('User name or password is invalid')
        
        return{
            'username': user.username,
            'password':user.password,
        }

        #return super().validate(attrs)

class userSeria(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class UserProfileSerializer(serializers.ModelSerializer):
    user = userSeria()
    class Meta:
        model = Profile
        fields = [
            'user',
            'id',
            'image',
            'bio',
            'mobile',
            'gender',
            'dob',
            'city',
            'work_at',
            'friends'
            
        ]

class FriendRequestSerializer(serializers.ModelSerializer):
    
    
    def create(self, validated_data):
        instance, _ = FriendRequest.objects.get_or_create(**validated_data)
        return instance
    class Meta:
        model = FriendRequest
        fields = [
            'id',
            'from_user',
            'to_user',
            'accepted_status'
        ]

       
   



'''json-formate-registration
{

 "password":"user123",
 "email":"user@test1.com",
 "first_name":"user",
 "last_name":"sirnm"
}
'''

'''login json formate
{
 "username":"user@test1.com",
 "password":"user123"
 
}
'''