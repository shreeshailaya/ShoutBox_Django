from django.contrib import admin
from userProfile.models import Profile,FriendRequest

# Register your models here.
@admin.register(Profile)
class UserProfile(admin.ModelAdmin):
    pass

@admin.register(FriendRequest)
class FriendRequest(admin.ModelAdmin):
    pass
