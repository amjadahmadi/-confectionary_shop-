from django.urls import path
from .views import UserCreateView,CodeGenerate
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user'
urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('code/', CodeGenerate.as_view(), name='code'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)