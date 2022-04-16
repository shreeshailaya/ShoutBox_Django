from django.contrib import admin
from shouts.models import Post, Like, Comments

# Register your models here.
@admin.register(Post)
class Posts(admin.ModelAdmin):
    pass

@admin.register(Like)
class Likes(admin.ModelAdmin):
    pass

@admin.register(Comments)
class Comments(admin.ModelAdmin):
    pass


