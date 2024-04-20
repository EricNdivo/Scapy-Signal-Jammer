from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('start/', views.start_jamming, name='start_jamming'),
    path('stop/', views.stop_jamming, name='stop_jamming'),
]
