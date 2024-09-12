from django.db import models

# Create your models here.
class Productos(models.Model):
    producto = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    Imagen = models.ImageField(upload_to='premios/', null=True, blank=True)
    def __str__(self):
        return self.producto
