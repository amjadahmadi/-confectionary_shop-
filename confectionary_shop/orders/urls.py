from django.urls import path, include
from rest_framework import routers

from .views import Orders, OrdersAPI
from django.conf import settings
from django.conf.urls.static import static

app_name = 'orders'
urlpatterns = [
                  path('orders/', Orders.as_view(), name='orders'),
                  path('ordersapi/', OrdersAPI.as_view(), name='ordersapi'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
