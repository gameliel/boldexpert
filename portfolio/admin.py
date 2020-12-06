from django.contrib import admin
from .models import *


class PortfolioImageAdmin(admin.StackedInline):
    model = PortfolioImage




@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'image', 'created_on')
    search_fields = ['title', 'description']
    inlines = [PortfolioImageAdmin]


    class Meta:
        model = Portfolio



@admin.register(PortfolioImage)
class PortfolioImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)