from rest_framework import routers
from .api import UserViewSet, UserViewSetOne
from django.urls import path
from .routers import CustomRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from . import views

"""router = CustomRouter()

router.register('', UserViewSet, 'users')
router.register('', UserViewSetOne, 'oneuser')

urlpatterns = router.urls
"""
router = routers.DefaultRouter()
router.register('', views.GetUsersView)

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="token_verify"),
]

urlpatterns += router.urls