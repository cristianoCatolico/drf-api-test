from django.urls import path
from .views import pais


urlpatterns = [
    path('pais/', pais)
]