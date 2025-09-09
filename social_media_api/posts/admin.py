from django.contrib import admin
from .models import Post, Comment, Like

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "content", "created_at")
    search_fields = ("content", "user__username")
    list_filter = ("created_at",)
    ordering = ("-created_at",)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "user", "content", "created_at")
    search_fields = ("content", "user__username", "post__content")
    list_filter = ("created_at",)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "post", "created_at")
    search_fields = ("user__username", "post__content")
    list_filter = ("created_at",)
