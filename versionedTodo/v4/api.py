from api1.models import Todo
from .serializer import TodoSerializer
from rest_framework import status
from rest_framework.response import Response
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 
from rest_framework.throttling import BaseThrottle
from rest_framework.decorators import action
import random

class RandomRateThrottle(BaseThrottle):
    def allow_request(self, request, view):
        return random.randint(1, 10) != 1
        
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'body']
    ordering = ('-id')
    throttle_scope = 'get'
    throttle_classes = [RandomRateThrottle]

    '''@action(detail=False, methods=["post","get"], throttle_classes=[UserRateThrottle])
    def example_adhoc_method(request, pk=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
        '''

