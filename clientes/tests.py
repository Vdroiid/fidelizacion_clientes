from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.authtoken.models import Token
from clientes.models import UsuarioPersonalizado  # Asegúrate de ajustar la importación según tu modelo personalizado
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .views import protected_view

class ProtectedViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

        # Crea un usuario de prueba utilizando el manager de UsuarioPersonalizado
        self.user = UsuarioPersonalizado.objects.create_user(
            username='testuser',
            telefono='123456789',
            genero='Masculino',
            direccion='Calle Ejemplo 123',
            estado='Activo',
            ciudad='Ciudad de Ejemplo',
            puntos=0,
            password='12345'
        )
        self.token = Token.objects.create(user=self.user)

    def test_protected_view(self):
        # Configura la solicitud GET con el token de autenticación
        request = self.factory.get('/api/protected-view/')
        request.user = self.user  # Simula que el usuario está autenticado
        request.auth = self.token  # Añade el token de autenticación a la solicitud

        # Llama a la vista protegida
        response = protected_view(request)

        # Verifica el código de estado y el contenido de la respuesta
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'message': 'Bienvenido, has iniciado sesión correctamente.'})
