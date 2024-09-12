from django.shortcuts import render
from premios.models import Premio
from django.shortcuts import render, get_object_or_404
from clientes.models import UsuarioPersonalizado

def view_premios(request):
    activar= None
    #Obtener todos los premios que hay en la base de datos
    premios = Premio.objects.all()
    suma_premios = Premio.objects.count()

    return render(request, 'beneficios.html', {'activar':activar, 'premios':premios, 'suma_premios':suma_premios})

def canjear(request, id):
    activar = None
    mensaje = ""
    # Recuperamos los datos del usuario actual
    usuario_actual = request.user
    clientes = UsuarioPersonalizado.objects.filter(username=usuario_actual.username)

    # Recibimos el id del premio a la que se dio click
    premio = get_object_or_404(Premio, id=id)
    puntos_a_restar = premio.Valor
    
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
            mensaje = "Ya no te alcanza con tus puntos"
            activar = "flex"

    #Obtener todos los premios que hay en la base de datos
    premios = Premio.objects.all()
    suma_premios = Premio.objects.count()
    return render(request, 'beneficios.html', {'activar': activar, 'mensaje':mensaje, 'premios':premios, 'suma_premios':suma_premios})
   