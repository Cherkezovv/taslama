from django.urls import path, include
from . import views


app_name = 'books_videos'

urlpatterns = [
    path('', views.index, name='index'),
    path('kitaplar_videolar/<int:pk>/', views.kitaplar_videolar, name='kitaplar_videolar'),
]
