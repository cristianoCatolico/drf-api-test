from .models import User
from rest_framework import viewsets, mixins
from .serializers import UserSerializer

class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()    

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class UserViewSetOne(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
