from django.urls import path
from . import views

urlpatterns = [
    # Redirecciona la vista de premios
    path('tienda/', views.view_tienda, name='tienda_views'),
    path('comprarview/<int:id>/', views.comprar, name='comprar_view'),
]