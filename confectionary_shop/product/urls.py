from django.urls import path, include
from rest_framework import routers

from .views import Detail_product, CategoryList
from django.conf import settings
from django.conf.urls.static import static

app_name = 'product'
urlpatterns = [
                  path('detail/', Detail_product.as_view(), name='detail'),
                  path('category_list/', CategoryList.as_view(), name='category_list'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
