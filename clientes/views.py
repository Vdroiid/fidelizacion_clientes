from rest_framework import viewsets

from .models import UsuarioPersonalizado
from .serializers import ClienteSerializer
from django.shortcuts import render


from django.contrib.auth.views import LoginView, LogoutView

class MyModelViewSet(viewsets.ModelViewSet):
    queryset = UsuarioPersonalizado.objects.all()
    serializer_class = ClienteSerializer
    
# Create your views here.
def IndexView(request):
    return render(request, "index.html")

def ClienteView(request):
    #Obtener todos los clientes desde la base de datos
    clientes = UsuarioPersonalizado.objects.all()
    #Pasar los clientes a la plantilla como texto
    return render(request, 'clientes.html', {'clientes':clientes})

