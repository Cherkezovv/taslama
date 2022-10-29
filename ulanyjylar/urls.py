from django.urls import path, include
from . import views


app_name = 'ulanyjylar'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('logoutt/', views.logoutt, name='logoutt'),
    path('register/', views.register, name='register'),
    path('shahsy_otag/', views.shahsy_otag, name='shahsy_otag'),
]