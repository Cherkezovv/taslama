from django.urls import path, include
from . import views


app_name = 'chat'

urlpatterns = [
    path('soragjogap/', views.soragjogap, name='sorag_jogap'),
    path('adminehabar/', views.adminehabar, name='adminehabar'),
]
