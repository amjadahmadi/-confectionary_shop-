from django.urls import path, include
from rest_framework import routers

from .views import Detail_product, CategoryList, ProductList
from django.conf import settings
from django.conf.urls.static import static

app_name = 'product'
urlpatterns = [
                  path('detail/<pk>', Detail_product.as_view(), name='detail'),
                  path('category_list/', CategoryList.as_view(), name='category_list'),
                  path('product_list/<category_id>', ProductList.as_view(), name='product_list'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
