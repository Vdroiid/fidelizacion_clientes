from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioPersonalizado

class CustomUserAdmin(UserAdmin):
    model = UsuarioPersonalizado
    list_display = ['username', 'telefono', 'genero', 'direccion', 'estado', 'ciudad', 'puntos', 'is_staff']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('telefono', 'genero', 'direccion', 'estado', 'ciudad', 'puntos')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'telefono', 'genero', 'direccion', 'estado', 'ciudad', 'puntos', 'password1', 'password2'),
        }),
    )
    search_fields = ('username', 'telefono')
    ordering = ('username',)

admin.site.register(UsuarioPersonalizado, CustomUserAdmin)
