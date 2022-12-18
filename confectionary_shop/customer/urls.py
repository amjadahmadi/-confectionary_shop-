from django.urls import path
from .views import UserCreateView, CodeGenerate, Logout, Login, Profile, CreateComment
from django.conf import settings
from django.conf.urls.static import static

app_name = 'user'
urlpatterns = [
                  path('signup/', UserCreateView.as_view(), name='signup'),
                  path('code/', CodeGenerate.as_view(), name='code'),
                  path('logout/', Logout.as_view(), name='logout'),
                  path('login/', Login.as_view(), name='login'),
                  path('profile/<pk>', Profile.as_view(), name='profile'),
                  path('comment/', CreateComment.as_view(), name='comment'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
