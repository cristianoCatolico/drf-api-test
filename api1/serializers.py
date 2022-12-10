from rest_framework import serializers
from .models import Pais

def starts_with_c(value):
    if value[0].lower()!= 'c':
        raise serializers.ValidationError('El nombre debe empezar con C')

class PaisSerializador(serializers.Serializer):
    nombre = serializers.CharField(max_length= 100, validators = [starts_with_c])
    moneda = serializers.CharField(max_length= 10)

    def validate_moneda(self, value):
        listMoneda = ['SOL', 'PESO']
        if value not in listMoneda:
            raise serializers.ValidationError("Moneda no reconocida")
        return value
    
    def validate(self, data):
        nombre = data.get('nombre')
        moneda = data.get('moneda')
        if nombre!='catolico':
            raise serializers.ValidationError("No acepto otro")
        return data
"""    class Meta:
        model = Pais
        fields = ('nombre', 'moneda')
        """