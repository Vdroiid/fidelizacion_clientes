from django.shortcuts import render

from clientes.models import UsuarioPersonalizado
from premios.models import Premio
from .models import Tarjeta
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
# Para rediregir a login
from django.shortcuts import redirect
from django.urls import reverse

def PrincipalView(request):
    activar = None
    # Filtrar los datos del usuario que inició sesión
    usuario_actual = request.user
    clientes = UsuarioPersonalizado.objects.filter(username=usuario_actual.username)
    # Obtener todos los premios de la base de datos
    premios = Premio.objects.all()
    vista_restringida = premios[:4]  # Filtrar los primeros tres premios
    suma_premios = Premio.objects.count()
    """
    # Se puede pasar los datos a la platilla de esta manera, como contexto:
        context = {
            'tarjeta': tarjeta,
            'clientes': clientes,
            'premios_res': premios_res,
            'suma_premios': suma_premios,
            'premios_all': premios_all,
        }
    """
    # Filtramos los datos de la tarjeta del usuario actual
    tarjeta = Tarjeta.objects.filter(usuario=usuario_actual.id)
    return render(request, 'iniciousua.html', {'activar':activar, 'tarjeta':tarjeta, 'UsuarioPersonalizado':clientes, 'premios_res':vista_restringida, 'suma_premios':suma_premios, 'premios_all':premios})

def canjear(request, id):
    # Recuperamos los datos del usuario actual
    usuario_actual = request.user
    clientes = UsuarioPersonalizado.objects.filter(username=usuario_actual.username)

    # Recibimos el id y recuperamos, solo el premio cliqueado
    premio = get_object_or_404(Premio, id=id)
    puntos_a_restar = premio.Valor
    mensaje = ""
    activar = None
    # Iteramos clientes para actualizar clientes
    for cliente in clientes:
        if cliente.puntos >= puntos_a_restar:
            # Modificar el campo 'puntos' del cliente
            cliente.puntos -= puntos_a_restar
            # Guardar los cambios en la base de datos
            cliente.save()
            mensaje = "Se restarón " + str(puntos_a_restar) + " puntos a tu cuenta"
            activar = "flex"
        else: 
            # messages.success(request, 'No tienes suficientes puntos')
            mensaje = "Lo siento, no le alcanza con tus puntos"
            activar = "flex"
    # Filtramos los datos de la tarjeta del usuario actual
    tarjeta = Tarjeta.objects.filter(usuario=usuario_actual.id)
    #Obtener todos premios
    premios = Premio.objects.all()
    vista_restringida = premios[:4]  # Filtrar los primeros tres premios
    suma_premios = Premio.objects.count()
    return render(request, 'iniciousua.html', {'activar': activar, 'mensaje':mensaje, 'tarjeta':tarjeta, 'UsuarioPersonalizado':clientes, 'premios_res':vista_restringida, 'suma_premios':suma_premios, 'premios_all':premios})
   
def cerrar(request):
    return redirect(reverse('admin:index'))
