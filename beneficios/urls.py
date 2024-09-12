from django.urls import path
from .views import view_beneficios
from . import views

urlpatterns = [
    path('', view_beneficios, name='obtener_beneficios'),

    #Para que se redireccione
    path('beneficios/', views.view_beneficios, name='beneficios_views'),
    path('detalles/<int:id>/', views.detalles, name='detalles'),
]
