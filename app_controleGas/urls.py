from unicodedata import name
from django import views
from django.urls import path
from .views import IndexView, LeituraView 

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('leitura', LeituraView.as_view(), name='leitura'),
]