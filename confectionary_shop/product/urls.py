from django.urls import path
from .views import Detail_product
from django.conf import settings
from django.conf.urls.static import static

app_name = 'product'
urlpatterns = [
                  path('detail/', Detail_product.as_view(), name='detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
