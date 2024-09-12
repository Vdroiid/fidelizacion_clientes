from django.shortcuts import render
from .models import Carrito
# Para la redirección 
from django.shortcuts import redirect
from django.urls import reverse
from tienda.models import Productos
from clientes.models import UsuarioPersonalizado
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# Create your views here.
def view_carrito(request):
    #Obtener todos los premios que hay en la base de datos
    productos = Carrito.objects.all()
        # Inicializa la variable total
    total = 0

    # Itera sobre los productos en el carrito y suma los precios
    for producto in productos:
        total += producto.precio
    pagar = int(total)

    return render(request, 'carrito.html', {'productos':productos, 'total':total, 'pagar':pagar})

def pagar_view(request, id):
    # Filtrar los resultado y borrarlos en la base de datios
    # Eso hará que lo que se puso en la "redireccion(), no se quede"
    activar = None
    mensaje = ""
    # Recuperamos los datos del usuario actual
    usuario_actual = request.user
    cliente = UsuarioPersonalizado.objects.filter(username=usuario_actual.username)

    calculo = id // 100
    puntos = calculo * 5
    

    # Iteramos clientes para actualizar clientes
    for client in cliente:
        if client.puntos:
            # Modificar el campo 'puntos' del cliente
            client.puntos += puntos 
            # Guardar los cambios en la base de datos
            client.save()
            activar = "flex"
            mensaje = "Se sumaron " + str(puntos) + " puntos a tu cuenta"
    #Obtener todos los premios que hay en la base de datos
    productos = Productos.objects.all()
    Carrito.objects.all().delete()


    return render(request, 'tienda.html', {'activar': activar, 'mensaje':mensaje, 'productos':productos})


def redireccion(request, id):
    producto = get_object_or_404(Productos, id=id)

    cantidad = 1
        # Buscar en el carrito si el producto ya está presente
    carrito_item = Carrito.objects.filter(producto=producto).first()
    
    if carrito_item:
        # Si el producto ya está en el carrito, actualizar la cantidad
        carrito_item.cantidad += cantidad
        carrito_item.precio = producto.precio * carrito_item.cantidad  # Actualizar el precio basado en la nueva cantidad
        carrito_item.save()
    else:
        # Si el producto no está en el carrito, crear una nueva entrada
        Carrito.objects.create(
            producto=producto,
            precio=producto.precio * cantidad,  # Establecer el precio basado en la cantidad
            cantidad=cantidad,
        )

    return redirect(reverse('tienda_views'))

def elimina_elemento(request, id):
    # Buscar el ítem del carrito usando el id proporcionado
    carrito_item = get_object_or_404(Carrito, id=id)
    
    # Eliminar el ítem del carrito
    carrito_item.delete()

    # Redirigir al usuario a la vista del carrito
    return redirect(reverse('carrito_views'))