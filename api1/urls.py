from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
     ProductViewSet,
     pais
)

router = DefaultRouter(trailing_slash=False)
router.register('products', ProductViewSet)

urlpatterns = [
    path('pais/', pais),
]

urlpatterns += router.urls