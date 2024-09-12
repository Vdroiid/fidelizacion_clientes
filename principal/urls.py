from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.PrincipalView, name= "PrincipalView"),

    # Para redireccionar
    path('principal_views/', views.PrincipalView, name='principal_views'),
    path('canjear/<int:id>/', views.canjear, name='canjear'),
    path('cerrar/', views.cerrar, name='cerrar'),

    path('admin/', admin.site.urls)
]
