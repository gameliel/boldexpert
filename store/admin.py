from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Category)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'digital', 'hot', 'featured', 'image')
    inlines = [ProductImageAdmin]

    class Meta:
        models = Product

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass
