from multiprocessing import dummy
from unicodedata import name
from django.urls import path
from userProfile.views import RegisterView
from userProfile.views import LoginAPIView, SuggestFriends, GetFriendsRequest
from rest_framework import routers
import userProfile.views as view



urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('userprofile/', view.getUserProfile , name='userprofile' ),
    path('userprofile/<int:pk>/', view.getUserProfileOnId, name='userprofileonid'),
    path('allusers/', SuggestFriends.as_view({'get': 'list'}), name='friends' ),
    path('sendfreq/', view.sendFriendRequest, name = 'friendrequestsend'),
    path('getfreqs/',GetFriendsRequest.as_view({'get': 'list'}), name='getfriendrequest'),
    path('deletefreq/<int:pk>/', view.deleteFriendRequest,name='deletefriendrequest'),
    path('acceptfreq/', view.acceptFriendRequest, name='acceptfriendrequest'),
    
]

'''
{
    "id": 45,
    "from_user": 1,
    "to_user": 14,
    "accepted_status": false
}
'''