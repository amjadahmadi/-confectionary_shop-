from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Discount_Code)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Discount_Code._meta.get_fields()]
    search_fields = ('discount_name',)
    ordering = ('start_date',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Products._meta.get_fields()]
    search_fields = [field.name for field in Products._meta.get_fields()]
    ordering = ('product_name_fa','product_name_en')


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    autocomplete_fields = ('product',)
    filter_horizontal = ('category',)
    list_display = ['product', 'kilo', 'count', 'price']
    search_fields = ('product__product_name_fa','product__product_name_en')
    ordering = ('price',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.get_fields() if field != 'category']
    # search_fields = ('category_name',)
    # ordering = ('category_name',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Discount._meta.get_fields()]
    search_fields = ('product', 'category_id', 'cake_designing_id')
    ordering = ('amount', 'active')
