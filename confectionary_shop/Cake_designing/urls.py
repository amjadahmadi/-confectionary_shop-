from django.urls import path
from .views import CakeDesigning, FeelingAndTasteAPI
from django.conf import settings
from django.conf.urls.static import static
import django.utils.translation as e

app_name = 'cake_designing'
urlpatterns = [
                  path('cake_designing/', CakeDesigning.as_view(), name='cake_designing'),
                  path('get_feeling_taste/<feeling_id>/<taste_id>', FeelingAndTasteAPI.as_view(), name='feeling_and_taste_api'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
