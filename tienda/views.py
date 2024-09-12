from django.shortcuts import render
from tienda.models import Productos
from clientes.models import UsuarioPersonalizado
from django.shortcuts import render, get_object_or_404

# Create your views here.
def view_tienda(request):
    activar=None
    #Obtener todos los premios que hay en la base de datos
    productos = Productos.objects.all()

    return render(request, 'tienda.html', {'activar':activar, 'productos':productos})

def comprar(request, id):
    activar = None
    mensaje = ""
    # Recuperamos los datos del usuario actual
    usuario_actual = request.user
    cliente = UsuarioPersonalizado.objects.filter(username=usuario_actual.username)

    # Recibimos el id del producto a la que se dio click
    productos = get_object_or_404(Productos, id=id)
    precio = productos.precio // 100
    suma_puntos = precio * 5
    # Iteramos clientes para actualizar clientes
    for client in cliente:
        if client.puntos:
            # Modificar el campo 'puntos' del cliente
            client.puntos += suma_puntos 
            # Guardar los cambios en la base de datos
            client.save()
            activar = "flex"
            mensaje = "Se sumaron " + str(suma_puntos) + " puntos a tu cuenta"
    #Obtener todos los premios que hay en la base de datos
    productos = Productos.objects.all()
    return render(request, 'tienda.html', {'activar': activar, 'mensaje':mensaje, 'productos':productos})