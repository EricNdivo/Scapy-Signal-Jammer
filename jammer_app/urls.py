from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('start_jamming/', views.start_jamming, name='start_jamming'),
    path('stop_jamming/', views.stop_jamming, name='stop_jamming'),
]