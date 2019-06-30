from django.contrib import admin

from .models import UserProfile, Post, Comment



class UserProfileAdmin(admin.ModelAdmin):
    list_display=['user', 'bio', 'residence']

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Post)
admin.site.register(Comment)

