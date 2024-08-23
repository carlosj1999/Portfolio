from django.urls import path
from . import views

app_name = 'ip_aggregator'
urlpatterns = [
    path('', views.index, name = 'index'),
    
]
