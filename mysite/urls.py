from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import *
from django.views.generic import TemplateView
#from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^auth/', include('djoser.urls')),
    #url(r'^auth/', include('djoser.urls.jwt')),
    #path('api/', include('accounts.urls')),

   #path('login/', views.LoginView.as_view(), name='login')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# All endpoints djoser
    # /users/
    # /users/me/
    # /users/confirm/
    # /users/resend_activation/
    # /users/set_password/
    # /users/reset_password/
    # /users/reset_password_confirm/
    # /users/set_username/
    # /users/reset_username/
    # /users/reset_username_confirm/
    # /token/login/ (Token Based Authentication)
    # /token/logout/ (Token Based Authentication)
    # /jwt/create/ (JSON Web Token Authentication)
    # /jwt/refresh/ (JSON Web Token Authentication)
    # /jwt/verify/ (JSON Web Token Authentication)
