from django.contrib import admin
from .models import *


class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'image', 'created_on')
    search_fields = ['title', 'description']
    inlines = [PostImageAdmin]

    class Meta:
        model = Post

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'body', 'created_on']

    class Meta:
        model = Comment

admin.site.register(Category, CategoryAdmin)