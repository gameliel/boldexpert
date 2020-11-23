from django.contrib import admin
from .models import *


class PostImageAdmin(admin.StackedInline):
    model = PostImage


class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model=Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'Category', 'slug', 'status', 'image', 'created_on')
    list_filter = ("status", "Category",)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)


class PostImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(PostImage, PostImageAdmin)

admin.site.register(Category)