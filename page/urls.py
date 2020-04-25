from . import views
from django.conf.urls import url
from page.views import page
#from django.contrib.auth import views
#from django.urls import path

urlpatterns = [
        url('', page.as_view()),
        #path('login/', views.LoginView.as_view(), name='login'),
]
