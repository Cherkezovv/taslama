from django.urls import path, include
from . import views


app_name = 'gyzykly'

urlpatterns = [
    path('videolar/', views.gyzykly_videolar, name='gyzykly_videolar'),
    path('kitaplar/', views.gyzykly_kitaplar, name='gyzykly_kitaplar'),
    path('habarlar/', views.habarlar, name='habarlar'),
    path('habarlar/<int:p_k>/', views.habar, name='habar'),
    
]
