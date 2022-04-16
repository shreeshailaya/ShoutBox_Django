from django.urls import path
from rest_framework import routers
from shouts.views import GetPosts
import shouts.views as view


urlpatterns = [
    path('getposts/', GetPosts.as_view({'get': 'list'}), name='getposts'),
    path('postposts/', view.postPosts, name='postposts'),
    path('postcomment/', view.postComment, name='postcomment'),
    path('getcomment/<int:pk>/',view.getPostComments, name='getcomment' ),
    path('likepost/', view.likePost, name='lokepost'),
    path('getlikes/<int:pk>/', view.getPostLikes, name='grtlikes')
   
]