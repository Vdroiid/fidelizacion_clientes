from django.test import TestCase, Client
from .models import Premio
from django.urls import reverse

#---------------------------- Purbas unitarias para los modelos -----------------------------#
#--------------------------------------------------------------------------------------------#
class PremiosModelTest(TestCase):
    def setUp(self):
        self.premio = Premio.objects.create(Nombre_Premio="Laptop Dell", Valor=3)
    def test_premio_str(self):
        self.assertEqual(str(self.premio), "Laptop Dell")
        
    def test_premio_creation(self):
        premio = Premio.objects.get(Nombre_Premio="Laptop Dell")
        self.assertEqual(premio.Valor, 3)

#---------------------------- Purbas unitarias para las vistas -----------------------------#
#-------------------------------------------------------------------------------------------#
class ViewPremiosTestCase(TestCase):
    def setUp(self):
        # Configura el cliente de pruebas
        self.client = Client()

        # Crea algunos objetos Empresa para usar en las pruebas
        self.premio1 = Premio.objects.create(
            Nombre_Premio='Premio 1',
            Valor = 45
        )
        self.premio2 = Premio.objects.create(
            Nombre_Premio='Premio 2',
            Valor = 100
        )

    def test_view_premios_status_code(self):
        # Realiza una solicitud GET a la vista
        response = self.client.get(reverse('premios_views'))

        # Verifica que la respuesta tiene el código de estado 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_view_premios_template_used(self):
        # Realiza una solicitud GET a la vista
        response = self.client.get(reverse('premios_views'))

        # Verifica que se está usando el template correcto
        self.assertTemplateUsed(response, 'beneficios.html')

    def test_view_premios_context(self):
        # Realiza una solicitud GET a la vista
        response = self.client.get(reverse('premios_views'))

        # Verifica que la vista pasa el contexto correcto al template
        self.assertIn('premios', response.context)
        self.assertEqual(len(response.context['premios']), 2)

        # Verifica que los objetos Empresa están en el contexto
        self.assertIn(self.premio1, response.context['premios'])
        self.assertIn(self.premio2, response.context['premios'])

class CanjearViewTestCase(TestCase):
    def setUp(self):
        # Configura el cliente de pruebas
        self.client = Client()

        # Crea un objeto Empresa para usar en las pruebas
        self.premio_prueba = Premio.objects.create(
                    Nombre_Premio='Premio 3',
                    Valor = 200
                )

    def test_canjear_view_status_code(self):
        # Realiza una solicitud GET a la vista para un objeto existente
        response = self.client.get(reverse('canjear_view', kwargs={'id': self.premio_prueba.id}))

        # Verifica que la respuesta tiene el código de estado 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_canjear_view_template_used(self):
        # Realiza una solicitud GET a la vista para un objeto existente
        response = self.client.get(reverse('canjear_view', kwargs={'id': self.premio_prueba.id}))

        # Verifica que se está usando el template correcto
        self.assertTemplateUsed(response, 'beneficios.html')

    def test_canjear_view_context(self):
        # Realiza una solicitud GET a la vista para un objeto existente
        response = self.client.get(reverse('canjear_view', kwargs={'id': self.premio_prueba.id}))

        # Verifica que la vista pasa el contexto correcto al template
        self.assertIn('premio', response.context)
        self.assertEqual(response.context['premio'], self.premio_prueba)

    def test_canjear_view_404_for_invalid_id(self):
        # Realiza una solicitud GET a la vista con un ID que no existe
        response = self.client.get(reverse('canjear_view', kwargs={'id': 99999}))

        # Verifica que la vista devuelve un error 404
        self.assertEqual(response.status_code, 404)

