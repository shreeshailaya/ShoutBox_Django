import re
from urllib import response
from urllib.request import Request
from wsgiref import validate
from django.forms import ValidationError
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from userProfile.serializers import LoginSerializer
from userProfile.serializers import RegisterSerializer, UserProfileSerializer, FriendRequestSerializer
from django.contrib import auth
from django.contrib.auth import logout
from rest_framework import generics, status, views, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from userProfile.models import Profile, FriendRequest
from django.contrib.auth.models import User


# Create your views here.


class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer
  

    def post(self, request):
        user = request.data
        print("This is user",user)
        user['username'] = user['email']
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        return Response(user_data, status=status.HTTP_201_CREATED)



class LoginAPIView(generics.GenericAPIView):
    serializer_class=LoginSerializer
    def post(self,request):
        serializers= self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        user_data = request.data
        userx = auth.authenticate(username=user_data['username'], password=user_data['password'])
        
        '''
        final_data = {
                #"data": serializers.data,
                "token": LoginSerializer.generateToken(self, userx),
                
            }
        '''
        return Response(LoginSerializer.generateToken(self, userx),status=status.HTTP_200_OK)


@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    #print(request.META['HTTP_AUTHORIZATION'])
    pre_token = request.META['HTTP_AUTHORIZATION']
    pre_token = pre_token[6:]
    print(pre_token)
    pk = Token.objects.get(key=pre_token)
    snnipt = Profile.objects.get(id=pk.user_id)
    serializers = UserProfileSerializer(snnipt)
    return Response(serializers.data)

@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def getUserProfileOnId(request,pk):
    snnipt = Profile.objects.get(id=pk)
    serializers = UserProfileSerializer(snnipt)
    return Response(serializers.data)


@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def friendsList(request):
    qs = User.objects.all()
    serializers = UserProfileSerializer(qs)
    return Response(serializers.data, status=status.HTTP_200_OK)


class SuggestFriends(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    permissions_classes = [permissions.IsAuthenticated]


    
@api_view(['POST','PUT'])
@permission_classes([IsAuthenticated])
def sendFriendRequest(request):
    pre_token = request.META['HTTP_AUTHORIZATION']
    token = pre_token[6:]
    from_user = Token.objects.get(key=token).user_id

    users_data = request.data
    user_id = users_data['to_user']
    #to_user_user = User.objects.get(id=user_id).user
    to_user = user_id
    #print( from_user1, to_user1)

    users_data['from_user'] = from_user
    users_data['to_user'] = to_user

    serializer_class = FriendRequestSerializer
    serializers= serializer_class(data = users_data)
    serializers.is_valid(raise_exception=True)

    #serializers.validate(users_data)
    serializers.save()
    
    print(serializers)
    return Response(serializers.data, status=status.HTTP_200_OK)
    '''
        {
        "to_user": 10,
        "from_user": ""
        }
    '''


class GetFriendsRequest(viewsets.ModelViewSet):
    serializer_class = FriendRequestSerializer
    permissions_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return FriendRequest.objects.filter(to_user=user)


@api_view(['DELETE','GET'])
@permission_classes([IsAuthenticated])
def deleteFriendRequest(self,pk, format=None):
        
        snippet = FriendRequest.objects.get(id=pk).delete()
        serializers = FriendRequestSerializer(snippet)
        #serializers.delete()
        data ={
            'success':'deleted Successfully'
            }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
   
@api_view(['POST','PUT'])
@permission_classes([IsAuthenticated])
def acceptFriendRequest(request):
    data = request.data
    from_user_id = data['from_user']
    to_user_id = data['to_user']
    friend_req_id = data['id']
    from_user = Profile.objects.get(id=from_user_id)
    to_user = Profile.objects.get(id=to_user_id)
    from_user.friends.add(to_user)
    to_user.friends.add(from_user)
    FriendRequest.objects.get(id=friend_req_id).delete()
    return Response(status = status.HTTP_200_OK)

'''
{
    "id": 44,
    "from_user": 14,
    "to_user": 15,
    "accepted_status": false
}
'''


    

   




'''
#@api_view(['GET'])
#@permission_classes([IsAuthenticated])
class UserLogOut(generics.GenericAPIView):
    def post(self, request):
        permission_classes = (IsAuthenticated)
        request.user.token.delete()
        
        logout(request)
        return Response('User Logged Out Successfully',status=status.HTTP_200_OK)

'''