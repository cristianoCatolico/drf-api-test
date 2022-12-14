from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pais, Product
from .serializers import PaisSerializador, ProductSerializer
from rest_framework.generics import DestroyAPIView, UpdateAPIView, RetrieveAPIView, CreateAPIView

from rest_framework import authentication, permissions
from rest_framework import viewsets
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

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class= ProductSerializer