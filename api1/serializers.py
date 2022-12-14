from rest_framework import serializers
from .models import Pais, Product

def starts_with_c(value):
    if value[0].lower()!= 'b':
        raise serializers.ValidationError('El nombre debe empezar con b')

class PaisSerializador(serializers.Serializer):
    nombre = serializers.CharField(max_length= 100, validators = [starts_with_c])
    moneda = serializers.CharField(max_length= 10)


    def create(self, validated_data):
        return Pais(**validated_data)
    def validate_moneda(self, value):
        listMoneda = ['SOL', 'PESO', 'REAL']
        if value not in listMoneda:
            raise serializers.ValidationError("Moneda no reconocida")
        return value
"""    
    def validate(self, data):
        nombre = data.get('nombre')
        moneda = data.get('moneda')
        if nombre!='catolico':
            raise serializers.ValidationError("No acepto otro")
        return data
    class Meta:
        model = Pais
        fields = ('nombre', 'moneda')
        """
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
