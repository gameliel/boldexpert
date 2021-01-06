from django.contrib import admin
from .models import *

class BannerAdmin(admin.StackedInline):
    model = Banner


class PortfolioImageAdmin(admin.StackedInline):
    model = PortfolioImage


class CategoryBannerAdmin(admin.StackedInline):
    model = CategoryBanner


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('topic', 'category', 'status', 'image', 'created_on')
    search_fields = ['title', 'description']
    inlines = [PortfolioImageAdmin, BannerAdmin]


    class Meta:
        model = Portfolio

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [CategoryBannerAdmin]

    class Meta:
        model = Category

@admin.register(PortfolioImage)
class PortfolioImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
     pass

# @admin.register(CategoryBanner)
# class CategoryBannerAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Category)