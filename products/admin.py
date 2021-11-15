from django.contrib import admin
from .models import Product, Category, ReviewRating

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'is_onsale',
        'onsale_price',
        'stock',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'image_url',
        'image',
    )

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ReviewRating)