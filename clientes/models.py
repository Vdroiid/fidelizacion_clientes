from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

admin.site.site_header = "Página Principal"
admin.site.site_title = "NetCard"
admin.site.index_title = "Fidelización"
admin.site.site_url = '/'
# Definir una tupla con los valores para el campo 'genero'
GENEROS_CHOICES = (
    ("Masculino", "Masculino"),
    ("Femenino", "Femenino"),
    ("Otro", "Otro"),
)

class CustomUserManager(BaseUserManager):
    def create_user(self, username, telefono, genero, direccion, estado, ciudad, puntos, password=None, **extra_fields):
        if not username:
            raise ValueError('El nombre de usuario debe ser establecido')
        usuario = self.model(
            username=username,
            telefono=telefono,
            genero=genero,
            direccion=direccion,
            estado=estado,
            ciudad=ciudad,
            puntos=puntos,
            **extra_fields
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, username, telefono, genero, direccion, estado, ciudad, puntos, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, telefono, genero, direccion, estado, ciudad, puntos, password, **extra_fields)

class UsuarioPersonalizado(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    telefono = models.CharField(max_length=10, unique=True, default='')
    genero = models.CharField(max_length=10, choices=GENEROS_CHOICES, default='Masculino')
    direccion = models.CharField(max_length=100, default='')
    estado = models.CharField(max_length=100, default='')
    ciudad = models.CharField(max_length=100, default='')
    puntos = models.IntegerField(default=0)

    

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['telefono', 'genero', 'direccion', 'estado', 'ciudad', 'puntos']

    # Especificar related_name para groups
    groups = models.ManyToManyField(
        Group,
        verbose_name=('Grupo a la que pertenece'),
        blank=False,
        related_name='custom_user_set_groups',  # Nombre de acceso inverso único
        related_query_name='user'
    )

    # Especificar related_name para user_permissions
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('Permiso del usuario'),
        blank=True,
        related_name='custom_user_set_permissions',  # Nombre de acceso inverso único
        related_query_name='user'
    )

    class Meta:
        verbose_name = "Cuenta de cliente"
        verbose_name_plural = "Cuentas de clientes"

    def __str__(self):
        return self.username
