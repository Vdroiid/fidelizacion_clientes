from django.db import models # type: ignore

# Create your models here.
class Premio(models.Model):
    Nombre_Premio = models.CharField(max_length=50)
    # <blanck> permite que el campo sea opcional en los formularios de Django.
    # <null> permite que el campo sea opcional en la base de datos SQLite3 (porque SQLite3 no distingue entre campos nulos y no nulos por defecto).
    # <upload_to> para especificar la carpeta dentro del directorio de medios donde se guardarán las imágenes.
    Imagen = models.ImageField(upload_to='premios/', null=True, blank=True)
    # Luego hay que modificar <settings.py>
    # Además se requiere instalar <python -m pip install Pillow>
    Valor = models.IntegerField(default=0)
    def __str__(self):
        return self.Nombre_Premio