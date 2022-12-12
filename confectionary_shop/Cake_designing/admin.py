from django.contrib import admin
from .models import Feeling,Taste,Cake_Designing
# Register your models here.


@admin.register(Feeling)
class FeelingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Feeling._meta.get_fields()]
    search_fields = ('feeling_name',)
    ordering = ('price',)


@admin.register(Taste)
class TasteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Taste._meta.get_fields()]
    search_fields = ('Taste_name',)
    ordering = ('price',)


@admin.register(Cake_Designing)
class TasteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cake_Designing._meta.get_fields()]
    search_fields = ('order_id',)
    ordering = ('order_id',)