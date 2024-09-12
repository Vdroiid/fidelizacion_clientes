from django.db import models

# Create your models here.
class Empresa(models.Model):
    Nombre = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=10)
    Correo = models.CharField(max_length=50)
    Web = models.CharField(max_length=50)
    titulo_beneficio = models.CharField(max_length=50, null=True)
    descripcion_beneficio = models.TextField(null=True)
    inicio = models.DateField(null=True)
    fin = models.DateField(null=True)

    Imagen = models.ImageField(upload_to='premios/', null=True, blank=True)


    # Es el que muestra en nombre de objeto
    def __str__(self):
        return self.Nombre