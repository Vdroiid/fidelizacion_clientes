from django.urls import path
from . import views

urlpatterns = [
    # Redirecciona la vista de premios
    path('carrito/', views.view_carrito, name='carrito_views'),
    path('redireccion/<int:id>/', views.redireccion, name='redireccion'),
    path('eliminar/<int:id>/', views.elimina_elemento, name='eliminar'),
    path('pagarview/<int:id>/', views.pagar_view, name='pagar_view'),
]
