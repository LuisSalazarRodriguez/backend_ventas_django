from rest_framework import serializers

from .models import *

class LineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linea
        fields = '__all__'
        
class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'