from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import Detail_product, CategoryList, ProductListAPI, DiscountCode
from django.conf import settings
from django.conf.urls.static import static
router = DefaultRouter()
router.register(r'discount_code', DiscountCode,basename="discount_code")
app_name = 'product'
urlpatterns = [
                  path('detail/<pk>', Detail_product.as_view(), name='detail'),
                  path('category_list/', CategoryList.as_view(), name='category_list'),
                  path('product_list/<category_id>', ProductListAPI.as_view(), name='product_list'),
                  path('', include(router.urls)),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
