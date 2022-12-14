from django.urls import path
from .views import (
     ProductDestroyView, 
     ProductUpdateView,
     ProducDetailView,
     ProducCreateView,
     pais
)


urlpatterns = [
    path('pais/', pais),
    path('products/<int:pk>/delete', ProductDestroyView.as_view()),
    path('products/<int:pk>/update', ProductUpdateView.as_view()),
    path('products/<int:pk>', ProducDetailView.as_view()),
    path('products/create', ProducCreateView.as_view())   
]