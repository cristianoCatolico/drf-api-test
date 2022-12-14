from django.urls import path
from .views import (
     ProductManageView,
     ProducCreateView,
     pais
)


urlpatterns = [
    path('pais/', pais),
    path('products/<int:pk>', ProductManageView.as_view()),    
    path('products/create', ProducCreateView.as_view())   
]