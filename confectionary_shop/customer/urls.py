from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'addressapi', AddressAPI, basename="addressapi")
router.register(r'profileapi', ProfileAPI, basename="profileapi")

app_name = 'user'
urlpatterns = [
                  path('signup/', UserCreateView.as_view(), name='signup'),
                  path('code/', CodeGenerate.as_view(), name='code'),
                  path('logout/', Logout.as_view(), name='logout'),
                  path('login/', Login.as_view(), name='login'),
                  path('profile/<pk>', Profile.as_view(), name='profile'),
                  path('comment/', CreateComment.as_view(), name='comment'),
                  path('address/<user_id>', AddressListAPI.as_view(), name='address'),
                  path('', include(router.urls)),
                  path('createuser/', UserCreate.as_view(),name='createuser'),
                  path('updateuser/<pk>', UserUpdate.as_view(),name='updateuser'),
                  path('bankapi/', BankAPI.as_view(),name='bankapi'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
