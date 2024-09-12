from rest_framework import serializers
from .models import UsuarioPersonalizado


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPersonalizado
        fields = '__all__'