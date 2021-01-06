from django.contrib import admin
from .models import *


class PostImageAdmin(admin.StackedInline):
    model = PostImage


class CategoryBannerAdmin(admin.StackedInline):
    model = CategoryBanner


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

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [CategoryBannerAdmin]

    class Meta:
        model = Category


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'body', 'created_on']

    class Meta:
        model = Comment


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    pass


class BannerAdmin(admin.StackedInline):
    inlines = [BannerAdmin]

# admin.site.register(Category, CategoryAdmin)