from django.contrib import admin
from .models import Productos

# Register your models here.

# Register mi modelo de Premios para verlo en admin.
admin.site.register(Productos)