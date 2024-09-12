from django.urls import path
from . import views

urlpatterns = [
    # Redirecciona la vista de premios
    path('premios/', views.view_premios, name='premios_views'),
    path('canjearview/<int:id>/', views.canjear, name='canjear_view'),

]