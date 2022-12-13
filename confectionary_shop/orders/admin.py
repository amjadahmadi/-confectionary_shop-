
from django.contrib import admin
from .models import Orders,Order_Item
# Register your models here.


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Orders._meta.get_fields()]
    search_fields = ('user_id',)
    ordering = ('final_price',)


@admin.register(Order_Item)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order_Item._meta.get_fields()]
    search_fields = ('order_id',)
    ordering = ('price',)


