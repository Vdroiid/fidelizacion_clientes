from django.db import models
from clientes.models import UsuarioPersonalizado
# from django.contrib.auth.models import User Para el superusuario

# Create your models here.

class Tarjeta(models.Model):
    # otros campos
    tarjeta = models.CharField(max_length=16, null=True)
    cvc = models.CharField(max_length=3, null=True)
    fecha = models.DateField(null=True)

    usuario = models.ForeignKey(
        UsuarioPersonalizado,
        related_name='tarjetas',  # Especifica un related_name aquí
        on_delete=models.CASCADE
    )
    def __str__(self):
        return f'Tarjeta {self.tarjeta} de {self.usuario}'


