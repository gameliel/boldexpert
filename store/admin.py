from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Category)

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'digital', 'hot', 'featured', 'image')

admin.site.register(Product, ProductAdmin)