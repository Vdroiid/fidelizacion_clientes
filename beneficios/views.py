from django.shortcuts import render
from beneficios.models import Empresa

# Create your views here.
def view_beneficios(request):
    #Obtener todos los clientes desde la base de datos
    beneficios = Empresa.objects.all()

    #Pasar los clientes a la plantilla como texto
    return render(request, 'beneficios1.html', {'nombre':beneficios})

def detalles(request, id):
    beneficio = Empresa.objects.get(id=id)
    return render(request, 'beneficio_detalles.html', {'beneficio': beneficio})
