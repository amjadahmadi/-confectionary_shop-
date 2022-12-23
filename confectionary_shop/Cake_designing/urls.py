from django.urls import path
from .views import CakeDesigning
from django.conf import settings
from django.conf.urls.static import static
import django.utils.translation as e

app_name = 'cake_designing'
urlpatterns = [
                  path('cake_designing/', CakeDesigning.as_view(), name='cake_designing'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
