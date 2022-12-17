from django.contrib import admin
from .models import Feeling, Taste, Cake_Designing


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
class CakeDesigningAdmin(admin.ModelAdmin):
    autocomplete_fields = ('feeling_id', 'taste_id')
    list_display = [field.name for field in Cake_Designing._meta.get_fields()]
    search_fields = ('order_id',)
    ordering = ('order_id',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj=None, **kwargs)
        if not request.user.is_superuser:
            for i in form.base_fields.keys():
                if i != 'extra_payment':
                   form.base_fields[i].disabled = True
        return form
