from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from django.conf import settings
from autoslug import AutoSlugField



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    slug = AutoSlugField(populate_from='user')
    bio = models.CharField(max_length=255, blank=True) 
    mobile = models.IntegerField(null=True)
    gender = models.CharField(max_length=25, blank=True)
    dob = models.DateField(null=True)
    city = models.CharField(max_length=100, blank=True)
    work_at = models.CharField(max_length=100, blank=True)
    friends = models.ManyToManyField("Profile", blank=True)

    
    def __str__(self):
        return str(self.user.username)
    
   
        

def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass

post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)

    

class FriendRequest(models.Model):
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    accepted_status = models.BooleanField(default=False)

    def __str__(self):
        return "From {}, to {}".format(self.from_user.username, self.to_user.username)



'''
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models



class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        return ''
            
'''
