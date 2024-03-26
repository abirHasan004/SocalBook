from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(profile)
class profile(admin.ModelAdmin):
    
    list_display=['user','profileimg' ]
    
@admin.register(POST)
class POST(admin.ModelAdmin):
    list_display=['img','Captions','user','like_count']
admin.site.register(Like_Post)

@admin.register(FollowerCount)
class Follower(admin.ModelAdmin):
    list_display=['user']
 