from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"url": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'post', 'text', 'created_date')
    list_filter = ('username', 'created_date')
    search_fields = ('text', 'username__username', 'post__title')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)