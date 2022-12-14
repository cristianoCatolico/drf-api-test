from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pais, Product
from .serializers import PaisSerializador, ProductSerializer
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView, UpdateAPIView, RetrieveAPIView, CreateAPIView

from rest_framework import authentication, permissions

@api_view(['GET', 'POST','PUT'])
def pais(request):
    print(request)
    if request.method == 'GET': 
        snippets = Pais.objects.all()
        serializer = PaisSerializador(snippets, many=True)        
        return Response(serializer.data)
    elif request.method == 'POST':
        print(request.data)
        serializer = PaisSerializador(data=request.data)        
        if serializer.is_valid():
            serializer.save() # save to db
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT': # user posting data
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BaseManageView(APIView):
    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'VIEWS_BY_METHOD'):
            raise Exception("La variable debe ser definida en el ManageView")
        if request.method in self.VIEWS_BY_METHOD:
            return self.VIEWS_BY_METHOD[request.method]()(request, *args, **kwargs)        
        
        return Response(status=405)
class ProductDestroyView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProducDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProducCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductManageView(BaseManageView):
    VIEWS_BY_METHOD = {
        'DELETE': ProductDestroyView.as_view,
        'GET': ProducDetailView.as_view,
        'PUT': ProductUpdateView.as_view,        
    }