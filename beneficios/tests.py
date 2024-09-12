from django.test import TestCase, Client
from .models import Empresa
from django.urls import reverse

#---------------------------- Purbas unitarias de los modelos -----------------------------#
#------------------------------------------------------------------------------------------#

class EmpresaModelTest(TestCase):
    def setUp(self):
        self.beneficios = Empresa.objects.create(Nombre="Bimbo", Telefono="9876543214", Correo="bimbo@gmail.com", Web="bimbo.com", titulo_beneficio="Galleta bimbo", descripcion_beneficio="Esto es una promoció 3x$5")

    def test_empresa_str(self):
        self.assertEqual(str(self.beneficios), "Bimbo")
        
    def test_beneficios_creation(self):
        beneficio = Empresa.objects.get(Nombre="Bimbo")
        self.assertEqual(beneficio.Web, "bimbo.com")

#---------------------------- Purbas unitarias de las vistas -----------------------------#
#-----------------------------------------------------------------------------------------#
class ViewBeneficiosTestCase(TestCase):
    def setUp(self):
        # Configura el cliente de pruebas
        self.client = Client()

        # Crea algunos objetos Empresa para usar en las pruebas
        self.empresa1 = Empresa.objects.create(
            Nombre='Empresa 1',
            Telefono='1234567890',
            Correo='empresa1@example.com',
            Web='http://empresa1.com',
            titulo_beneficio='Beneficio 1',
            descripcion_beneficio='Descripción del beneficio 1',
            inicio='2024-01-01',
            fin='2024-12-31'
        )
        self.empresa2 = Empresa.objects.create(
            Nombre='Empresa 2',
            Telefono='0987654321',
            Correo='empresa2@example.com',
            Web='http://empresa2.com',
            titulo_beneficio='Beneficio 2',
            descripcion_beneficio='Descripción del beneficio 2',
            inicio='2024-02-01',
            fin='2024-11-30'
        )

    def test_view_beneficios_status_code(self):
        # Realiza una solicitud GET a la vista
        response = self.client.get(reverse('beneficios_views'))

        # Verifica que la respuesta tiene el código de estado 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_view_beneficios_template_used(self):
        # Realiza una solicitud GET a la vista
        response = self.client.get(reverse('beneficios_views'))

        # Verifica que se está usando el template correcto
        self.assertTemplateUsed(response, 'beneficios1.html')

    def test_view_beneficios_context(self):
        # Realiza una solicitud GET a la vista
        response = self.client.get(reverse('beneficios_views'))

        # Verifica que la vista pasa el contexto correcto al template
        self.assertIn('nombre', response.context)
        self.assertEqual(len(response.context['nombre']), 2)

        # Verifica que los objetos Empresa están en el contexto
        self.assertIn(self.empresa1, response.context['nombre'])
        self.assertIn(self.empresa2, response.context['nombre'])

class DetallesViewTestCase(TestCase):
    def setUp(self):
        # Configura el cliente de pruebas
        self.client = Client()

        # Crea un objeto Empresa para usar en las pruebas
        self.empresa = Empresa.objects.create(
            Nombre='Empresa de Prueba',
            Telefono='1122334455',
            Correo='empresa_prueba@example.com',
            Web='http://empresa-prueba.com',
            titulo_beneficio='Beneficio de Prueba',
            descripcion_beneficio='Descripción del beneficio de prueba',
            inicio='2024-03-01',
            fin='2024-10-31'
        )

    def test_detalles_view_status_code(self):
        # Realiza una solicitud GET a la vista para un objeto existente
        response = self.client.get(reverse('detalles', kwargs={'id': self.empresa.id}))

        # Verifica que la respuesta tiene el código de estado 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_detalles_view_template_used(self):
        # Realiza una solicitud GET a la vista para un objeto existente
        response = self.client.get(reverse('detalles', kwargs={'id': self.empresa.id}))

        # Verifica que se está usando el template correcto
        self.assertTemplateUsed(response, 'beneficio_detalles.html')

    def test_detalles_view_context(self):
        # Realiza una solicitud GET a la vista para un objeto existente
        response = self.client.get(reverse('detalles', kwargs={'id': self.empresa.id}))

        # Verifica que la vista pasa el contexto correcto al template
        self.assertIn('beneficio', response.context)
        self.assertEqual(response.context['beneficio'], self.empresa)

    def test_detalles_view_404_for_invalid_id(self):
        # Realiza una solicitud GET a la vista con un ID que no existe
        response = self.client.get(reverse('detalles', kwargs={'id': 99999}))

        # Verifica que la vista devuelve un error 404
        self.assertEqual(response.status_code, 404)
