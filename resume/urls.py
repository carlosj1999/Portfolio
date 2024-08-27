from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('home', views.HomeView.as_view, name='home'),
    #path('', views.home, name='home'),
    path('', views.resume, name='resume'),
]
